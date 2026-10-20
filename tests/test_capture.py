"""Run from the project folder: python -m unittest discover -s tests -v"""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import tempfile
import unittest
from unittest.mock import patch
from PySide6.QtCore import QPoint, QPointF, QRectF, Qt, QSettings
from PySide6.QtGui import QColor, QImage, QPixmap, QFontDatabase
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from LumaShot import CaptureOverlay
from LumaShot import History, Mark, render_crop
from LumaShot import LANGUAGES, STRINGS
from LumaShot import MainWindow, BASE_STYLE

APP = QApplication.instance() or QApplication([])
if APP.platformName() == "offscreen":
    for font in ("segoeui.ttf", "segoeuib.ttf", "seguisym.ttf"):
        QFontDatabase.addApplicationFont(os.path.join(os.environ.get("WINDIR", "C:/Windows"), "Fonts", font))


class CaptureTests(unittest.TestCase):
    def test_every_language_has_every_string(self):
        keys = set(STRINGS["ro"])
        for language in LANGUAGES:
            self.assertEqual(keys, set(STRINGS[language]))
            for key in keys:
                self.assertTrue(STRINGS[language][key])
            self.assertEqual(len(STRINGS[language]["colors"]), 6)

    def test_crop_preserves_physical_resolution(self):
        source = QImage(300, 200, QImage.Format.Format_RGB32)
        source.fill(QColor("white"))
        source.setPixelColor(60, 50, QColor("blue"))
        crop = render_crop(source, QRectF(20, 15, 70, 60), [], 1.5)
        self.assertEqual((crop.width(), crop.height()), (105, 90))
        self.assertEqual(crop.pixelColor(30, 28), QColor("blue"))
        self.assertEqual(crop.devicePixelRatio(), 1)

    def test_mask_replaces_source_pixels_in_saved_file(self):
        source = QImage(200, 200, QImage.Format.Format_RGB32)
        source.fill(QColor("#ff00ff"))
        marks = [Mark("mask", QPointF(20, 20), QPointF(60, 60))]
        crop = render_crop(source, QRectF(10, 10, 80, 80), marks, 2)
        with tempfile.TemporaryDirectory() as temp:
            path = os.path.join(temp, "redacted.png")
            self.assertTrue(crop.save(path))
            saved = QImage(path)
            for x in range(20, 100):
                for y in range(20, 100):
                    self.assertEqual(saved.pixelColor(x, y), QColor("#111118"))
            self.assertEqual(saved.pixelColor(5, 5), QColor("#ff00ff"))

    def test_undo_redo_and_new_branch(self):
        h = History()
        first = Mark("rect", QPointF(1, 1), QPointF(10, 10))
        second = Mark("line", QPointF(2, 2), QPointF(9, 9))
        h.add(first)
        h.add(second)
        h.undo()
        self.assertEqual(h.items, [first])
        h.redo()
        self.assertEqual(h.items, [first, second])
        h.undo()
        h.add(first)
        h.redo()
        self.assertEqual(h.items, [first, first])

    def test_all_tools_render_without_errors(self):
        source = QImage(400, 400, QImage.Format.Format_RGB32)
        source.fill(QColor("white"))
        for kind in ["pen", "line", "arrow", "rect", "ellipse", "text", "highlight", "mask", "number"]:
            mark = Mark(kind, QPointF(30, 60), QPointF(90, 90),
                        "#ff0000", 4, "1", [QPointF(50, 80)])
            image = render_crop(source, QRectF(0, 0, 200, 200), [mark], 2)
            self.assertFalse(image.isNull())
            self.assertNotEqual(image, source)

    def test_selection_drawing_and_copy_signal_in_all_languages(self):
        for language in LANGUAGES:
            screen = APP.primaryScreen()
            pix = QPixmap(screen.size())
            pix.fill(QColor("#ffffff"))
            overlay = CaptureOverlay(screen, pix, language)
            overlay.show()
            APP.processEvents()
            results = []
            overlay.finished.connect(lambda action, image: results.append((action, image)))
            QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=QPoint(40, 40))
            QTest.mouseMove(overlay, QPoint(400, 300))
            QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=QPoint(400, 300))
            self.assertEqual(overlay.selection, QRectF(40, 40, 360, 260))
            overlay.set_tool("arrow")
            QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=QPoint(80, 80))
            QTest.mouseMove(overlay, QPoint(200, 200))
            QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=QPoint(200, 200))
            self.assertEqual(len(overlay.history.items), 1)
            QTest.keyClick(overlay, Qt.Key.Key_C, Qt.KeyboardModifier.ControlModifier)
            self.assertEqual(results[-1][0], "copy")
            self.assertEqual(results[-1][1].size().width(), 360)
            overlay.close()
            APP.processEvents()


class ApplicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        settings = QSettings(os.path.join(self.temp.name, "settings.ini"), QSettings.Format.IniFormat)
        self.settings_patch = patch("LumaShot.QSettings", return_value=settings)
        self.hotkey_patch = patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=0)
        self.settings_patch.start()
        self.hotkey_patch.start()
        APP.setStyle("Fusion")
        APP.setStyleSheet(BASE_STYLE)
        self.window = MainWindow()
        self.window.tray.hide()
        self.window.folder = self.temp.name
        self.window.restore_window = False
        self.image = QImage(150, 100, QImage.Format.Format_RGB32)
        self.image.fill(QColor("blue"))

    def tearDown(self):
        APP.removeNativeEventFilter(self.window.hotkeys)
        self.window.quitting = True
        self.window.close_overlays()
        self.window.hide()
        self.window.deleteLater()
        APP.processEvents()
        self.hotkey_patch.stop()
        self.settings_patch.stop()
        self.temp.cleanup()

    def test_languages_persist_and_capture_button_fits(self):
        for language in LANGUAGES:
            self.window.change_language(language)
            APP.processEvents()
            self.window.show()
            APP.processEvents()
            self.assertGreaterEqual(self.window.capture_button.height(), 56)
            self.assertEqual(self.window.lang, language)
            self.assertIn(STRINGS[language]["capture"], self.window.capture_button.text())
            if language != "ro":
                self.assertEqual(self.window.settings.value("language"), language)
            if os.environ.get("LUMASHOT_QA_DIR"):
                self.window.grab().save(os.path.join(os.environ["LUMASHOT_QA_DIR"], f"ui-{language}.png"))

    def test_png_and_jpeg_save(self):
        for extension, fmt in [("png", "PNG"), ("jpg", "JPEG")]:
            filename = os.path.join(self.temp.name, "capture."+extension)
            with patch("LumaShot.QFileDialog.getSaveFileName", return_value=(filename, fmt)):
                self.window.finish_capture("save", self.image)
            self.assertTrue(os.path.isfile(filename))
            self.assertEqual(QImage(filename).size(), self.image.size())

    def test_save_cancel_keeps_annotations(self):
        pix = QPixmap(APP.primaryScreen().size())
        pix.fill(QColor("white"))
        overlay = CaptureOverlay(APP.primaryScreen(), pix, "en")
        overlay.selection = QRectF(20, 20, 100, 100)
        overlay.history.add(Mark("arrow", QPointF(30, 30), QPointF(70, 70)))
        overlay.show()
        self.window.overlays = [overlay]
        with patch("LumaShot.QFileDialog.getSaveFileName", return_value=("", "")):
            self.window.finish_capture("save", self.image)
        self.assertTrue(overlay.isVisible())
        self.assertEqual(len(overlay.history.items), 1)

    def test_copy_sets_image_on_clipboard(self):
        self.window.finish_capture("copy", self.image)
        self.assertEqual(APP.clipboard().image().size(), self.image.size())


if __name__ == "__main__":
    unittest.main()

