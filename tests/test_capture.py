"""Run from the project folder: python -m unittest discover -s tests -v"""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import tempfile
import unittest
from unittest.mock import patch
from PySide6.QtCore import QPoint, QPointF, QRectF, Qt, QSettings
from PySide6.QtGui import QColor, QImage, QPixmap, QFontDatabase, QKeySequence
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from LumaShot import CaptureOverlay
from LumaShot import History, Mark, render_crop
from LumaShot import LANGUAGES, STRINGS, COLORS
from LumaShot import MainWindow, BASE_STYLE, Hotkeys, native_hotkey, JsonSettings

APP = QApplication.instance() or QApplication([])
if APP.platformName() == "offscreen":
    for font in ("segoeui.ttf", "segoeuib.ttf", "seguisym.ttf"):
        QFontDatabase.addApplicationFont(os.path.join(os.environ.get("WINDIR", "C:/Windows"), "Fonts", font))


class CaptureTests(unittest.TestCase):
    def test_eight_handles_resize_edges_without_changing_other_axis(self):
        from LumaShot import RecordingOverlay
        for overlay_type in (CaptureOverlay, RecordingOverlay):
            pix = QPixmap(APP.primaryScreen().size())
            pix.fill(QColor("white"))
            overlay = overlay_type(APP.primaryScreen(), pix, "ro")
            overlay.show()
            APP.processEvents()
            cases = [("t", QPoint(280, 50), QRectF(100, 50, 300, 250)),
                     ("b", QPoint(280, 350), QRectF(100, 100, 300, 250)),
                     ("l", QPoint(50, 240), QRectF(50, 100, 350, 200)),
                     ("r", QPoint(450, 240), QRectF(100, 100, 350, 200)),
                     ("l", QPoint(450, 240), QRectF(400, 100, 50, 200)),
                     ("t", QPoint(280, 350), QRectF(100, 300, 300, 50)),
                     ("r", QPoint(overlay.width()+50, 240), QRectF(100, 100, overlay.width()-100, 200))]
            for handle, end, expected in cases:
                with self.subTest(overlay=overlay_type.__name__, handle=handle, end=end):
                    overlay.selection = QRectF(100, 100, 300, 200)
                    self.assertEqual(len(overlay.handles()), 8)
                    start = overlay.handles()[handle].toPoint()
                    QTest.mouseMove(overlay, start)
                    expected_cursor = Qt.CursorShape.SizeVerCursor if handle in ("t", "b") else Qt.CursorShape.SizeHorCursor
                    self.assertEqual(overlay.cursor().shape(), expected_cursor)
                    QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=start)
                    self.assertEqual(overlay.drag_mode, handle)
                    QTest.mouseMove(overlay, end)
                    QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=end)
                    self.assertEqual(overlay.selection, expected)
            overlay.close()

    def test_compact_rails_palette_and_removed_tools(self):
        pix = QPixmap(APP.primaryScreen().size())
        pix.fill(QColor("white"))
        overlay = CaptureOverlay(APP.primaryScreen(), pix, "ro")
        overlay.show()
        for x, y in [(2, 2), (pix.width()-180, 2),
                     (2, pix.height()-180), (pix.width()-180, pix.height()-180)]:
            overlay.selection = QRectF(x, y, 170, 167)
            overlay.position_panel()
            self.assertLessEqual(overlay.panel.width(), 36)
            self.assertLessEqual(overlay.actions.height(), 36)
            self.assertTrue(overlay.rect().contains(overlay.panel.geometry()))
            self.assertTrue(overlay.rect().contains(overlay.actions.geometry()))
            self.assertFalse(overlay.panel.geometry().intersects(overlay.actions.geometry()))
            overlay.toggle_palette()
            self.assertTrue(overlay.rect().contains(overlay.palette.geometry()))
            overlay.palette.hide()
        self.assertNotIn("ellipse", overlay.tool_buttons)
        self.assertNotIn("mask", overlay.tool_buttons)
        self.assertFalse(overlay.palette.isVisible())
        from PySide6.QtWidgets import QPushButton
        self.assertEqual(len(overlay.palette.findChildren(QPushButton)), 24)
        QTest.mouseClick(overlay.color_button, Qt.MouseButton.LeftButton)
        self.assertTrue(overlay.palette.isVisible())
        QTest.mouseClick(overlay.color_buttons["#facc15"], Qt.MouseButton.LeftButton)
        self.assertEqual(overlay.color, "#facc15")
        self.assertFalse(overlay.palette.isVisible())
        before = overlay.tool
        QTest.keyClick(overlay, Qt.Key.Key_E)
        QTest.keyClick(overlay, Qt.Key.Key_M)
        self.assertEqual(overlay.tool, before)
        overlay.close()

    def test_every_language_has_every_string(self):
        keys = set(STRINGS["ro"])
        for language in LANGUAGES:
            self.assertEqual(keys, set(STRINGS[language]))
            for key in keys:
                self.assertTrue(STRINGS[language][key])
            self.assertEqual(len(STRINGS[language]["colors"]), len(COLORS))

    def test_default_move_and_enter_keeps_capture_open_but_confirms_text(self):
        pix = QPixmap(APP.primaryScreen().size())
        pix.fill(QColor("white"))
        overlay = CaptureOverlay(APP.primaryScreen(), pix, "ro")
        overlay.show()
        APP.processEvents()
        results = []
        overlay.finished.connect(lambda action, image: results.append(action))
        self.assertEqual(overlay.tool, "move")
        self.assertTrue(overlay.tool_buttons["move"].isChecked())
        self.assertFalse(overlay.tool_buttons["arrow"].isChecked())
        QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=QPoint(40, 40))
        QTest.mouseMove(overlay, QPoint(400, 300))
        QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=QPoint(400, 300))
        QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=QPoint(100, 100))
        QTest.mouseMove(overlay, QPoint(120, 110))
        QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=QPoint(120, 110))
        self.assertEqual(overlay.selection, QRectF(60, 50, 360, 260))
        self.assertFalse(overlay.history.items)
        for key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            QTest.keyClick(overlay, key)
            self.assertFalse(results)
            self.assertTrue(overlay.isVisible())
        overlay.set_tool("text")
        overlay.begin_text(QPointF(100, 100))
        overlay.editor.setText("Notă de test")
        QTest.keyClick(overlay.editor, Qt.Key.Key_Return)
        self.assertIsNone(overlay.editor)
        self.assertEqual(overlay.history.items[-1].text, "Notă de test")
        self.assertFalse(results)
        self.assertTrue(overlay.isVisible())
        QTest.keyClick(overlay, Qt.Key.Key_C, Qt.KeyboardModifier.ControlModifier)
        self.assertEqual(results, ["copy"])
        overlay.close()

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
        settings = JsonSettings(os.path.join(self.temp.name, "settings.json"), migrate=False)
        self.settings_patch = patch("LumaShot.JsonSettings", return_value=settings)
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
        APP.removeNativeEventFilter(self.window.full_hotkeys)
        APP.removeNativeEventFilter(self.window.record_hotkeys)
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

    def test_tray_left_click_starts_area_and_right_menu_has_five_actions(self):
        from PySide6.QtWidgets import QSystemTrayIcon
        with patch.object(self.window, "start_capture") as capture:
            self.window.tray_activated(QSystemTrayIcon.ActivationReason.Trigger)
            capture.assert_called_once_with()
            self.window.tray_activated(QSystemTrayIcon.ActivationReason.Context)
            self.window.tray_activated(QSystemTrayIcon.ActivationReason.DoubleClick)
            self.assertEqual(capture.call_count, 1)
        self.assertEqual(len(self.window.tray.contextMenu().actions()), 5)
        for language in LANGUAGES:
            self.window.change_language(language)
            APP.processEvents()
            with patch.object(self.window, "start_capture") as capture:
                actions = self.window.tray.contextMenu().actions()
                self.assertEqual([a.text() for a in actions], [STRINGS[language][k] for k in
                                 ("capture", "full_capture", "record", "open", "quit")])
                for action, mode in zip(actions[:3], (None, "full", "record")):
                    self.assertFalse(action.icon().isNull())
                    action.trigger()
                    if mode is None:
                        capture.assert_called_with()
                    else:
                        capture.assert_called_with(mode)
        self.window.recording = object()
        try:
            with patch.object(self.window, "stop_recording") as stop:
                self.window.rebuild_tray()
                actions = self.window.tray.contextMenu().actions()
                self.assertFalse(actions[0].isEnabled())
                self.assertFalse(actions[1].isEnabled())
                actions[2].trigger()
                stop.assert_called_once_with()
        finally:
            self.window.recording = None

    def test_frozen_settings_are_created_beside_executable(self):
        from pathlib import Path
        with patch("LumaShot.sys.frozen", True, create=True), \
             patch("LumaShot.sys.executable", str(Path(self.temp.name)/"LumaShot.exe")):
            settings = JsonSettings(migrate=False)
            self.assertEqual(settings.path, Path(self.temp.name).resolve()/"LumaShot.settings.json")
            self.assertTrue(settings.path.exists())

    def test_theme_persists_and_controls_keep_contrast_in_all_languages(self):
        for language in LANGUAGES:
            self.window.change_language(language)
            APP.processEvents()
            for theme in ("dark", "light"):
                self.window.change_theme(theme)
                APP.processEvents()
                self.assertEqual(self.window.settings.value("theme"), theme)
                self.assertEqual(self.window.tabs.count(), 4)
                self.assertEqual(self.window.theme_combo.currentData(), theme)
                self.assertEqual(self.window.icon_color, "#edf5f3" if theme == "dark" else "#193d43")
                from PySide6.QtWidgets import QLineEdit
                self.window.show()
                self.window.tabs.setCurrentIndex(2)
                APP.processEvents()
                field = self.window.quality_spin.findChild(QLineEdit)
                self.assertGreater(field.width(), 30)
                self.assertEqual(self.window.quality_spin.text(), "95 %")

    def test_full_shortcut_is_optional_independent_and_can_be_disabled(self):
        self.assertFalse(self.window.full_hotkeys.registered)
        with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=1), \
             patch("LumaShot.ctypes.windll.user32.UnregisterHotKey"):
            self.window.hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+K"))
            self.window.apply_hotkey()
            region = list(self.window.hotkeys.registered)
            self.window.full_hotkey_enabled.setChecked(True)
            self.window.full_hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+L"))
            self.window.apply_hotkey(True)
            self.assertEqual(self.window.settings.value("full_hotkey"), "Ctrl+Alt+L")
            self.assertEqual(self.window.full_hotkeys.registered[0][0], 0x5B70)
            self.assertNotEqual(region[0][0], self.window.full_hotkeys.registered[0][0])
            self.window.full_hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+K"))
            with patch("LumaShot.QMessageBox.warning") as warning:
                self.window.apply_hotkey(True)
                warning.assert_called_once()
            self.assertEqual(self.window.settings.value("full_hotkey"), "Ctrl+Alt+L")
            self.window.full_hotkey_enabled.setChecked(False)
            self.window.apply_hotkey(True)
            self.assertFalse(self.window.full_hotkeys.registered)
            self.assertFalse(self.window.option("full_hotkey_enabled"))
            self.assertEqual(self.window.hotkeys.registered, region)
            self.window.hotkeys.close()

    def test_video_shortcut_persists_and_cannot_conflict_with_either_screenshot_shortcut(self):
        with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=1), \
             patch("LumaShot.ctypes.windll.user32.UnregisterHotKey", return_value=1):
            for mode, editor, checkbox, key in (
                (False, self.window.hotkey_editor, self.window.hotkey_enabled, "Ctrl+Alt+K"),
                (True, self.window.full_hotkey_editor, self.window.full_hotkey_enabled, "Ctrl+Alt+L"),
                ("record", self.window.record_hotkey_editor, self.window.record_hotkey_enabled, "Ctrl+Alt+V")):
                checkbox.setChecked(True)
                editor.setKeySequence(QKeySequence(key))
                self.window.apply_hotkey(mode)
            self.assertEqual(self.window.settings.value("record_hotkey"), "Ctrl+Alt+V")
            self.assertEqual(self.window.record_hotkeys.registered[0][0], 0x5B80)
            with patch("LumaShot.QMessageBox.warning") as warning:
                self.window.record_hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+K"))
                self.window.apply_hotkey("record")
                self.window.record_hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+L"))
                self.window.apply_hotkey("record")
                self.window.full_hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+V"))
                self.window.apply_hotkey(True)
                self.assertEqual(warning.call_count, 3)
            self.assertEqual(self.window.settings.value("record_hotkey"), "Ctrl+Alt+V")
            self.window.record_hotkey_enabled.setChecked(False)
            self.window.apply_hotkey("record")
            self.assertFalse(self.window.record_hotkeys.registered)
            self.assertFalse(self.window.option("record_hotkey_enabled"))

    def test_video_shortcut_respects_editor_focus_and_drives_current_bar(self):
        from unittest.mock import MagicMock
        with patch.object(self.window, "start_capture") as capture:
            with patch("LumaShot.QApplication.focusWidget", return_value=self.window.record_hotkey_editor):
                self.window.hotkey_capture("record")
                capture.assert_not_called()
            with patch("LumaShot.QApplication.focusWidget", return_value=None):
                self.window.hotkey_capture("record")
                capture.assert_called_once_with("record")
                bar = MagicMock()
                self.window.record_controls = bar
                self.window.hotkey_capture("record")
                bar.primary_action.assert_called_once()
                self.window.record_controls = None

    def test_editing_either_shortcut_does_not_capture(self):
        with patch("LumaShot.QApplication.focusWidget", return_value=self.window.full_hotkey_editor), \
             patch.object(self.window, "start_capture") as capture:
            self.window.hotkey_capture()
            self.window.hotkey_capture("full")
            capture.assert_not_called()

    def test_capture_delay_guards_against_duplicate_clicks(self):
        with patch("LumaShot.QTimer.singleShot") as timer:
            self.window.start_capture("full")
            self.window.start_capture()
            timer.assert_called_once()
            self.assertEqual(self.window.capture_mode, "full")
            self.assertFalse(self.window.full_button.isEnabled())

    def fake_screen(self, name="display", x=0, scale=1):
        from PySide6.QtCore import QRect
        class Screen:
            def geometry(self):
                return QRect(x, 0, 640, 480)
            def name(self):
                return name
            def grabWindow(self, _):
                pix = QPixmap(640 * scale, 480 * scale)
                pix.fill(QColor("#1a638a"))
                pix.setDevicePixelRatio(scale)
                return pix
        return Screen()

    def test_full_capture_preselects_cursor_monitor_and_copies_native_pixels(self):
        first, second = self.fake_screen(), self.fake_screen("second", -640, 2)
        self.window.capture_mode = "full"
        with patch("LumaShot.QApplication.screenAt", return_value=second), \
             patch("LumaShot.QApplication.screens", return_value=[first, second]):
            self.window.capture_screens()
        self.assertEqual(len(self.window.overlays), 1)
        overlay = self.window.overlays[0]
        self.assertEqual(overlay.screen_key, "second")
        self.assertEqual(overlay.selection, QRectF(0, 0, 640, 480))
        overlay.complete("copy")
        self.assertEqual(APP.clipboard().image().width(), 1280)
        self.assertEqual(APP.clipboard().image().pixelColor(1279, 959).name(), "#1a638a")

    def test_remember_area_restores_region_and_does_not_leak_full_selection(self):
        screen = self.fake_screen()
        self.window.settings.setValue("remember_area", True)
        with patch("LumaShot.QApplication.screenAt", return_value=screen), \
             patch("LumaShot.QApplication.screens", return_value=[screen]):
            self.window.capture_screens()
            self.window.overlays[0].selection = QRectF(50, 40, 100, 90)
            self.window.overlays[0].complete("copy")
            self.window.capture_screens()
            self.assertEqual(self.window.overlays[0].selection, QRectF(50, 40, 100, 90))
            self.window.close_overlays()
            self.window.capture_mode = "full"
            self.window.capture_screens()
            self.window.overlays[0].complete("copy")
            self.assertEqual(self.window.settings.value("last_area")["rect"], [50, 40, 100, 90])

    def test_instant_save_uses_format_quality_and_skips_editor(self):
        from pathlib import Path
        screen = self.fake_screen()
        self.window.settings.setValue("full_action", "save")
        self.window.settings.setValue("save_format", "JPEG")
        self.window.settings.setValue("jpeg_quality", 77)
        self.window.capture_mode = "full"
        with patch("LumaShot.QApplication.screenAt", return_value=screen), \
             patch("LumaShot.QFileDialog.getSaveFileName") as dialog, \
             patch.object(QImage, "save", autospec=True, return_value=True) as save:
            self.window.capture_screens()
            self.assertEqual(save.call_args.args[-2:], ("JPEG", 77))
            dialog.assert_not_called()
        self.window.save_immediately(self.image)
        files = list(Path(self.temp.name).glob("*.jpg"))
        self.assertEqual(len(files), 1)
        self.assertEqual(QImage(str(files[0])).size(), self.image.size())
        self.assertFalse(self.window.overlays)

    def test_cursor_option_only_composites_cursor_monitor(self):
        first, second = self.fake_screen(), self.fake_screen("second", 640)
        self.window.capture_mode = "full"
        self.window.settings.setValue("include_cursor", True)
        with patch("LumaShot.QApplication.screenAt", return_value=second), \
             patch("LumaShot.QApplication.screens", return_value=[first, second]), \
             patch("LumaShot.capture_cursor", side_effect=lambda pix: pix) as cursor:
            self.window.capture_screens()
            cursor.assert_called_once()

    def test_notifications_can_be_disabled(self):
        self.window.settings.setValue("notifications", False)
        with patch.object(self.window.tray, "isVisible", return_value=True), \
             patch.object(self.window.tray, "showMessage") as notify:
            self.window.finish_capture("copy", self.image)
            notify.assert_not_called()
            self.window.settings.setValue("notifications", True)
            self.window.finish_capture("copy", self.image)
            notify.assert_called_once()

    def test_tooltips_match_language_action_and_editor_shortcuts(self):
        for language in LANGUAGES:
            self.window.change_language(language)
            APP.processEvents()
            for action, key in (("edit", "tip_full_edit"), ("save", "tip_full_save")):
                self.window.change_full_action(action)
                self.assertEqual(" ".join(self.window.full_button.toolTip().split()),
                                 " ".join(STRINGS[language][key].split()))
            self.assertEqual(self.window.tray.toolTip(), STRINGS[language]["tip_tray"])
            self.assertTrue(self.window.tray.contextMenu().toolTipsVisible())
            overlay = CaptureOverlay(self.fake_screen(), self.fake_screen().grabWindow(0), language)
            from PySide6.QtWidgets import QPushButton
            for key, shortcut in (("copy", "Ctrl+C"), ("save", "Ctrl+S"), ("cancel", "Esc")):
                button = overlay.actions.findChild(QPushButton, key)
                self.assertIn(STRINGS[language][key], button.toolTip())
                self.assertIn(shortcut, button.toolTip())
            overlay.close()

    def test_tooltip_fits_screen_and_is_hidden_before_capture(self):
        from PySide6.QtWidgets import QToolTip
        self.window.change_language("ru")
        APP.processEvents()
        self.window.show()
        for theme in ("dark", "light"):
            self.window.change_theme(theme)
            APP.processEvents()
            screen = APP.primaryScreen().availableGeometry()
            button = self.window.full_button
            QToolTip.showText(screen.bottomRight() - QPoint(2, 2), button.toolTip(), button)
            APP.processEvents()
            tips = [w for w in APP.topLevelWidgets()
                    if w.windowType() == Qt.WindowType.ToolTip and w.isVisible()]
            self.assertTrue(tips)
            self.assertTrue(screen.contains(tips[0].geometry()))
            self.assertGreater(tips[0].height(), 20)
            with patch("LumaShot.QTimer.singleShot"):
                self.window.start_capture()
            self.assertFalse(any(w.isVisible() for w in tips))
            self.window.capture_pending = False
            self.window.capture_button.setEnabled(True)
            self.window.full_button.setEnabled(True)
            self.window.show()

    def test_editor_tooltips_do_not_inherit_compact_button_height_or_swatch_color(self):
        from PySide6.QtWidgets import QToolTip, QPushButton
        for theme in ("light", "dark"):
            self.window.change_theme(theme)
            APP.processEvents()
            screen = self.fake_screen()
            overlay = CaptureOverlay(screen, screen.grabWindow(0), "ru", theme)
            overlay.selection = QRectF(40, 40, 300, 200)
            overlay.position_panel()
            overlay.show()
            APP.processEvents()
            for button in (overlay.actions.findChild(QPushButton, "copy"), overlay.color_button):
                QToolTip.showText(QPoint(300, 300), button.toolTip(), button)
                APP.processEvents()
                tips = [w for w in APP.topLevelWidgets()
                        if w.windowType() == Qt.WindowType.ToolTip and w.isVisible()]
                self.assertTrue(tips)
                self.assertGreater(tips[0].height(), 32)
                self.assertIn("#163e3b", overlay.styleSheet())
                tips[0].hide()
            overlay.close()

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

    def test_custom_shortcut_persists_and_is_registered_on_restart(self):
        with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=1), \
             patch("LumaShot.ctypes.windll.user32.UnregisterHotKey"):
            self.window.hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+K"))
            self.window.apply_hotkey()
            self.assertEqual(self.window.settings.value("capture_hotkey"), "Ctrl+Alt+K")
            self.assertIn("Ctrl+Alt+K", self.window.capture_button.toolTip())
            with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=1) as register:
                restarted = Hotkeys(lambda: None, self.window.settings.value("capture_hotkey"))
                self.assertEqual(register.call_args.args[2:], (0x4003, ord("K")))
                restarted.close()
            self.window.hotkeys.close()

    def test_conflicting_shortcut_preserves_previous_binding_and_settings(self):
        with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=1):
            self.window.hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+K"))
            self.window.apply_hotkey()
        before = list(self.window.hotkeys.registered)
        with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=0), \
             patch("LumaShot.ctypes.windll.user32.UnregisterHotKey") as unregister, \
             patch("LumaShot.QMessageBox.warning") as warning:
            self.window.hotkey_editor.setKeySequence(QKeySequence("Ctrl+Alt+L"))
            self.window.apply_hotkey()
            self.assertTrue(warning.called)
            unregister.assert_not_called()
            self.assertEqual(self.window.hotkeys.registered, before)
            self.assertEqual(self.window.settings.value("capture_hotkey"), "Ctrl+Alt+K")
            self.window.hotkeys.close()


class HotkeyTests(unittest.TestCase):
    def test_native_mapping_and_validation(self):
        self.assertEqual(native_hotkey(QKeySequence("Ctrl+Shift+F9")), (0x4006, 0x78))
        self.assertEqual(native_hotkey(QKeySequence("Print")), (0x4000, 0x2C))
        for bad in ("", "K", "Ctrl+K, Ctrl+C"):
            with self.assertRaises(ValueError):
                native_hotkey(QKeySequence(bad))

    def test_reusing_default_shortcut_does_not_register_it_twice(self):
        with patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=1) as register, \
             patch("LumaShot.ctypes.windll.user32.UnregisterHotKey") as unregister:
            controller = Hotkeys(lambda: None)
            self.assertEqual(register.call_count, 2)
            self.assertTrue(controller.replace(QKeySequence("Ctrl+Shift+F9")))
            self.assertEqual(register.call_count, 2)
            self.assertEqual(len(controller.registered), 1)
            unregister.assert_called_once_with(None, 0x5B51)
            controller.close()


if __name__ == "__main__":
    unittest.main()

