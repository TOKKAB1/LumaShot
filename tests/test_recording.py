"""Synthetic inputs only: these tests never open a microphone or record the desktop."""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from PySide6.QtCore import QRect, QRectF, QPoint, QTimer, Qt, QUrl, QSettings, QSize, QObject, Signal
from PySide6.QtGui import QColor, QImage, QPixmap
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtMultimedia import QMediaPlayer, QVideoSink, QAudioDecoder, QAudioFormat
import LumaShot as app

APP = QApplication.instance() or QApplication([])


def until(predicate, timeout=8):
    end = time.monotonic()+timeout
    while not predicate() and time.monotonic()<end:
        APP.processEvents()
        time.sleep(.003)
    return predicate()


class SyntheticGrab:
    def __init__(self, rect):
        self.rect = rect
        self.closed = False
        self.count = 0

    def frame(self, cursor=False):
        self.count += 1
        image = QImage(self.rect.size(), QImage.Format.Format_RGB32)
        image.fill(QColor.fromHsv(self.count*10%360, 180, 220))
        return image

    def close(self):
        self.closed = True


class SyntheticAudio:
    def __init__(self, kind):
        self.frequency = 440 if kind == "microphone" else 880
        self.position = 0
        self.error = None
        self.blocks = self
        self.closed = False

    def get_nowait(self):
        samples = np.arange(self.position, self.position+960)
        self.position += 960
        tone = .4*np.sin(2*np.pi*self.frequency*samples/48000)
        return np.repeat(tone[:, None], 2, axis=1).astype(np.float32)

    def close(self):
        self.closed = True


class PortableSettingsTests(unittest.TestCase):
    def test_json_creation_roundtrip_and_unicode(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"LumaShot.settings.json"
            prefs = app.JsonSettings(path, migrate=False)
            self.assertTrue(path.exists())
            prefs.setValue("folder", "C:/Capturi/Înregistrări/Видео")
            prefs.setValue("last_area", {"native_rect": [-1200, -50, 2400, 900]})
            prefs.setValue("microphone", True)
            prefs.setValue("system_audio", False)
            fresh = app.JsonSettings(path, migrate=False)
            self.assertEqual(fresh.data, prefs.data)
            self.assertTrue(fresh.value("microphone", type=bool))
            self.assertFalse(fresh.value("system_audio", type=bool))
            self.assertFalse(list(Path(folder).glob("*.tmp")))

    def test_legacy_migration_runs_only_without_json(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"settings.json"
            old = QSettings(str(Path(folder)/"legacy.ini"), QSettings.Format.IniFormat)
            old.setValue("theme", "dark")
            old.setValue("last_area", {"screen": "first", "rect": [20, 30, 200, 100]})
            old.setValue("include_cursor", True)
            with patch("LumaShot.QSettings", return_value=old) as legacy:
                prefs = app.JsonSettings(path)
                self.assertEqual(prefs.value("theme"), "dark")
                self.assertEqual(prefs.value("last_area"), old.value("last_area"))
                self.assertTrue(prefs.value("include_cursor", type=bool))
                prefs.setValue("theme", "light")
                self.assertEqual(app.JsonSettings(path).value("theme"), "light")
                legacy.assert_called_once()

    def test_damaged_json_is_preserved_and_wrong_types_are_ignored(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"settings.json"
            path.write_text("{broken", encoding="utf-8")
            prefs = app.JsonSettings(path, migrate=False)
            backup = list(Path(folder).glob("*.damaged-*"))
            self.assertEqual(len(backup), 1)
            self.assertEqual(backup[0].read_text(), "{broken")
            self.assertTrue(prefs.error)
            path.write_text(json.dumps({"microphone": "false", "jpeg_quality": []}))
            prefs = app.JsonSettings(path, migrate=False)
            self.assertFalse(prefs.value("microphone"))
            self.assertEqual(prefs.value("jpeg_quality"), 95)

    def test_failed_atomic_replace_keeps_original_and_reports_error(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/"settings.json"
            prefs = app.JsonSettings(path, migrate=False)
            original = path.read_bytes()
            errors = []
            prefs.on_error = errors.append
            with patch("LumaShot.os.replace", side_effect=PermissionError("read only")):
                prefs.setValue("theme", "dark")
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(errors, ["read only"])
            self.assertFalse(list(Path(folder).glob("*.tmp")))


class DesktopSelectionTests(unittest.TestCase):
    def test_cross_monitor_crop_keeps_native_pixels_at_negative_origin(self):
        image = QImage(1600, 600, QImage.Format.Format_RGB32)
        image.fill(QColor("red"))
        from PySide6.QtGui import QPainter
        painter = QPainter(image)
        painter.fillRect(QRect(800, 0, 800, 600), QColor("blue"))
        painter.end()
        overlay = app.CaptureOverlay(APP.primaryScreen(), QPixmap.fromImage(image), "ro")
        overlay.resize(800, 300)
        overlay.native_bounds = QRect(-800, -100, 1600, 600)
        overlay.scale = 2
        overlay.selection = QRectF(350, 50, 100, 100)
        native = app.selected_native_rect(overlay)
        self.assertEqual(native, QRect(-100, 0, 200, 200))
        cropped = app.render_crop(overlay.screen_image, overlay.selection, [], overlay.scale)
        self.assertEqual(cropped.size(), native.size())
        self.assertEqual(cropped.pixelColor(20, 50), QColor("red"))
        self.assertEqual(cropped.pixelColor(180, 50), QColor("blue"))
        overlay.close()

    def test_record_selection_can_move_and_resize_but_not_copy(self):
        pix = QPixmap(800, 600)
        pix.fill(QColor("white"))
        overlay = app.RecordingOverlay(APP.primaryScreen(), pix, "ro")
        overlay.show()
        events = []
        selections = []
        overlay.selection_ready.connect(lambda item: selections.append(QRectF(item.selection)))
        overlay.finished.connect(lambda action, _: events.append(action))
        QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=QPoint(40, 40))
        QTest.mouseMove(overlay, QPoint(400, 300))
        QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=QPoint(400, 300))
        self.assertEqual(overlay.selection, QRectF(40, 40, 360, 260))
        self.assertFalse(overlay.panel.isVisible())
        self.assertFalse(overlay.actions.isVisible())
        self.assertEqual(selections[-1], overlay.selection)
        QTest.keyClick(overlay, Qt.Key.Key_Return)
        QTest.keyClick(overlay, Qt.Key.Key_C, Qt.KeyboardModifier.ControlModifier)
        self.assertFalse(events)
        QTest.mousePress(overlay, Qt.MouseButton.LeftButton, pos=QPoint(100, 100))
        QTest.mouseMove(overlay, QPoint(120, 110))
        QTest.mouseRelease(overlay, Qt.MouseButton.LeftButton, pos=QPoint(120, 110))
        self.assertEqual(overlay.selection, QRectF(60, 50, 360, 260))
        overlay.complete("record")
        self.assertEqual(events, ["record"])
        overlay.close()

    def test_multi_monitor_flow_uses_one_surface_and_restores_native_region(self):
        with tempfile.TemporaryDirectory() as folder:
            settings = app.JsonSettings(Path(folder)/"settings.json", migrate=False)
            settings.setValue("remember_area", True)
            with patch("LumaShot.JsonSettings", return_value=settings), \
                 patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=0):
                window = app.MainWindow()
            window.tray.hide()
            window.restore_window = False
            bounds = QRect(-800, 0, 1600, 600)
            def place(overlay, rect):
                overlay.setGeometry(0, 0, 800, 300)
                overlay.native_bounds = rect
                overlay.scale = 2
            screen = APP.primaryScreen()
            try:
                with patch("LumaShot.QApplication.screens", return_value=[screen, screen]), \
                     patch("LumaShot.desktop_bounds", return_value=bounds), \
                     patch("LumaShot.DesktopGrab", SyntheticGrab), \
                     patch("LumaShot.place_desktop_overlay", side_effect=place):
                    window.capture_screens()
                    self.assertEqual(len(window.overlays), 1)
                    window.overlays[0].selection = QRectF(350, 50, 100, 100)
                    window.overlays[0].complete("copy")
                    self.assertEqual(settings.value("last_area")["native_rect"], [-100, 100, 200, 200])
                    window.capture_screens()
                    self.assertEqual(window.overlays[0].selection, QRectF(350, 50, 100, 100))
            finally:
                window.close_overlays()
                APP.removeNativeEventFilter(window.hotkeys)
                APP.removeNativeEventFilter(window.full_hotkeys)
                APP.removeNativeEventFilter(window.record_hotkeys)
                window.hide()
                window.deleteLater()
                APP.processEvents()


class RecordingBarTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        settings = app.JsonSettings(Path(self.temp.name)/"settings.json", migrate=False)
        settings.setValue("folder", self.temp.name)
        with patch("LumaShot.JsonSettings", return_value=settings), \
             patch("LumaShot.ctypes.windll.user32.RegisterHotKey", return_value=0):
            self.window = app.MainWindow()
        self.window.tray.hide()
        self.window.restore_window = False
        self.exclusion = patch("LumaShot.exclude_from_capture", return_value=True)
        self.exclusion.start()

    def tearDown(self):
        if self.window.recording:
            self.window.recording.stop()
        self.window.close_overlays()
        self.window.dismiss_recording_bar()
        for controller in (self.window.hotkeys, self.window.full_hotkeys, self.window.record_hotkeys):
            APP.removeNativeEventFilter(controller)
            controller.close()
        self.window.hide()
        self.window.deleteLater()
        APP.processEvents()
        self.exclusion.stop()
        self.temp.cleanup()

    def ready_bar(self):
        pix = QPixmap(800, 600)
        pix.fill(QColor("#118769"))
        overlay = app.RecordingOverlay(APP.primaryScreen(), pix, self.window.lang)
        overlay.native_bounds = QRect(0, 0, 800, 600)
        overlay.selection = QRectF(40, 180, 500, 250)
        overlay.selection_ready.connect(self.window.update_recording_bar)
        overlay.finished.connect(self.window.finish_capture)
        self.window.overlays = [overlay]
        self.window.capture_mode = "record"
        overlay.show()
        overlay.position_panel()
        return overlay, self.window.record_controls

    def test_ready_bar_is_one_row_audio_settings_persist_and_close_cancels(self):
        overlay, bar = self.ready_bar()
        self.assertLessEqual(bar.height(), 50)
        self.assertGreaterEqual(bar.start_button.width(), 90)
        self.assertEqual(bar.duration.text(), "00:00:00")
        self.assertEqual(bar.start_button.text(), self.window.t("bar_start"))
        self.assertFalse(overlay.actions.isVisible())
        self.assertTrue(bar.safe_to_record())
        QTest.mouseClick(bar.checks["microphone"], Qt.MouseButton.LeftButton)
        self.assertTrue(self.window.option("microphone"))
        self.assertIn(self.window.t("audio_on"), bar.checks["microphone"].toolTip())
        self.assertIsNone(self.window.recording)
        QTest.mouseClick(bar.close_button, Qt.MouseButton.LeftButton)
        self.assertFalse(self.window.overlays)
        self.assertIsNone(self.window.record_controls)
        self.assertFalse(list(Path(self.temp.name).glob("*.mp4")))

    def test_same_bar_survives_start_and_stop_finalizes_mp4(self):
        overlay, bar = self.ready_bar()
        original = app.VideoRecording
        def create(rect, path, cursor, parent):
            return original(rect, path, cursor, parent, grab_factory=SyntheticGrab)
        with patch("LumaShot.QTimer.singleShot") as timer, \
             patch("LumaShot.VideoRecording", side_effect=create), \
             patch("LumaShot.QMessageBox.warning") as warning:
            before = bar.pos()
            QTest.mouseClick(bar.start_button, Qt.MouseButton.LeftButton)
            self.assertFalse(self.window.overlays)
            self.assertIs(self.window.record_controls, bar)
            self.assertFalse(bar.start_button.isEnabled())
            callback = timer.call_args.args[1]
            callback()  # delayed creation, without recording real pixels
            self.assertIs(self.window.record_controls, bar)
            self.assertEqual(before, bar.pos())
            timer.call_args.args[1]()  # delayed encoder start
            self.assertTrue(until(lambda: self.window.recording.active))
            self.assertEqual(bar.start_button.text(), self.window.t("bar_stop"))
            self.assertTrue(bar.start_button.isEnabled())
            QTest.qWait(220)
            self.assertIsNotNone(bar.boundary)
            self.assertEqual(len(bar.boundary.strips), 4)
            QTest.mouseClick(bar.pause_button, Qt.MouseButton.LeftButton)
            self.assertTrue(self.window.recording.paused)
            self.assertEqual(bar.pause_button.accessibleName(), self.window.t("record_resume"))
            before_pause = self.window.recording.elapsed()
            QTest.qWait(150)
            self.assertEqual(self.window.recording.elapsed(), before_pause)
            QTest.mouseClick(bar.pause_button, Qt.MouseButton.LeftButton)
            self.assertFalse(self.window.recording.paused)
            QTest.qWait(100)
            boundary = bar.boundary
            QTest.mouseClick(bar.start_button, Qt.MouseButton.LeftButton)
            self.assertTrue(until(lambda: self.window.recording is None))
            self.assertIsNone(self.window.record_controls)
            self.assertFalse(boundary.strips)
            self.assertIsNotNone(self.window.review_dialog)
            self.assertTrue(self.window.recording_draft.path.exists())
            self.assertFalse(list(Path(self.temp.name).glob("*.mp4")))
            self.window.review_dialog.save_default()
            self.assertTrue(until(lambda: self.window.review_dialog is None))
            self.assertEqual(len(list(Path(self.temp.name).glob("*.mp4"))), 1)
            warning.assert_not_called()

    def test_exclusion_failure_blocks_start_when_bar_overlaps_recorded_area(self):
        bar = app.RecordingControls(self.window, rect=QRect(0, 0, 800, 600))
        self.window.record_controls = bar
        events = []
        bar.start_requested.connect(lambda: events.append(True))
        with patch("LumaShot.exclude_from_capture", return_value=False):
            bar.set_region(bar.region)
            self.assertFalse(bar.safe_to_record())
            QTest.mouseClick(bar.start_button, Qt.MouseButton.LeftButton)
            self.assertFalse(events)
            self.assertTrue(bar.error_label.isVisible())
            self.assertIn(self.window.t("record_hide_blocked"), bar.error_label.accessibleName())

    def test_bar_positions_above_selection_and_clamps_to_negative_monitor(self):
        work = QRect(-1920, 0, 1920, 1040)
        size = QSize(310, 44)
        position = app.recording_bar_position(QRect(-1800, 200, 800, 600), size, work)
        self.assertEqual(position.y(), 148)
        self.assertTrue(work.contains(QRect(position, size)))
        position = app.recording_bar_position(QRect(-1920, 0, 3840, 1080), size, work)
        self.assertTrue(work.contains(QRect(position, size)))

    def test_bar_labels_and_icons_are_accessible_in_each_language(self):
        for language in app.LANGUAGES:
            self.window.change_language(language)
            for theme in ("light", "dark"):
                self.window.change_theme(theme)
                bar = app.RecordingControls(self.window)
                bar.show()
                APP.processEvents()
                self.assertLessEqual(bar.height(), 50)
                self.assertFalse(bar.start_button.icon().isNull())
                self.assertFalse(bar.pause_button.icon().isNull())
                bar.on_paused(True)
                self.assertEqual(bar.pause_button.accessibleName(), self.window.t("record_resume"))
                self.assertIn(self.window.t("record_resume_tip"), bar.pause_button.toolTip())
                for key, button in bar.checks.items():
                    self.assertIn(self.window.t(key), button.accessibleName())
                    self.assertIn(self.window.t("audio_off"), button.toolTip())
                    self.assertFalse(button.icon().isNull())
                bar.dispose()
                bar.deleteLater()

    def test_boundary_fallback_is_outside_crop_and_does_not_accept_input(self):
        region = QRect(-800, -50, 640, 360)
        boundary = app.RecordingBoundary(region)
        try:
            with patch("LumaShot.exclude_from_capture", return_value=False):
                boundary.show()
                for strip in boundary.strips:
                    self.assertFalse(region.intersects(strip.geometry()))
                    self.assertTrue(strip.windowFlags() & Qt.WindowType.WindowTransparentForInput)
                    self.assertTrue(strip.windowFlags() & Qt.WindowType.WindowDoesNotAcceptFocus)
            with patch("LumaShot.exclude_from_capture", return_value=True):
                boundary.show()
                for strip in boundary.strips:
                    self.assertTrue(region.contains(strip.geometry()))
            before = boundary.strips[0].styleSheet()
            boundary.set_paused(True)
            self.assertNotEqual(before, boundary.strips[0].styleSheet())
        finally:
            boundary.close()


class RecordingTests(unittest.TestCase):
    def test_pause_excludes_time_and_frames_and_releases_audio(self):
        with tempfile.TemporaryDirectory() as folder, patch("LumaShot.AudioSource", SyntheticAudio):
            path = Path(folder)/"pause.mp4"
            rec = app.VideoRecording(QRect(0, 0, 320, 240), path, grab_factory=SyntheticGrab)
            rec.set_audio("system_audio", True)
            results = []
            rec.finished.connect(lambda path, error: results.append(error))
            rec.start()
            self.assertTrue(until(lambda: rec.active))
            QTest.qWait(450)
            source = rec.sources["system_audio"]
            rec.set_paused(True)
            paused_time, count = rec.elapsed(), rec.grabber.count
            self.assertTrue(source.closed)
            QTest.qWait(500)
            self.assertEqual(rec.elapsed(), paused_time)
            self.assertEqual(rec.grabber.count, count)
            rec.set_paused(False)
            self.assertIsNot(rec.sources["system_audio"], source)
            QTest.qWait(450)
            rec.set_paused(True)
            rec.stop()  # Stopping from pause must still finalize one playable file.
            self.assertTrue(until(lambda: bool(results)))
            self.assertEqual(results, [""])
            player = QMediaPlayer()
            player.setSource(QUrl.fromLocalFile(str(path)))
            self.assertTrue(until(lambda: player.duration() > 0))
            self.assertTrue(750 < player.duration() < 1150, player.duration())
            player.setSource(QUrl())
            rec.deleteLater()
            APP.processEvents()

    def test_stereo_quality_with_bursty_audio_delivery(self):
        import queue
        class BurstyStereo:
            def __init__(self, kind):
                self.blocks, self.error = queue.Queue(), None
                self.position = 0
                self.started_at = time.monotonic()
                self.timer = QTimer()
                self.timer.timeout.connect(self.deliver)
                self.timer.start(80)
            def deliver(self):
                # Four 20-ms chunks arrive together, like a shared WASAPI buffer.
                due = int((time.monotonic()-self.started_at)*50)*960
                while self.position < due:
                    t = np.arange(self.position, self.position+960)/48000
                    left = .2*np.sin(2*np.pi*440*t)+.15*np.sin(2*np.pi*12000*t)
                    right = .3*np.sin(2*np.pi*1800*t)
                    self.blocks.put(np.stack([left, right], axis=1).astype(np.float32))
                    self.position += 960
            def close(self):
                self.timer.stop()
                self.deliver()
        with tempfile.TemporaryDirectory() as folder, patch("LumaShot.AudioSource", BurstyStereo):
            path = Path(folder)/"stereo.mp4"
            rec = app.VideoRecording(QRect(0, 0, 320, 240), path, grab_factory=SyntheticGrab)
            rec.set_audio("system_audio", True)
            results = []
            rec.finished.connect(lambda path, error: results.append(error))
            rec.start()
            QTimer.singleShot(1600, rec.stop)
            self.assertTrue(until(lambda: bool(results)))
            self.assertEqual(results, [""])
            decoder = QAudioDecoder()
            fmt = QAudioFormat()
            fmt.setSampleRate(48000)
            fmt.setChannelCount(2)
            fmt.setSampleFormat(QAudioFormat.SampleFormat.Float)
            decoder.setAudioFormat(fmt)
            buffers, done = [], []
            decoder.bufferReady.connect(lambda: buffers.append(bytes(decoder.read().constData())))
            decoder.finished.connect(lambda: done.append(True))
            decoder.setSource(QUrl.fromLocalFile(str(path)))
            decoder.start()
            self.assertTrue(until(lambda: bool(done)), decoder.errorString())
            audio = np.frombuffer(b"".join(buffers), np.float32).reshape(-1, 2)
            decoder.stop()
            decoder.setSource(QUrl())
            rec.deleteLater()
            APP.processEvents()
            sample = audio[24000:60000]
            def tone(channel, frequency):
                return abs(np.dot(sample[:, channel], np.exp(-2j*np.pi*frequency*np.arange(len(sample))/48000)))/len(sample)
            self.assertGreater(tone(0, 440), .075)
            self.assertGreater(tone(0, 12000), .045)  # Music's high frequencies survive AAC.
            self.assertGreater(tone(1, 1800), .11)
            self.assertLess(tone(1, 440), .008)  # Stereo channels stay independent.
            for start in range(24000, 59000, 960):
                self.assertGreater(float(np.sqrt(np.mean(audio[start:start+960]**2))), .12)

    def test_mixer_silence_headroom_and_clipping(self):
        self.assertFalse(any(app.mix_audio([])))
        loud = np.full((960, 2), 2, np.float32)
        pcm = np.frombuffer(app.mix_audio([loud, loud]), dtype="<i2")
        self.assertTrue(np.all(pcm == 32767))
        first, second = np.full((960, 2), .2, np.float32), np.full((960, 2), .6, np.float32)
        self.assertAlmostEqual(float(np.frombuffer(app.mix_audio([first, second]), dtype="<i2").mean())/32767, .4, places=4)

    def test_audio_toggles_release_sources_independently(self):
        with tempfile.TemporaryDirectory() as folder, patch("LumaShot.AudioSource", SyntheticAudio):
            rec = app.VideoRecording(QRect(0, 0, 64, 64), Path(folder)/"a.mp4", grab_factory=SyntheticGrab)
            self.assertFalse(rec.sources)
            rec.active = True
            rec.set_audio("microphone", True)
            mic = rec.sources["microphone"]
            rec.set_audio("system_audio", True)
            system = rec.sources["system_audio"]
            rec.pending_audio = object()
            rec.set_audio("microphone", False)
            self.assertTrue(mic.closed)
            self.assertFalse(system.closed)
            self.assertIsNone(rec.pending_audio)
            rec.stop()
            self.assertTrue(system.closed)
            rec.deleteLater()
            APP.processEvents()

    def test_audio_devices_stay_closed_until_encoder_starts(self):
        with tempfile.TemporaryDirectory() as folder, patch("LumaShot.AudioSource") as audio:
            rec = app.VideoRecording(QRect(0, 0, 64, 64), Path(folder)/"a.mp4", grab_factory=SyntheticGrab)
            rec.set_audio("microphone", True)
            rec.set_audio("system_audio", True)
            audio.assert_not_called()
            rec.stop()
            audio.assert_not_called()
            rec.deleteLater()
            APP.processEvents()

    def test_stop_before_start_does_not_restart_or_save_empty_video_as_success(self):
        with tempfile.TemporaryDirectory() as folder:
            rec = app.VideoRecording(QRect(0, 0, 64, 64), Path(folder)/"a.mp4", grab_factory=SyntheticGrab)
            results = []
            rec.finished.connect(lambda path, error: results.append(error))
            rec.stop()
            rec.start()
            rec.stop()
            self.assertEqual(len(results), 1)
            self.assertTrue(results[0])
            self.assertTrue(rec.grabber.closed)
            self.assertFalse(rec.timer.isActive())
            rec.deleteLater()
            APP.processEvents()

    def test_mp4_roundtrip_and_independent_audio_toggle_timeline(self):
        with tempfile.TemporaryDirectory() as folder, patch("LumaShot.AudioSource", SyntheticAudio):
            path = Path(folder)/"synthetic.mp4"
            rec = app.VideoRecording(QRect(-80, 10, 321, 241), path, grab_factory=SyntheticGrab)
            results = []
            rec.finished.connect(lambda path, error: results.append(error))
            rec.start()
            QTimer.singleShot(300, lambda: rec.set_audio("microphone", True))
            QTimer.singleShot(800, lambda: rec.set_audio("system_audio", True))
            QTimer.singleShot(1300, lambda: rec.set_audio("microphone", False))
            QTimer.singleShot(1800, lambda: rec.set_audio("system_audio", False))
            QTimer.singleShot(2250, rec.stop)
            self.assertTrue(until(lambda: bool(results)))
            self.assertEqual(results, [""])
            self.assertTrue(rec.grabber.closed)

            player, sink = QMediaPlayer(), QVideoSink()
            frames = []
            player.setVideoSink(sink)
            sink.videoFrameChanged.connect(lambda f: frames.append(f.toImage()) if f.isValid() else None)
            player.setSource(QUrl.fromLocalFile(str(path)))
            player.play()
            self.assertTrue(until(lambda: bool(frames) and player.duration()>0))
            self.assertEqual((frames[0].width(), frames[0].height()), (322, 242))
            self.assertTrue(player.hasVideo() and player.hasAudio())
            self.assertTrue(1900 < player.duration() < 2900, player.duration())
            player.stop()
            player.setSource(QUrl())

            decoder = QAudioDecoder()
            fmt = QAudioFormat()
            fmt.setSampleRate(48000)
            fmt.setChannelCount(2)
            fmt.setSampleFormat(QAudioFormat.SampleFormat.Float)
            decoder.setAudioFormat(fmt)
            buffers, done = [], []
            decoder.bufferReady.connect(lambda: buffers.append(bytes(decoder.read().constData())))
            decoder.finished.connect(lambda: done.append(True))
            decoder.setSource(QUrl.fromLocalFile(str(path)))
            decoder.start()
            self.assertTrue(until(lambda: bool(done)), decoder.errorString())
            audio = np.frombuffer(b"".join(buffers), np.float32).reshape(-1, 2)[:, 0]
            def energy(start, end, frequency=None):
                block = audio[int(start*48000):int(end*48000)]
                if frequency is None:
                    return float(np.sqrt(np.mean(block**2)))
                basis = np.exp(-2j*np.pi*frequency*np.arange(len(block))/48000)
                return abs(np.dot(block, basis))/len(block)
            self.assertLess(energy(.08, .2), .005)
            self.assertGreater(energy(.45, .65, 440), .05)
            self.assertGreater(energy(.95, 1.15, 440), .025)
            self.assertGreater(energy(.95, 1.15, 880), .025)
            self.assertLess(energy(1.5, 1.65, 440), .01)
            self.assertGreater(energy(1.5, 1.65, 880), .05)
            self.assertLess(energy(2, 2.15), .005)
            decoder.stop()
            decoder.setSource(QUrl())
            rec.deleteLater()
            APP.processEvents()


if __name__ == "__main__":
    unittest.main()
