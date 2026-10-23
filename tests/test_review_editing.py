"""Synthetic recordings and isolated settings; no real startup registration or devices."""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch
from PySide6.QtCore import QPoint, QPointF, QRect, QRectF, Qt, QEvent, QSettings
from PySide6.QtGui import QImage, QPixmap, QColor, QMouseEvent, QFontDatabase
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from PySide6.QtMultimedia import QMediaPlayer
import LumaShot as app
from test_recording import SyntheticGrab, until

APP = QApplication.instance() or QApplication([])
if APP.platformName() == "offscreen":
    for filename in ("segoeui.ttf", "segoeuib.ttf", "seguisym.ttf"):
        QFontDatabase.addApplicationFont(str(Path(os.environ.get("WINDIR", "C:/Windows"))/"Fonts"/filename))
SHIFT = Qt.KeyboardModifier.ShiftModifier


class EditingTests(unittest.TestCase):
    def setUp(self):
        pix = QPixmap(APP.primaryScreen().size())
        pix.fill(QColor("white"))
        self.overlay = app.CaptureOverlay(APP.primaryScreen(), pix, "ro")
        self.overlay.selection = QRectF(20, 20, 620, 500)
        self.overlay.show()
        APP.processEvents()

    def tearDown(self):
        self.overlay.close()
        APP.processEvents()

    def drag(self, start, end):
        QTest.mousePress(self.overlay, Qt.MouseButton.LeftButton, SHIFT, QPoint(*start))
        event = QMouseEvent(QEvent.Type.MouseMove, QPointF(*end), QPointF(self.overlay.mapToGlobal(QPoint(*end))), Qt.MouseButton.NoButton,
                            Qt.MouseButton.LeftButton, SHIFT)
        APP.sendEvent(self.overlay, event)
        QTest.mouseRelease(self.overlay, Qt.MouseButton.LeftButton, SHIFT, QPoint(*end))

    def test_shift_move_resize_and_undo_preserve_capture_rectangle(self):
        o = self.overlay
        crop = QRectF(o.selection)
        original = app.Mark("rect", QPointF(100, 100), QPointF(200, 180))
        o.history.add(original)
        self.drag((100, 140), (130, 160))
        self.assertEqual(o.history.items[0].start, QPointF(130, 120))
        self.assertEqual(o.history.items[0].end, QPointF(230, 200))
        self.assertEqual(o.selection, crop)
        self.drag((230, 200), (300, 260))
        self.assertEqual(o.history.items[0].end, QPointF(300, 260))
        o.undo()
        self.assertEqual(o.history.items[0].end, QPointF(230, 200))
        o.undo()
        self.assertEqual(o.history.items, [original])
        o.redo()
        self.assertEqual(o.history.items[0].start, QPointF(130, 120))
        self.assertEqual(o.selection, crop)

    def test_arrow_endpoints_and_freehand_handles_are_editable(self):
        o = self.overlay
        o.history.add(app.Mark("arrow", QPointF(100, 100), QPointF(200, 200)))
        QTest.mouseClick(o, Qt.MouseButton.LeftButton, SHIFT, QPoint(150, 150))
        self.assertEqual(set(o.object_handles()), {"start", "end"})
        self.drag((200, 200), (300, 240))
        self.assertEqual(o.history.items[0].end, QPointF(300, 240))
        pen = app.Mark("pen", QPointF(350, 100), QPointF(450, 200), points=[QPointF(380, 160), QPointF(450, 200)])
        o.history.add(pen)
        o.selected_mark = None
        QTest.mouseClick(o, Qt.MouseButton.LeftButton, SHIFT, QPoint(380, 160))
        self.assertEqual(len(o.object_handles()), 8)
        self.drag((450, 200), (550, 300))
        self.assertEqual(o.history.items[1].points[0], QPointF(410, 220))
        self.assertEqual(o.history.items[1].end, QPointF(550, 300))

    def test_shift_double_click_rewrites_text_and_escape_cancels(self):
        o = self.overlay
        o.history.add(app.Mark("text", QPointF(100, 200), QPointF(100, 200), text="Original"))
        point = app.mark_bounds(o.history.items[0]).center().toPoint()
        QTest.mouseDClick(o, Qt.MouseButton.LeftButton, SHIFT, point)
        self.assertIsNotNone(o.editor)
        o.editor.setText("Text modificat")
        QTest.keyClick(o.editor, Qt.Key.Key_Return)
        self.assertEqual(len(o.history.items), 1)
        self.assertEqual(o.history.items[0].text, "Text modificat")
        o.undo()
        self.assertEqual(o.history.items[0].text, "Original")
        o.redo()
        o.begin_text(o.history.items[0].start, 0)
        o.editor.setText("Anulat")
        # Escape in the overlay discards the text editor without changing the mark.
        QTest.keyClick(o, Qt.Key.Key_Escape)
        self.assertEqual(o.history.items[0].text, "Text modificat")
        self.assertIsNone(o.editor)

    def test_text_resize_and_deleted_mark_restore_through_history(self):
        o = self.overlay
        o.history.add(app.Mark("text", QPointF(100, 200), QPointF(100, 200), text="Text"))
        o.selected_mark = 0
        before = app.mark_bounds(o.current_mark())
        point = before.bottomRight().toPoint()
        self.drag((point.x(), point.y()), (point.x()+80, point.y()+30))
        self.assertGreater(app.mark_bounds(o.current_mark()).width(), before.width()+60)
        self.assertGreater(o.current_mark().font_size, 22)
        QTest.keyPress(o, Qt.Key.Key_Shift)
        QTest.keyClick(o, Qt.Key.Key_Delete, SHIFT)
        self.assertFalse(o.history.items)
        o.undo()
        self.assertEqual(len(o.history.items), 1)
        o.undo()
        self.assertEqual(o.history.items[0].font_size, 0)

    def test_selected_object_style_changes_are_undoable(self):
        o = self.overlay
        mark = app.Mark("rect", QPointF(100, 100), QPointF(200, 180), "#ff0000", 3)
        o.history.add(mark)
        QTest.mouseClick(o, Qt.MouseButton.LeftButton, SHIFT, QPoint(100, 140))
        o.set_color("#118769")
        o.set_stroke(6)
        self.assertEqual(o.current_mark().color, "#118769")
        self.assertEqual(o.current_mark().width, 6)
        o.undo()
        self.assertEqual(o.history.items[0].width, 3)
        o.undo()
        self.assertEqual(o.history.items[0].color, "#ff0000")

    def test_selected_text_can_move_from_its_center_without_resizing(self):
        o = self.overlay
        o.history.add(app.Mark("text", QPointF(100, 200), QPointF(100, 200), text="Original"))
        center = app.mark_bounds(o.history.items[0]).center().toPoint()
        QTest.mouseClick(o, Qt.MouseButton.LeftButton, SHIFT, center)
        self.drag((center.x(), center.y()), (center.x()+30, center.y()+20))
        self.assertEqual(o.history.items[0].start, QPointF(130, 220))
        self.assertEqual(o.history.items[0].font_size, 0)


class StartupTests(unittest.TestCase):
    def test_settings_checkbox_registers_and_removes_startup_and_persists_choice(self):
        with tempfile.TemporaryDirectory() as folder:
            prefs = app.JsonSettings(Path(folder)/"settings.json", migrate=False)
            registry = QSettings(str(Path(folder)/"run.ini"), QSettings.Format.IniFormat)
            with patch("LumaShot.JsonSettings", return_value=prefs), \
                 patch.object(app.WindowsStartup, "registry", return_value=registry), \
                 patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=0):
                window = app.MainWindow()
                try:
                    window.show()
                    APP.processEvents()
                    QTest.mouseClick(window.startup_check, Qt.MouseButton.LeftButton, pos=QPoint(10, window.startup_check.height()//2))
                    self.assertTrue(bool(registry.value("LumaShot")))
                    self.assertTrue(prefs.value("start_windows", type=bool))
                    QTest.mouseClick(window.startup_check, Qt.MouseButton.LeftButton, pos=QPoint(10, window.startup_check.height()//2))
                    self.assertFalse(registry.contains("LumaShot"))
                    import json
                    self.assertFalse(json.loads((Path(folder)/"settings.json").read_text(encoding="utf-8"))["start_windows"])
                finally:
                    window.quitting = True
                    window.tray.hide()
                    for controller in (window.hotkeys, window.full_hotkeys, window.record_hotkeys):
                        APP.removeNativeEventFilter(controller)
                        controller.close()
                    window.hide()
                    window.deleteLater()
                    APP.processEvents()

    def test_startup_toggle_quotes_command_and_preserves_other_entries(self):
        with tempfile.TemporaryDirectory() as folder:
            registry = QSettings(str(Path(folder)/"run.ini"), QSettings.Format.IniFormat)
            registry.setValue("AnotherApp", "unrelated")
            startup = app.WindowsStartup()
            with patch.object(startup, "registry", return_value=registry), \
                 patch.object(app.sys, "frozen", True, create=True), \
                 patch.object(app.sys, "executable", "C:/Program Files/LumaShot/LumaShot.exe"):
                startup.set_enabled(True)
                self.assertTrue(startup.enabled())
                command = registry.value("LumaShot")
                self.assertTrue(command.startswith('"'))
                self.assertTrue(command.endswith('" --tray'))
                startup.set_enabled(False)
                self.assertFalse(startup.enabled())
                self.assertEqual(registry.value("AnotherApp"), "unrelated")


class ReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = tempfile.TemporaryDirectory()
        path = Path(cls.fixture.name)/"sample.mp4"
        rec = app.VideoRecording(QRect(0, 0, 320, 240), path, grab_factory=SyntheticGrab)
        results = []
        rec.finished.connect(lambda path, error: results.append(error))
        rec.start()
        self_ready = until(lambda: rec.active)
        if not self_ready:
            raise RuntimeError("Synthetic encoder did not start")
        QTest.qWait(350)
        rec.stop()
        if not until(lambda: bool(results)) or results[0]:
            raise RuntimeError(str(results))
        cls.video = path.read_bytes()
        rec.deleteLater()
        APP.processEvents()

    @classmethod
    def tearDownClass(cls):
        cls.fixture.cleanup()

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.draft = app.VideoDraft()
        self.draft.path.write_bytes(self.video)
        self.review = app.VideoReview(self.draft, self.folder.name, "ro")
        self.review.show()
        APP.processEvents()

    def tearDown(self):
        self.review.release_player()
        self.review.allow_close = True
        self.review.close()
        self.review.deleteLater()
        APP.processEvents()
        self.draft.cleanup()
        self.folder.cleanup()

    def test_play_seek_then_save_default_without_reencoding(self):
        review = self.review
        self.assertTrue(until(lambda: review.player.duration() > 0))
        review.toggle_playback()
        self.assertTrue(until(lambda: review.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState))
        self.assertTrue(until(lambda: not review.video_image.isNull()))
        self.assertFalse(review.video.pixmap().isNull())
        review.toggle_playback()
        review.player.setPosition(100)
        self.assertEqual(review.player.position(), 100)
        review.save_default()
        self.assertTrue(until(lambda: review.saved_path is not None))
        self.assertEqual(Path(review.saved_path).read_bytes(), self.video)
        self.assertEqual(Path(review.saved_path).parent.resolve(), Path(self.folder.name).resolve())

    def test_custom_cancel_and_window_close_cancel_keep_unsaved_draft(self):
        with patch.object(app.QFileDialog, "getSaveFileName", return_value=("", "")):
            self.review.save_custom()
        with patch.object(app.QMessageBox, "exec", return_value=0), \
             patch.object(app.QMessageBox, "clickedButton", return_value=None):
            self.review.close()
        self.assertTrue(self.review.isVisible())
        self.assertTrue(self.draft.path.exists())
        self.assertFalse(list(Path(self.folder.name).glob("*.mp4")))

    def test_failed_save_retains_draft_and_can_retry_to_custom_path(self):
        with patch("LumaShot.save_video_draft", side_effect=OSError("read only")):
            self.review.save_default()
            self.assertTrue(until(lambda: not self.review.saving))
        self.assertTrue(self.draft.path.exists())
        self.assertIn("read only", self.review.status.text())
        target = Path(self.folder.name)/"custom"/"My video.mp4"
        with patch.object(app.QFileDialog, "getSaveFileName", return_value=(str(target), "MP4 (*.mp4)")):
            self.review.save_custom()
        self.assertTrue(until(lambda: self.review.saved_path is not None))
        self.assertEqual(target.read_bytes(), self.video)

    def test_atomic_save_failure_preserves_existing_file(self):
        target = Path(self.folder.name)/"existing.mp4"
        target.write_bytes(b"original")
        with patch("LumaShot.os.replace", side_effect=OSError("disk error")):
            with self.assertRaises(OSError):
                app.save_video_draft(self.draft.path, target, overwrite=True)
        self.assertEqual(target.read_bytes(), b"original")
        self.assertEqual(self.draft.path.read_bytes(), self.video)
        self.assertFalse(list(target.parent.glob(".LumaShot-save-*")))


if __name__ == "__main__":
    unittest.main()
