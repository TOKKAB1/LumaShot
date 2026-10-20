# LumaShot 0.1 — Python + PySide6. Run: python LumaShot.py
"""All user-visible copy, shared by the dashboard, tray and capture editor."""

LANGUAGES = {"ro": "Română", "ru": "Русский", "en": "English"}
STRINGS = {
    "ro": {
        "tagline": "O captură. Exact cum o vrei.",
        "intro": "Selectează, adnotează și copiază — fără să pierzi ritmul.",
        "capture": "Captură nouă", "ready": "Pregătit pentru captură",
        "language": "Limba interfeței", "folder": "Dosarul pentru capturi",
        "browse": "Alege…", "settings": "Preferințe", "workflow": "Trei pași. Atât.",
        "step1": "01  Selectează", "step1body": "Trasează zona dorită pe ecran.",
        "step2": "02  Explică", "step2body": "Săgeți, text și pași numerotați.",
        "step3": "03  Păstrează", "step3body": "Copiază sau salvează imaginea.",
        "local": "Local, fără cont • PNG și JPEG",
        "trayhint": "Închiderea ferestrei păstrează aplicația lângă ceas.",
        "open": "Deschide LumaShot", "quit": "Ieșire",
        "select": "Selectează o zonă • Esc pentru anulare",
        "edit_hint": "Ctrl+C copiază • Ctrl+S salvează • Esc anulează",
        "move": "Mută / redimensionează selecția (V)",
        "pen": "Creion (P)", "line": "Linie (L)", "arrow": "Săgeată (A)",
        "rect": "Dreptunghi (R)", "ellipse": "Elipsă (E)",
        "text": "Text (T)", "highlight": "Evidențiere (H)",
        "mask": "Mascare opacă (M)", "number": "Pas numerotat (N)",
        "undo": "Anulează (Ctrl+Z)", "redo": "Refă (Ctrl+Y)",
        "copy": "Copiază", "save": "Salvează", "cancel": "Anulează",
        "color": "Culoare", "width": "Grosime", "text_prompt": "Scrie textul și apasă Enter",
        "saved": "Captură salvată: {path}", "copied": "Captura a fost copiată.",
        "error": "Nu s-a putut finaliza", "save_error": "Imaginea nu a putut fi salvată. Alege un dosar în care ai drept de scriere.",
        "capture_error": "Nu am putut captura ecranul. Încearcă din nou.",
        "hotkeys": "Scurtături globale", "no_hotkey": "Scurtăturile sunt ocupate. Folosește butonul «Captură nouă».",
        "print_busy": "Print Screen este ocupată; folosește {key}.",
        "screen_note": "Poți selecta o zonă de pe oricare monitor, câte un monitor per captură.",
        "capture_busy": "Captură în curs…", "cancelled": "Captură anulată",
        "choose_folder": "Alege dosarul pentru capturi", "save_title": "Salvează captura",
        "format": "Imagine PNG (*.png);;Imagine JPEG (*.jpg *.jpeg)",
        "version": "VERSIUNEA 0.1 • PERSONAL",
        "colors": ["Mov", "Roșu", "Galben", "Verde", "Alb", "Negru"],
    },
    "ru": {
        "tagline": "Снимок. Именно такой, как нужно.",
        "intro": "Выделяйте, добавляйте пометки и копируйте без лишних шагов.",
        "capture": "Новый снимок", "ready": "Всё готово к снимку",
        "language": "Язык интерфейса", "folder": "Папка для снимков",
        "browse": "Выбрать…", "settings": "Настройки", "workflow": "Всего три шага.",
        "step1": "01  Выделите", "step1body": "Выберите нужную область экрана.",
        "step2": "02  Объясните", "step2body": "Стрелки, текст и нумерация шагов.",
        "step3": "03  Сохраните", "step3body": "Скопируйте или сохраните снимок.",
        "local": "Локально, без аккаунта • PNG и JPEG",
        "trayhint": "После закрытия окна приложение остаётся в области уведомлений.",
        "open": "Открыть LumaShot", "quit": "Выход",
        "select": "Выделите область • Esc для отмены",
        "edit_hint": "Ctrl+C — копировать • Ctrl+S — сохранить • Esc — отмена",
        "move": "Переместить / изменить область (V)",
        "pen": "Карандаш (P)", "line": "Линия (L)", "arrow": "Стрелка (A)",
        "rect": "Прямоугольник (R)", "ellipse": "Эллипс (E)",
        "text": "Текст (T)", "highlight": "Выделение цветом (H)",
        "mask": "Скрыть область (M)", "number": "Номер шага (N)",
        "undo": "Отменить (Ctrl+Z)", "redo": "Повторить (Ctrl+Y)",
        "copy": "Копировать", "save": "Сохранить", "cancel": "Отмена",
        "color": "Цвет", "width": "Толщина", "text_prompt": "Введите текст и нажмите Enter",
        "saved": "Снимок сохранён: {path}", "copied": "Снимок скопирован.",
        "error": "Не удалось завершить", "save_error": "Не удалось сохранить изображение. Выберите папку с правом записи.",
        "capture_error": "Не удалось сделать снимок экрана. Попробуйте ещё раз.",
        "hotkeys": "Глобальные сочетания", "no_hotkey": "Сочетания заняты. Используйте кнопку «Новый снимок».",
        "print_busy": "Print Screen занята; используйте {key}.",
        "screen_note": "Можно выбрать область на любом мониторе, по одному монитору за снимок.",
        "capture_busy": "Создание снимка…", "cancelled": "Снимок отменён",
        "choose_folder": "Выберите папку для снимков", "save_title": "Сохранить снимок",
        "format": "Изображение PNG (*.png);;Изображение JPEG (*.jpg *.jpeg)",
        "version": "ВЕРСИЯ 0.1 • ДЛЯ СЕБЯ",
        "colors": ["Фиолетовый", "Красный", "Жёлтый", "Зелёный", "Белый", "Чёрный"],
    },
    "en": {
        "tagline": "A screenshot. Just how you need it.",
        "intro": "Select, annotate and copy — without breaking your flow.",
        "capture": "New capture", "ready": "Ready to capture",
        "language": "Interface language", "folder": "Screenshot folder",
        "browse": "Choose…", "settings": "Preferences", "workflow": "Three steps. That's it.",
        "step1": "01  Select", "step1body": "Drag over the area you need.",
        "step2": "02  Explain", "step2body": "Arrows, text and numbered steps.",
        "step3": "03  Keep", "step3body": "Copy or save your screenshot.",
        "local": "Local, no account • PNG and JPEG",
        "trayhint": "Closing this window keeps the app in the system tray.",
        "open": "Open LumaShot", "quit": "Quit",
        "select": "Select an area • Esc to cancel",
        "edit_hint": "Ctrl+C to copy • Ctrl+S to save • Esc to cancel",
        "move": "Move / resize selection (V)",
        "pen": "Pen (P)", "line": "Line (L)", "arrow": "Arrow (A)",
        "rect": "Rectangle (R)", "ellipse": "Ellipse (E)",
        "text": "Text (T)", "highlight": "Highlight (H)",
        "mask": "Opaque redaction (M)", "number": "Numbered step (N)",
        "undo": "Undo (Ctrl+Z)", "redo": "Redo (Ctrl+Y)",
        "copy": "Copy", "save": "Save", "cancel": "Cancel",
        "color": "Color", "width": "Width", "text_prompt": "Type text and press Enter",
        "saved": "Screenshot saved: {path}", "copied": "Screenshot copied.",
        "error": "Couldn't finish", "save_error": "Couldn't save the image. Choose a folder you can write to.",
        "capture_error": "Couldn't capture the screen. Please try again.",
        "hotkeys": "Global shortcuts", "no_hotkey": "Shortcuts are in use. Use the New capture button.",
        "print_busy": "Print Screen is in use; use {key}.",
        "screen_note": "Select an area on any monitor, one monitor per capture.",
        "capture_busy": "Capturing…", "cancelled": "Capture cancelled",
        "choose_folder": "Choose screenshot folder", "save_title": "Save screenshot",
        "format": "PNG image (*.png);;JPEG image (*.jpg *.jpeg)",
        "version": "VERSION 0.1 • PERSONAL",
        "colors": ["Purple", "Red", "Yellow", "Green", "White", "Black"],
    },
}


def tr(language, key, **values):
    text = STRINGS.get(language, STRINGS["ro"])[key]
    return text.format(**values) if values else text


"""Vector annotations rendered identically on screen and in the exported bitmap."""
from dataclasses import dataclass, field
import math
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QImage, QPainter, QPainterPath, QPen, QPolygonF


@dataclass
class Mark:
    kind: str
    start: QPointF
    end: QPointF
    color: str = "#a78bfa"
    width: int = 3
    text: str = ""
    points: list = field(default_factory=list)


class History:
    def __init__(self):
        self.items = []
        self.future = []

    def add(self, mark):
        self.items.append(mark)
        self.future.clear()

    def undo(self):
        if self.items:
            self.future.append(self.items.pop())

    def redo(self):
        if self.future:
            self.items.append(self.future.pop())


def paint_mark(painter, mark):
    painter.save()
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    color = QColor(mark.color)
    painter.setPen(QPen(color, mark.width, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
    painter.setBrush(Qt.BrushStyle.NoBrush)
    rect = QRectF(mark.start, mark.end).normalized()
    if mark.kind == "pen":
        path = QPainterPath(mark.start)
        for pt in mark.points:
            path.lineTo(pt)
        if not mark.points:
            painter.drawPoint(mark.start)
        else:
            painter.drawPath(path)
    elif mark.kind in ("line", "arrow"):
        painter.drawLine(mark.start, mark.end)
        if mark.kind == "arrow":
            angle = math.atan2(mark.end.y() - mark.start.y(), mark.end.x() - mark.start.x())
            size = max(12, mark.width * 4)
            for offset in (-0.48, 0.48):
                tip = mark.end - QPointF(math.cos(angle + offset) * size,
                                         math.sin(angle + offset) * size)
                painter.drawLine(mark.end, tip)
    elif mark.kind == "rect":
        painter.drawRect(rect)
    elif mark.kind == "ellipse":
        painter.drawEllipse(rect)
    elif mark.kind == "highlight":
        color.setAlpha(85)
        painter.fillRect(rect, color)
    elif mark.kind == "mask":
        # Solid, fully opaque pixels; no source image is included in the export.
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        painter.fillRect(rect.toAlignedRect(), QColor("#111118"))
    elif mark.kind == "text":
        font = QFont("Segoe UI")
        font.setPixelSize(16 + mark.width * 2)
        painter.setFont(font)
        painter.drawText(mark.start, mark.text)
    elif mark.kind == "number":
        radius = 13 + mark.width
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(mark.start, radius, radius)
        painter.setPen(QColor("#ffffff") if color.lightness() < 180 else QColor("#111118"))
        font = QFont("Segoe UI", weight=QFont.Weight.Bold)
        font.setPixelSize(16)
        painter.setFont(font)
        painter.drawText(QRectF(mark.start.x()-radius, mark.start.y()-radius,
                                radius*2, radius*2), Qt.AlignmentFlag.AlignCenter, mark.text)
    painter.restore()


def render_crop(source, selection, marks, scale):
    """Selection and marks use logical coordinates; source keeps physical pixels."""
    left = max(0, round(selection.left() * scale))
    top = max(0, round(selection.top() * scale))
    right = min(source.width(), round((selection.left() + selection.width()) * scale))
    bottom = min(source.height(), round((selection.top() + selection.height()) * scale))
    result = source.copy(left, top, right-left, bottom-top)
    result.setDevicePixelRatio(1)
    painter = QPainter(result)
    painter.translate(-left, -top)
    painter.scale(scale, scale)
    for mark in marks:
        paint_mark(painter, mark)
    painter.end()
    return result


from PySide6.QtCore import QPoint, QPointF, QRect, QRectF, Qt, Signal
from PySide6.QtGui import QColor, QFont, QPainter, QPen, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QSpinBox, QWidget,
)

TOOLS = [
    ("move", "↔", "V"), ("pen", "✎", "P"), ("line", "╱", "L"),
    ("arrow", "↗", "A"), ("rect", "□", "R"), ("ellipse", "○", "E"),
    ("text", "T", "T"), ("highlight", "▰", "H"), ("mask", "■", "M"),
    ("number", "①", "N"),
]
COLORS = ["#a78bfa", "#ef4444", "#facc15", "#22c55e", "#ffffff", "#111118"]
PANEL_STYLE = """
QFrame#tools { background: #20212e; border: 1px solid #48465e; border-radius: 10px; }
QPushButton { color: #f0eef9; background: transparent; border: none;
              border-radius: 5px; padding: 5px 8px; min-height: 24px; }
QPushButton:hover { background: #393749; }
QPushButton:checked { background: #7652cc; }
QPushButton#copy { background: #7954d5; font-weight: 600; }
QLabel { color: #bdb9d0; border: none; }
QSpinBox { background: #30303e; color: white; border: 1px solid #4c485f;
           border-radius: 4px; min-height: 26px; }
QLineEdit { color: white; background: #252534; border: 2px solid #a78bfa;
            border-radius: 5px; padding: 7px; }
"""


class CaptureOverlay(QWidget):
    chosen = Signal(object)
    finished = Signal(str, object)

    def __init__(self, screen, screenshot, language):
        super().__init__(None, Qt.WindowType.FramelessWindowHint |
                         Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setWindowTitle("LumaShot — Capture")
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setGeometry(screen.geometry())
        self.screen_image = screenshot.toImage()
        self.scale = screenshot.devicePixelRatio()
        self.screen_image.setDevicePixelRatio(1)
        self.lang = language
        self.selection = QRectF()
        self.origin = QPointF()
        self.drag_mode = None
        self.active_mark = None
        self.history = History()
        self.tool = "arrow"
        self.color = COLORS[1]
        self.stroke = 3
        self.editor = None
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.CrossCursor)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setStyleSheet(PANEL_STYLE)
        self.panel = self.make_panel()
        self.panel.hide()

    def t(self, key, **values):
        return tr(self.lang, key, **values)

    def make_panel(self):
        frame = QFrame(self)
        frame.setObjectName("tools")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(8, 7, 8, 7)
        layout.setSpacing(5)
        tools = QHBoxLayout()
        tools.setSpacing(2)
        self.tool_buttons = {}
        for key, glyph, shortcut in TOOLS:
            button = QPushButton(glyph)
            button.setFixedSize(35, 34)
            button.setFont(QFont("Segoe UI Symbol", 15))
            button.setToolTip(self.t(key))
            button.setAccessibleName(self.t(key))
            button.setCheckable(True)
            button.setChecked(key == self.tool)
            button.clicked.connect(lambda checked=False, k=key: self.set_tool(k))
            tools.addWidget(button)
            self.tool_buttons[key] = button
        for glyph, key, callback in [("↶", "undo", self.undo), ("↷", "redo", self.redo)]:
            button = QPushButton(glyph)
            button.setFixedSize(34, 34)
            button.setToolTip(self.t(key))
            button.setAccessibleName(self.t(key))
            button.clicked.connect(callback)
            tools.addWidget(button)
        layout.addLayout(tools)
        bottom = QHBoxLayout()
        bottom.setSpacing(5)
        self.color_buttons = {}
        for index, color in enumerate(COLORS):
            button = QPushButton()
            button.setFixedSize(22, 22)
            button.setToolTip(self.t("colors")[index])
            button.setAccessibleName(self.t("colors")[index])
            button.clicked.connect(lambda checked=False, c=color: self.set_color(c))
            bottom.addWidget(button)
            self.color_buttons[color] = button
        self.set_color(self.color)
        width = QSpinBox()
        width.setRange(1, 12)
        width.setValue(self.stroke)
        width.setFixedWidth(48)
        width.setToolTip(self.t("width"))
        width.setAccessibleName(self.t("width"))
        width.valueChanged.connect(self.set_stroke)
        bottom.addWidget(width)
        bottom.addStretch()
        for key in ("copy", "save", "cancel"):
            button = QPushButton(self.t(key))
            button.setObjectName(key)
            button.clicked.connect(lambda checked=False, k=key: self.complete(k))
            bottom.addWidget(button)
        layout.addLayout(bottom)
        frame.adjustSize()
        return frame

    def set_color(self, color):
        self.color = color
        for c, button in self.color_buttons.items():
            border = "#ffffff" if c == color else "#5b5868"
            button.setStyleSheet(
                f"background:{c}; border:2px solid {border}; border-radius:11px; padding:0;")

    def set_stroke(self, value):
        self.stroke = value

    def set_tool(self, tool):
        self.commit_text()
        self.tool = tool
        for key, button in self.tool_buttons.items():
            button.setChecked(key == tool)
        self.setFocus()
        self.update()

    def undo(self):
        self.commit_text()
        self.history.undo()
        self.update()

    def redo(self):
        self.history.redo()
        self.update()

    def position_panel(self):
        self.panel.adjustSize()
        width, height = self.panel.width(), self.panel.height()
        x = max(6, min(int(self.selection.right())-width, self.width()-width-6))
        y = int(self.selection.bottom())+10
        if y+height > self.height()-6:
            y = int(self.selection.top())-height-10
        if y < 6:
            y = max(6, self.height()-height-6)
        self.panel.move(x, y)
        self.panel.show()

    def paintEvent(self, event):
        p = QPainter(self)
        p.drawImage(QRectF(self.rect()), self.screen_image)
        p.fillRect(self.rect(), QColor(8, 8, 17, 145))
        if not self.selection.isEmpty():
            p.save()
            p.setClipRect(self.selection)
            p.drawImage(QRectF(self.rect()), self.screen_image)
            for mark in self.history.items:
                paint_mark(p, mark)
            if self.active_mark:
                paint_mark(p, self.active_mark)
            p.restore()
            p.setPen(QPen(QColor("#c2a7ff"), 1, Qt.PenStyle.DashLine))
            p.setBrush(Qt.BrushStyle.NoBrush)
            p.drawRect(self.selection)
            if self.tool == "move" or not self.history.items:
                p.setBrush(QColor("#ffffff"))
                p.setPen(QColor("#7954d5"))
                for pt in self.handles().values():
                    p.drawRect(QRectF(pt.x()-3, pt.y()-3, 6, 6))
            label = f"{round(self.selection.width()*self.scale)} × {round(self.selection.height()*self.scale)} px"
            p.setFont(QFont("Segoe UI", 10))
            box = QRectF(self.selection.left(), max(5, self.selection.top()-30), 155, 25)
            p.fillRect(box, QColor("#20212e"))
            p.setPen(QColor("#ffffff"))
            p.drawText(box, Qt.AlignmentFlag.AlignCenter, label)
        else:
            p.setPen(QColor("#ffffff"))
            p.setFont(QFont("Segoe UI", 16))
            p.drawText(self.rect().adjusted(20, 30, -20, -30),
                       Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
                       self.t("select"))
        p.end()

    def handles(self):
        r = self.selection
        return {"tl": r.topLeft(), "tr": r.topRight(),
                "bl": r.bottomLeft(), "br": r.bottomRight()}

    def bounded(self, point):
        return QPointF(max(0, min(point.x(), self.width())),
                       max(0, min(point.y(), self.height())))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            self.complete("cancel")
            return
        if event.button() != Qt.MouseButton.LeftButton:
            return
        self.commit_text()
        pos = self.bounded(event.position())
        self.origin = pos
        if self.selection.isEmpty():
            self.chosen.emit(self)
            self.drag_mode = "select"
            self.panel.hide()
            self.selection = QRectF(pos, pos)
        elif self.tool == "move":
            self.old_selection = QRectF(self.selection)
            self.drag_mode = "move" if self.selection.contains(pos) else None
            for key, pt in self.handles().items():
                if (pt-pos).manhattanLength() <= 14:
                    self.drag_mode = key
            if self.drag_mode:
                self.panel.hide()
        elif self.selection.contains(pos):
            if self.tool == "text":
                self.begin_text(pos)
            elif self.tool == "number":
                n = 1 + sum(m.kind == "number" for m in self.history.items)
                self.history.add(Mark("number", pos, pos, self.color, self.stroke, str(n)))
            else:
                self.active_mark = Mark(self.tool, pos, pos, self.color, self.stroke)
                self.drag_mode = "draw"
        self.update()

    def mouseMoveEvent(self, event):
        pos = self.bounded(event.position())
        if self.drag_mode == "select":
            self.selection = QRectF(self.origin, pos).normalized()
        elif self.drag_mode == "draw" and self.active_mark:
            pos = QPointF(max(self.selection.left(), min(pos.x(), self.selection.right())),
                          max(self.selection.top(), min(pos.y(), self.selection.bottom())))
            self.active_mark.end = pos
            if self.tool == "pen":
                self.active_mark.points.append(pos)
        elif self.drag_mode == "move":
            delta = pos-self.origin
            r = self.old_selection.translated(delta)
            r.moveLeft(max(0, min(r.left(), self.width()-r.width())))
            r.moveTop(max(0, min(r.top(), self.height()-r.height())))
            self.selection = r
        elif self.drag_mode in ("tl", "tr", "bl", "br"):
            r = self.old_selection
            opposite = {"tl": r.bottomRight(), "tr": r.bottomLeft(),
                        "bl": r.topRight(), "br": r.topLeft()}[self.drag_mode]
            self.selection = QRectF(opposite, pos).normalized()
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() != Qt.MouseButton.LeftButton:
            return
        if self.drag_mode == "draw" and self.active_mark:
            self.history.add(self.active_mark)
            self.active_mark = None
        self.drag_mode = None
        if self.selection.width() < 4 or self.selection.height() < 4:
            self.selection = QRectF()
            self.panel.hide()
        else:
            self.position_panel()
        self.update()

    def begin_text(self, pos):
        self.text_pos = pos
        self.editor = QLineEdit(self)
        self.editor.setPlaceholderText(self.t("text_prompt"))
        self.editor.setAccessibleName(self.t("text"))
        self.editor.setGeometry(max(0, min(int(pos.x()), self.width()-350)),
                                max(0, min(int(pos.y())-25, self.height()-44)), 345, 40)
        self.editor.returnPressed.connect(self.commit_text)
        self.editor.show()
        self.editor.setFocus()

    def commit_text(self):
        if self.editor:
            text = self.editor.text().strip()
            self.editor.deleteLater()
            self.editor = None
            if text:
                self.history.add(Mark("text", self.text_pos, self.text_pos,
                                      self.color, self.stroke, text))
            self.setFocus()
            self.update()

    def complete(self, action):
        if action == "cancel":
            self.finished.emit("cancel", None)
        elif not self.selection.isEmpty():
            self.commit_text()
            image = render_crop(self.screen_image, self.selection,
                                self.history.items, self.scale)
            self.finished.emit(action, image)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            if self.editor:
                self.editor.deleteLater()
                self.editor = None
                self.setFocus()
            else:
                self.complete("cancel")
            return
        if event.matches(QKeySequence.StandardKey.Copy):
            self.complete("copy")
        elif event.matches(QKeySequence.StandardKey.Save):
            self.complete("save")
        elif event.matches(QKeySequence.StandardKey.Undo):
            self.undo()
        elif event.matches(QKeySequence.StandardKey.Redo):
            self.redo()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.complete("copy")
        elif not event.modifiers():
            for key, glyph, shortcut in TOOLS:
                if event.text().upper() == shortcut:
                    self.set_tool(key)
                    break
        else:
            super().keyPressEvent(event)


"""LumaShot: local-only screenshot tool for Windows. Python + PySide6."""
import ctypes
from ctypes import wintypes
from datetime import datetime
import os
from pathlib import Path
import sys
import traceback

from PySide6.QtCore import (
    QAbstractNativeEventFilter, QSettings, QStandardPaths, Qt, QTimer,
)
from PySide6.QtGui import (
    QAction, QColor, QFont, QIcon, QLinearGradient, QPainter, QPen, QPixmap,
)
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMessageBox, QPushButton, QSystemTrayIcon,
    QVBoxLayout, QWidget,
)

BASE_STYLE = """
QWidget { color: #f3f0fc; font-family: 'Segoe UI'; font-size: 13px; }
QMainWindow, QWidget#root { background: #111119; }
QLabel { background: transparent; }
QLabel#muted { color: #a8a5bb; }
QLabel#brand { font-size: 22px; font-weight: 700; }
QLabel#eyebrow { color: #c1a7ff; font-size: 11px; font-weight: 700; }
QLabel#headline { font-size: 28px; font-weight: 700; }
QLabel#section { font-size: 16px; font-weight: 600; }
QFrame#card { background: #1c1c28; border: 1px solid #2d2c3d; border-radius: 12px; }
QPushButton { background: #2b293b; border: 1px solid #403b56;
              border-radius: 7px; padding: 9px 15px; font-weight: 600; }
QPushButton:hover { background: #393449; border-color: #a78bfa; }
QPushButton:pressed { background: #4b405e; }
QPushButton#primary { background: #9267ee; border: none; color: white;
                      font-size: 16px; padding: 15px 23px; }
QPushButton#primary:hover { background: #a47cfa; }
QPushButton#primary:disabled { background: #4f4269; color: #beb5ce; }
QComboBox { background: #282635; border: 1px solid #49415e; border-radius: 6px;
            padding: 8px 14px; min-width: 120px; }
QComboBox QAbstractItemView { background: #282635; color: white; selection-background-color: #7856bd; }
QMenu { background: #22212e; color: white; padding: 5px; border: 1px solid #454055; }
QMenu::item { padding: 7px 25px; }
QMenu::item:selected { background: #6b4bb1; border-radius: 3px; }
QToolTip { color: white; background: #292637; border: 1px solid #756193; padding: 5px; }
QMessageBox { background: #20202c; }
"""


def app_icon():
    pix = QPixmap(64, 64)
    pix.fill(Qt.GlobalColor.transparent)
    p = QPainter(pix)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    gradient = QLinearGradient(0, 0, 64, 64)
    gradient.setColorAt(0, QColor("#b991ff"))
    gradient.setColorAt(1, QColor("#6240cf"))
    p.setBrush(gradient)
    p.setPen(Qt.PenStyle.NoPen)
    p.drawRoundedRect(1, 1, 62, 62, 16, 16)
    p.setPen(QPen(QColor("white"), 4, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
    for a, b, c, d in [(18, 27, 18, 18), (18, 18, 27, 18), (37, 18, 46, 18),
                       (46, 18, 46, 27), (46, 37, 46, 46), (46, 46, 37, 46),
                       (27, 46, 18, 46), (18, 46, 18, 37)]:
        p.drawLine(a, b, c, d)
    p.end()
    return QIcon(pix)


class Hotkeys(QAbstractNativeEventFilter):
    """Register hotkeys without a keyboard hook; report conflicts honestly."""
    def __init__(self, callback):
        super().__init__()
        self.callback = callback
        self.registered = []
        if sys.platform == "win32":
            for identifier, modifiers, key, label in [
                (0x5B51, 0x4000, 0x2C, "Print Screen"),
                (0x5B52, 0x4000 | 0x0002 | 0x0004, 0x78, "Ctrl+Shift+F9"),
            ]:
                if ctypes.windll.user32.RegisterHotKey(None, identifier, modifiers, key):
                    self.registered.append((identifier, label))

    def nativeEventFilter(self, event_type, message):
        if sys.platform == "win32":
            msg = wintypes.MSG.from_address(int(message))
            if msg.message == 0x0312 and any(i == msg.wParam for i, _ in self.registered):
                QTimer.singleShot(0, self.callback)
                return True, 0
        return False, 0

    def close(self):
        if sys.platform == "win32":
            for identifier, _ in self.registered:
                ctypes.windll.user32.UnregisterHotKey(None, identifier)
        self.registered.clear()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("LumaShot", "LumaShot")
        self.lang = self.settings.value("language", "ro")
        if self.lang not in LANGUAGES:
            self.lang = "ro"
        pictures = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation)
        self.folder = self.settings.value("folder", str(Path(pictures) / "LumaShot"))
        self.overlays = []
        self.capture_pending = False
        self.restore_window = True
        self.quitting = False
        self.setWindowTitle("LumaShot")
        self.setWindowIcon(app_icon())
        self.setMinimumSize(800, 570)
        self.resize(860, 600)
        self.hotkeys = Hotkeys(self.start_capture)
        QApplication.instance().installNativeEventFilter(self.hotkeys)
        self.tray = QSystemTrayIcon(self.windowIcon(), self)
        self.tray.setToolTip("LumaShot")
        self.tray.activated.connect(self.tray_activated)
        self.rebuild_ui()
        self.rebuild_tray()
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray.show()

    def t(self, key, **values):
        return tr(self.lang, key, **values)

    def label(self, key, name="", wrap=False):
        label = QLabel(self.t(key))
        if name:
            label.setObjectName(name)
        label.setWordWrap(wrap)
        return label

    def rebuild_ui(self):
        old = self.takeCentralWidget()
        if old:
            old.deleteLater()
        root = QWidget()
        root.setObjectName("root")
        layout = QVBoxLayout(root)
        layout.setContentsMargins(34, 25, 34, 24)
        layout.setSpacing(19)
        header = QHBoxLayout()
        icon = QLabel()
        icon.setPixmap(self.windowIcon().pixmap(38, 38))
        header.addWidget(icon)
        header.addSpacing(5)
        brand = QLabel("LumaShot")
        brand.setObjectName("brand")
        header.addWidget(brand)
        header.addStretch()
        header.addWidget(self.label("language", "muted"))
        language = QComboBox()
        language.setAccessibleName(self.t("language"))
        for code, name in LANGUAGES.items():
            language.addItem(name, code)
        language.setCurrentIndex(list(LANGUAGES).index(self.lang))
        language.currentIndexChanged.connect(lambda index: self.change_language(language.itemData(index)))
        header.addWidget(language)
        layout.addLayout(header)
        hero = QFrame()
        hero.setObjectName("card")
        hero_layout = QVBoxLayout(hero)
        hero_layout.setContentsMargins(26, 24, 26, 24)
        hero_layout.setSpacing(12)
        hero_layout.addWidget(self.label("version", "eyebrow"))
        hero_layout.addWidget(self.label("tagline", "headline", True))
        hero_layout.addWidget(self.label("intro", "muted", True))
        hero_layout.addSpacing(8)
        row = QHBoxLayout()
        self.capture_button = QPushButton("＋   " + self.t("capture"))
        self.capture_button.setAccessibleName(self.t("capture"))
        self.capture_button.setObjectName("primary")
        self.capture_button.setMinimumHeight(56)
        self.capture_button.clicked.connect(self.start_capture)
        row.addWidget(self.capture_button)
        row.addSpacing(14)
        labels = [name for _, name in self.hotkeys.registered]
        shortcuts = QLabel("\n".join(labels) if labels else self.t("no_hotkey"))
        shortcuts.setObjectName("muted")
        shortcuts.setWordWrap(True)
        row.addWidget(shortcuts, 1)
        hero_layout.addLayout(row)
        hero_layout.addWidget(self.label("screen_note", "muted", True))
        layout.addWidget(hero)
        layout.addWidget(self.label("settings", "section"))
        folder_row = QHBoxLayout()
        folder_text = QVBoxLayout()
        folder_text.addWidget(self.label("folder"))
        self.folder_label = QLabel(self.folder)
        self.folder_label.setObjectName("muted")
        self.folder_label.setWordWrap(True)
        folder_text.addWidget(self.folder_label)
        folder_row.addLayout(folder_text, 1)
        choose = QPushButton(self.t("browse"))
        choose.clicked.connect(self.choose_folder)
        folder_row.addWidget(choose)
        layout.addLayout(folder_row)
        layout.addStretch()
        self.status = self.label("ready", "eyebrow")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        bottom = QHBoxLayout()
        bottom.addWidget(self.label("local", "muted"))
        bottom.addStretch()
        quit_button = QPushButton(self.t("quit"))
        quit_button.clicked.connect(self.quit_app)
        bottom.addWidget(quit_button)
        layout.addLayout(bottom)
        if QSystemTrayIcon.isSystemTrayAvailable():
            layout.addWidget(self.label("trayhint", "muted", True))
        self.setCentralWidget(root)
        if not labels:
            self.status.setText(self.t("no_hotkey"))
        elif "Print Screen" not in labels:
            self.status.setText(self.t("print_busy", key=labels[0]))

    def rebuild_tray(self):
        old_menu = self.tray.contextMenu()
        menu = QMenu(self)
        for key, callback in [("capture", self.start_capture),
                              ("open", self.show_main), ("quit", self.quit_app)]:
            action = QAction(self.t(key), self)
            action.triggered.connect(callback)
            menu.addAction(action)
        self.tray.setContextMenu(menu)
        if old_menu:
            old_menu.deleteLater()

    def change_language(self, code):
        if code == self.lang:
            return
        self.lang = code
        self.settings.setValue("language", code)
        # Defer replacement until the combo box signal finishes.
        QTimer.singleShot(0, self.rebuild_ui)
        QTimer.singleShot(0, self.rebuild_tray)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.t("choose_folder"), self.folder)
        if folder:
            self.folder = folder
            self.settings.setValue("folder", folder)
            self.folder_label.setText(folder)

    def show_main(self):
        if self.overlays or self.capture_pending:
            return
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            self.start_capture()
        elif reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_main()

    def start_capture(self):
        if self.overlays or self.capture_pending:
            return
        self.capture_pending = True
        self.restore_window = self.isVisible()
        self.capture_button.setEnabled(False)
        self.status.setText(self.t("capture_busy"))
        self.hide()
        # Let Windows finish removing the main window and tray menu.
        QTimer.singleShot(260, self.capture_screens)

    def capture_screens(self):
        try:
            shots = [(screen, screen.grabWindow(0)) for screen in QApplication.screens()]
            if not shots or any(pix.isNull() for _, pix in shots):
                raise RuntimeError("Screen capture returned no image")
            for screen, pix in shots:
                overlay = CaptureOverlay(screen, pix, self.lang)
                overlay.chosen.connect(self.choose_overlay)
                overlay.finished.connect(self.finish_capture)
                self.overlays.append(overlay)
            # Grab all images first, then display the overlays.
            for overlay in self.overlays:
                overlay.show()
            from PySide6.QtGui import QCursor
            under_cursor = QApplication.screenAt(QCursor.pos())
            target = next((w for w in self.overlays if w.geometry() == under_cursor.geometry()),
                          self.overlays[0]) if under_cursor else self.overlays[0]
            target.raise_()
            target.activateWindow()
            target.setFocus()
        except Exception:
            traceback.print_exc()
            self.close_overlays()
            self.show()
            QMessageBox.warning(self, self.t("error"), self.t("capture_error"))
        finally:
            self.capture_pending = False
            self.capture_button.setEnabled(True)

    def choose_overlay(self, chosen):
        for overlay in self.overlays:
            if overlay is not chosen:
                overlay.hide()
        chosen.activateWindow()
        chosen.setFocus()

    def close_overlays(self):
        for overlay in self.overlays:
            overlay.close()
        self.overlays.clear()

    def finish_capture(self, action, image):
        if action == "save":
            # Keep the editor intact if the save dialog is cancelled or fails.
            editor = next((w for w in self.overlays if w.isVisible()), None)
            for overlay in self.overlays:
                overlay.hide()
            try:
                Path(self.folder).mkdir(parents=True, exist_ok=True)
                filename = str(Path(self.folder) / ("LumaShot_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f") + ".png"))
                path, file_filter = QFileDialog.getSaveFileName(
                    self, self.t("save_title"), filename, self.t("format"))
                if not path:
                    if editor:
                        editor.show()
                        editor.activateWindow()
                    return
                jpeg = "JPEG" in file_filter
                suffix = Path(path).suffix.lower()
                if suffix not in (".png", ".jpg", ".jpeg"):
                    path += ".jpg" if jpeg else ".png"
                fmt = "JPEG" if Path(path).suffix.lower() in (".jpg", ".jpeg") else "PNG"
                if not image.save(path, fmt, 95):
                    raise OSError("QImage.save returned false")
                self.folder = str(Path(path).parent)
                self.settings.setValue("folder", self.folder)
                self.folder_label.setText(self.folder)
                message = self.t("saved", path=path)
            except (OSError, ValueError):
                QMessageBox.warning(self, self.t("error"), self.t("save_error"))
                if editor:
                    editor.show()
                    editor.activateWindow()
                return
        elif action == "copy":
            QApplication.clipboard().setImage(image)
            message = self.t("copied")
        else:
            message = self.t("cancelled")
        self.close_overlays()
        self.status.setText(message)
        if self.restore_window:
            self.show_main()
        elif action != "cancel":
            self.tray.showMessage("LumaShot", message,
                                  QSystemTrayIcon.MessageIcon.Information, 2000)

    def closeEvent(self, event):
        if not self.quitting and self.tray.isVisible():
            event.ignore()
            self.hide()
        else:
            event.accept()
            self.quit_app()

    def quit_app(self):
        self.quitting = True
        self.close_overlays()
        self.tray.hide()
        self.hotkeys.close()
        QApplication.instance().quit()


def main():
    QApplication.setApplicationName("LumaShot")
    QApplication.setOrganizationName("LumaShot")
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(BASE_STYLE)
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(app_icon())
    # A second launch reopens the existing app rather than competing for hotkeys.
    socket = QLocalSocket()
    socket.connectToServer("LumaShot.Personal.v1")
    if socket.waitForConnected(250):
        socket.write(b"show")
        socket.waitForBytesWritten(250)
        socket.disconnectFromServer()
        return 0
    server = QLocalServer()
    server.setSocketOptions(QLocalServer.SocketOption.UserAccessOption)
    if not server.listen("LumaShot.Personal.v1"):
        return 1
    window = MainWindow()
    def connected():
        connection = server.nextPendingConnection()
        if connection:
            connection.disconnectFromServer()
            connection.deleteLater()
        window.show_main()
    server.newConnection.connect(connected)
    app.aboutToQuit.connect(window.hotkeys.close)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

