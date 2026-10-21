# Original LumaShot code and artwork: MIT. Bundled icons retain their own notices.
LUMASHOT_LICENSE = 'MIT License\n\nCopyright (c) 2026 TOKKAB1\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n'

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


STRINGS["ro"].update({
    "hotkey_label": "Scurtătură pentru captură", "hotkey_hint": "Apasă combinația dorită",
    "apply": "Aplică", "hotkey_invalid": "Alege o singură combinație cu Ctrl, Alt sau Shift, o tastă F sau Print Screen.",
    "hotkey_busy": "Combinația este ocupată sau rezervată de Windows. Scurtătura anterioară rămâne activă.",
    "hotkey_saved": "Scurtătură activă: {key}", "more_colors": "Altă culoare…",
})
STRINGS["ru"].update({
    "hotkey_label": "Сочетание для снимка", "hotkey_hint": "Нажмите нужное сочетание",
    "apply": "Применить", "hotkey_invalid": "Выберите одно сочетание с Ctrl, Alt или Shift, клавишу F или Print Screen.",
    "hotkey_busy": "Сочетание занято или зарезервировано Windows. Предыдущее сочетание остаётся активным.",
    "hotkey_saved": "Активное сочетание: {key}", "more_colors": "Другой цвет…",
})
STRINGS["en"].update({
    "hotkey_label": "Capture shortcut", "hotkey_hint": "Press your preferred shortcut",
    "apply": "Apply", "hotkey_invalid": "Choose one combination with Ctrl, Alt or Shift, an F key, or Print Screen.",
    "hotkey_busy": "This shortcut is in use or reserved by Windows. The previous shortcut remains active.",
    "hotkey_saved": "Active shortcut: {key}", "more_colors": "Custom color…",
})


for code, additions in {
    "ro": {
        "capture": "Selectează o zonă", "full_capture": "Ecran complet",
        "general": "General", "formats": "Format", "theme": "Aspect",
        "light": "Luminos", "dark": "Întunecat",
        "notifications": "Notificări după copiere și salvare",
        "remember_area": "Memorează ultima zonă selectată",
        "include_cursor": "Include cursorul în captură",
        "hotkey_label": "Captură de zonă", "full_hotkey": "Ecran complet",
        "button_only": "Dezactivată — folosește butonul",
        "shortcut_unavailable": "Scurtătură indisponibilă. Alege alta sau folosește butonul.",
        "default_format": "Format pentru salvare", "jpeg_quality": "Calitate JPEG",
        "full_action": "La captura ecranului complet", "edit_first": "Deschide editorul",
        "save_instant": "Salvează imediat în dosar",
        "screen_note": "Ecran complet capturează monitorul pe care se află cursorul.",
        "settings_saved": "Preferințele se salvează automat. Scurtăturile se confirmă cu Aplică.",
    },
    "ru": {
        "capture": "Выбрать область", "full_capture": "Весь экран",
        "general": "Общие", "formats": "Формат", "theme": "Оформление",
        "light": "Светлое", "dark": "Тёмное",
        "notifications": "Уведомлять о копировании и сохранении",
        "remember_area": "Запоминать последнюю выбранную область",
        "include_cursor": "Включать курсор в снимок",
        "hotkey_label": "Снимок области", "full_hotkey": "Весь экран",
        "button_only": "Отключено — используйте кнопку",
        "shortcut_unavailable": "Сочетание недоступно. Выберите другое или используйте кнопку.",
        "default_format": "Формат сохранения", "jpeg_quality": "Качество JPEG",
        "full_action": "При снимке всего экрана", "edit_first": "Открыть редактор",
        "save_instant": "Сразу сохранить в папку",
        "screen_note": "Снимок всего экрана захватывает монитор, на котором находится курсор.",
        "settings_saved": "Настройки сохраняются автоматически. Сочетания подтвердите кнопкой «Применить».",
    },
    "en": {
        "capture": "Select an area", "full_capture": "Full screen",
        "general": "General", "formats": "Format", "theme": "Appearance",
        "light": "Light", "dark": "Dark",
        "notifications": "Notify after copying and saving",
        "remember_area": "Remember the last selected area",
        "include_cursor": "Include the cursor in screenshots",
        "hotkey_label": "Area capture", "full_hotkey": "Full screen",
        "button_only": "Disabled — use the button",
        "shortcut_unavailable": "Shortcut unavailable. Choose another or use the button.",
        "default_format": "Save format", "jpeg_quality": "JPEG quality",
        "full_action": "When capturing the full screen", "edit_first": "Open the editor",
        "save_instant": "Save immediately to folder",
        "screen_note": "Full screen captures the monitor under your cursor.",
        "settings_saved": "Preferences save automatically. Confirm shortcuts with Apply.",
    },
}.items():
    STRINGS[code].update(additions)


for code, additions in {
    "ro": {
        "tip_area": "Selectează o zonă de pe oricare monitor, apoi adnotează, copiază sau salvează.",
        "tip_full_edit": "Capturează monitorul de sub cursor și deschide editorul cu tot ecranul selectat.",
        "tip_full_save": "Salvează imediat monitorul de sub cursor în dosarul ales, fără editor.",
        "tip_language": "Schimbă limba interfeței, meniurilor și explicațiilor.",
        "tip_theme": "Schimbă aspectul aplicației, meniului din tray și editorului.",
        "tip_notifications": "Afișează o notificare Windows după copiere sau salvare, inclusiv salvarea imediată.",
        "tip_remember_area": "Reutilizează ultima zonă copiată sau salvată pe același monitor. Captura completă nu o înlocuiește.",
        "tip_include_cursor": "Include cursorul în poziția sa din momentul capturii, înainte de selectarea zonei.",
        "tip_enable_hotkey": "Bifează pentru activare sau debifează pentru dezactivare, apoi apasă Aplică. Butonul de captură rămâne disponibil.",
        "tip_apply": "Confirmă combinația de taste și activarea sau dezactivarea acestei scurtături.",
        "tip_hotkey": "Apasă combinația dorită, apoi Aplică. Modificarea nu devine activă până la confirmare.",
        "tip_format": "PNG păstrează imaginea fără pierderi. JPEG ocupă de obicei mai puțin spațiu, cu pierderi de calitate.",
        "tip_quality": "Calitate JPEG între 1 și 100. O valoare mai mare păstrează mai multe detalii. Nu se aplică formatului PNG.",
        "tip_full_action": "Alege dacă butonul și scurtătura pentru ecran complet deschid editorul sau salvează imediat în dosar.",
        "tip_palette": "Deschide paleta de culori și reglajul grosimii liniei.",
        "tip_tray": "LumaShot\nClic stânga: selectează o zonă\nClic dreapta: meniu",
        "tip_general_tab": "Aspect, limbă, comportamentul capturii și dosar.",
        "tip_shortcuts_tab": "Activează și configurează scurtăturile pentru cele două moduri de captură.",
        "tip_format_tab": "Formatul imaginii, calitatea JPEG și salvarea imediată.",
    },
    "ru": {
        "tip_area": "Выделите область на любом мониторе, затем добавьте пометки, скопируйте или сохраните снимок.",
        "tip_full_edit": "Захватить монитор под курсором и открыть редактор с выделенным экраном.",
        "tip_full_save": "Сразу сохранить монитор под курсором в выбранную папку, без редактора.",
        "tip_language": "Изменить язык интерфейса, меню и подсказок.",
        "tip_theme": "Изменить оформление приложения, меню в трее и редактора.",
        "tip_notifications": "Показывать уведомление Windows после копирования или сохранения, в том числе мгновенного.",
        "tip_remember_area": "Восстановить последнюю скопированную или сохранённую область на том же мониторе. Снимок всего экрана её не заменяет.",
        "tip_include_cursor": "Включить курсор в его положении на момент снимка, до выделения области.",
        "tip_enable_hotkey": "Установите или снимите флажок и нажмите «Применить». Кнопка снимка остаётся доступной.",
        "tip_apply": "Подтвердить комбинацию клавиш и включение или отключение этого сочетания.",
        "tip_hotkey": "Нажмите нужное сочетание, затем «Применить». Изменение действует только после подтверждения.",
        "tip_format": "PNG сохраняет изображение без потерь. JPEG обычно занимает меньше места, но теряет часть качества.",
        "tip_quality": "Качество JPEG от 1 до 100. Более высокое значение сохраняет больше деталей. На PNG не влияет.",
        "tip_full_action": "Выберите действие кнопки и сочетания для всего экрана: открыть редактор или сразу сохранить в папку.",
        "tip_palette": "Открыть палитру цветов и настройку толщины линии.",
        "tip_tray": "LumaShot\nЛевый щелчок: выбрать область\nПравый щелчок: меню",
        "tip_general_tab": "Оформление, язык, параметры снимка и папка.",
        "tip_shortcuts_tab": "Включение и настройка сочетаний для двух режимов снимка.",
        "tip_format_tab": "Формат изображения, качество JPEG и мгновенное сохранение.",
    },
    "en": {
        "tip_area": "Select an area on any monitor, then annotate, copy or save it.",
        "tip_full_edit": "Capture the monitor under your cursor and open the editor with the whole screen selected.",
        "tip_full_save": "Save the monitor under your cursor immediately to the selected folder, without opening the editor.",
        "tip_language": "Change the language of the interface, menus and tooltips.",
        "tip_theme": "Change the appearance of the app, tray menu and editor.",
        "tip_notifications": "Show a Windows notification after copying or saving, including immediate saves.",
        "tip_remember_area": "Restore the last copied or saved area on the same monitor. Full-screen captures do not replace it.",
        "tip_include_cursor": "Include the cursor at its position when the screen is captured, before selecting an area.",
        "tip_enable_hotkey": "Check to enable or uncheck to disable, then click Apply. The capture button stays available.",
        "tip_apply": "Confirm this key combination and whether this shortcut is enabled or disabled.",
        "tip_hotkey": "Press your preferred combination, then Apply. Changes take effect only after confirmation.",
        "tip_format": "PNG preserves the image without loss. JPEG usually uses less space, with some loss of quality.",
        "tip_quality": "JPEG quality from 1 to 100. Higher values preserve more detail. This does not affect PNG.",
        "tip_full_action": "Choose whether the full-screen button and shortcut open the editor or save directly to the folder.",
        "tip_palette": "Open the color palette and line-width control.",
        "tip_tray": "LumaShot\nLeft-click: select an area\nRight-click: menu",
        "tip_general_tab": "Appearance, language, capture behavior and folder.",
        "tip_shortcuts_tab": "Enable and customize shortcuts for the two capture modes.",
        "tip_format_tab": "Image format, JPEG quality and immediate saving.",
    },
}.items():
    STRINGS[code].update(additions)


def wrapped_tip(text):
    import textwrap
    return "\n".join(textwrap.fill(line, width=54, break_long_words=False, break_on_hyphens=False)
                     for line in text.splitlines())


def tr(language, message_key, **values):
    text = STRINGS.get(language, STRINGS["ro"])[message_key]
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
    QPushButton, QSpinBox, QWidget, QGridLayout, QColorDialog,
)


# Official Lucide icons, pinned to c29c276f16590cf017126671535ad8c792be64d8.
# https://github.com/lucide-icons/lucide — ISC / MIT notices retained below.
LUCIDE_LICENSE = 'ISC License\n\nCopyright (c) 2026 Lucide Icons and Contributors\n\nPermission to use, copy, modify, and/or distribute this software for any\npurpose with or without fee is hereby granted, provided that the above\ncopyright notice and this permission notice appear in all copies.\n\nTHE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES\nWITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF\nMERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR\nANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES\nWHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN\nACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF\nOR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.\n\n---\n\nThe following Lucide icons are derived from the Feather project:\n\nairplay, alert-circle, alert-octagon, alert-triangle, aperture, arrow-down-circle, arrow-down-left, arrow-down-right, arrow-down, arrow-left-circle, arrow-left, arrow-right-circle, arrow-right, arrow-up-circle, arrow-up-left, arrow-up-right, arrow-up, at-sign, calendar, cast, check, chevron-down, chevron-left, chevron-right, chevron-up, chevrons-down, chevrons-left, chevrons-right, chevrons-up, circle, clipboard, clock, code, columns, command, compass, corner-down-left, corner-down-right, corner-left-down, corner-left-up, corner-right-down, corner-right-up, corner-up-left, corner-up-right, crosshair, database, divide-circle, divide-square, dollar-sign, download, external-link, feather, frown, hash, headphones, help-circle, info, italic, key, layout, life-buoy, link-2, link, loader, lock, log-in, log-out, maximize, meh, minimize, minimize-2, minus-circle, minus-square, minus, monitor, moon, more-horizontal, more-vertical, move, music, navigation-2, navigation, octagon, pause-circle, percent, plus-circle, plus-square, plus, power, radio, rss, search, server, share, shopping-bag, sidebar, smartphone, smile, square, table-2, tablet, target, terminal, trash-2, trash, triangle, tv, type, upload, x-circle, x-octagon, x-square, x, zoom-in, zoom-out\n\nThe MIT License (MIT) (for the icons listed above)\n\nCopyright (c) 2013-present Cole Bemis\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n'
LUCIDE_SVGS = {
    "capture": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M3 7V5a2 2 0 0 1 2-2h2\" />\n  <path d=\"M17 3h2a2 2 0 0 1 2 2v2\" />\n  <path d=\"M21 17v2a2 2 0 0 1-2 2h-2\" />\n  <path d=\"M7 21H5a2 2 0 0 1-2-2v-2\" />\n</svg>\n",
    "move": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M12 2v20\" />\n  <path d=\"m15 19-3 3-3-3\" />\n  <path d=\"m19 9 3 3-3 3\" />\n  <path d=\"M2 12h20\" />\n  <path d=\"m5 9-3 3 3 3\" />\n  <path d=\"m9 5 3-3 3 3\" />\n</svg>\n",
    "pen": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z\" />\n  <path d=\"m15 5 4 4\" />\n</svg>\n",
    "line": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M5 12h14\" />\n</svg>\n",
    "arrow": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M13 5H19V11\" />\n  <path d=\"M19 5L5 19\" />\n</svg>\n",
    "rect": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\" />\n</svg>\n",
    "ellipse": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <circle cx=\"12\" cy=\"12\" r=\"10\" />\n</svg>\n",
    "text": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M12 4v16\" />\n  <path d=\"M4 7V5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2\" />\n  <path d=\"M9 20h6\" />\n</svg>\n",
    "highlight": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"m9 11-6 6v3h9l3-3\" />\n  <path d=\"m22 12-4.6 4.6a2 2 0 0 1-2.8 0l-5.2-5.2a2 2 0 0 1 0-2.8L14 4\" />\n</svg>\n",
    "mask": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\" />\n  <line x1=\"9\" x2=\"15\" y1=\"15\" y2=\"9\" />\n</svg>\n",
    "number": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M11 5h10\" />\n  <path d=\"M11 12h10\" />\n  <path d=\"M11 19h10\" />\n  <path d=\"M4 4h1v5\" />\n  <path d=\"M4 9h2\" />\n  <path d=\"M6.5 20H3.4c0-1 2.6-1.925 2.6-3.5a1.5 1.5 0 0 0-2.6-1.02\" />\n</svg>\n",
    "undo": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M9 14 4 9l5-5\" />\n  <path d=\"M4 9h10.5a5.5 5.5 0 0 1 5.5 5.5a5.5 5.5 0 0 1-5.5 5.5H11\" />\n</svg>\n",
    "redo": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"m15 14 5-5-5-5\" />\n  <path d=\"M20 9H9.5A5.5 5.5 0 0 0 4 14.5A5.5 5.5 0 0 0 9.5 20H13\" />\n</svg>\n",
    "copy": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <rect width=\"14\" height=\"14\" x=\"8\" y=\"8\" rx=\"2\" ry=\"2\" />\n  <path d=\"M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2\" />\n</svg>\n",
    "save": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M15.2 3a2 2 0 0 1 1.4.6l3.8 3.8a2 2 0 0 1 .6 1.4V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z\" />\n  <path d=\"M17 21v-7a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v7\" />\n  <path d=\"M7 3v4a1 1 0 0 0 1 1h7\" />\n</svg>\n",
    "cancel": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M18 6 6 18\" />\n  <path d=\"m6 6 12 12\" />\n</svg>\n",
    "folder": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2\" />\n</svg>\n",
    "open": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\" />\n  <path d=\"M10 4v4\" />\n  <path d=\"M2 8h20\" />\n  <path d=\"M6 4v4\" />\n</svg>\n",
    "quit": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"m16 17 5-5-5-5\" />\n  <path d=\"M21 12H9\" />\n  <path d=\"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4\" />\n</svg>\n",
    "language": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"m5 8 6 6\" />\n  <path d=\"m4 14 6-6 2-3\" />\n  <path d=\"M2 5h12\" />\n  <path d=\"M7 2h1\" />\n  <path d=\"m22 22-5-10-5 10\" />\n  <path d=\"M14 18h6\" />\n</svg>\n",
    "settings": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <path d=\"M10 5H3\" />\n  <path d=\"M12 19H3\" />\n  <path d=\"M14 3v4\" />\n  <path d=\"M16 17v4\" />\n  <path d=\"M21 12h-9\" />\n  <path d=\"M21 19h-5\" />\n  <path d=\"M21 5h-7\" />\n  <path d=\"M8 10v4\" />\n  <path d=\"M8 12H3\" />\n</svg>\n",
    "monitor": "<svg\n  xmlns=\"http://www.w3.org/2000/svg\"\n  width=\"24\"\n  height=\"24\"\n  viewBox=\"0 0 24 24\"\n  fill=\"none\"\n  stroke=\"currentColor\"\n  stroke-width=\"2\"\n  stroke-linecap=\"round\"\n  stroke-linejoin=\"round\"\n>\n  <rect width=\"20\" height=\"14\" x=\"2\" y=\"3\" rx=\"2\" />\n  <line x1=\"8\" x2=\"16\" y1=\"21\" y2=\"21\" />\n  <line x1=\"12\" x2=\"12\" y1=\"17\" y2=\"21\" />\n</svg>\n"
}

from functools import lru_cache
from PySide6.QtCore import QByteArray, QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtSvg import QSvgRenderer


@lru_cache(maxsize=80)
def ui_icon(name, color="#eeeaf8"):
    """Render once per name/color, then let QIcon choose the DPI-appropriate size."""
    source = LUCIDE_SVGS[name]
    icon = QIcon()
    for mode, stroke in ((QIcon.Mode.Normal, color), (QIcon.Mode.Disabled, "#777286")):
        renderer = QSvgRenderer(QByteArray(source.replace("currentColor", stroke).encode("utf-8")))
        for size in (16, 20, 24, 32, 40, 48, 64):
            pixmap = QPixmap(size, size)
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            icon.addPixmap(pixmap, mode)
            if mode == QIcon.Mode.Normal:
                icon.addPixmap(pixmap, QIcon.Mode.Active)
                icon.addPixmap(pixmap, QIcon.Mode.Selected)
    return icon

TOOLS = [
    ("move", "↔", "V"), ("pen", "✎", "P"), ("line", "╱", "L"),
    ("arrow", "↗", "A"), ("rect", "□", "R"),
    ("text", "T", "T"), ("highlight", "▰", "H"),
    ("number", "①", "N"),
]
COLORS = ["#a78bfa", "#ef4444", "#facc15", "#22c55e", "#ffffff", "#111118"]
PANEL_STYLE = """
QFrame#tools { background: #f2f2f7; border: 1px solid #b7b5c2; border-radius: 4px; }
QPushButton { color: #353341; background: transparent; border: none;
              border-radius: 3px; padding: 0; min-height: 0; }
QPushButton:hover { background: #dedce8; }
QPushButton:checked { background: #dcefe8; }
QPushButton#copy { background: #dcefe8; }
QLabel { color: #353341; border: none; }
QSpinBox { background: white; color: #353341; border: 1px solid #b7b5c2;
           border-radius: 3px; min-height: 24px; }
QLineEdit { color: white; background: #252534; border: 2px solid #118769;
            border-radius: 5px; padding: 7px; }
QToolTip { color: #f7fffc; background: #163e3b; border: 1px solid #568c7e;
           padding: 7px; border-radius: 4px; font-size: 12px; }
"""


class CaptureOverlay(QWidget):
    chosen = Signal(object)
    finished = Signal(str, object)

    def __init__(self, screen, screenshot, language, theme="light"):
        super().__init__(None, Qt.WindowType.FramelessWindowHint |
                         Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Tool)
        self.setWindowTitle("LumaShot — Capture")
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setGeometry(screen.geometry())
        self.screen_image = screenshot.toImage()
        self.scale = screenshot.devicePixelRatio()
        self.screen_image.setDevicePixelRatio(1)
        self.lang = language
        self.theme = theme
        self.screen_key = screen.name() if hasattr(screen, "name") else "screen"
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
        panel_style = PANEL_STYLE
        colors = theme_colors(theme)
        for old, new in {"#f2f2f7": colors["raised"], "#b7b5c2": colors["border"],
                         "#353341": colors["fg"], "#dedce8": colors["selected"],
                         "#dcefe8": colors["selected"], "background: white": "background: " + colors["input"],
                         "#252534": colors["input"], "color: white": "color: " + colors["fg"]}.items():
            panel_style = panel_style.replace(old, new)
        self.setStyleSheet(panel_style)
        self.panel = self.make_panel()
        self.panel.hide()
        self.actions.hide()
        self.palette.hide()

    def tool_button(self, key, callback, checkable=False):
        button = QPushButton()
        button.setFixedSize(26, 26)
        button.setStyleSheet("QPushButton { min-height:26px; max-height:26px; padding:0; }")
        button.setIcon(ui_icon(key, theme_colors(self.theme)["fg"]))
        button.setIconSize(QSize(18, 18))
        shortcut = {"copy": "Ctrl+C / Enter", "save": "Ctrl+S", "cancel": "Esc"}.get(key)
        button.setToolTip(wrapped_tip(self.t(key) + ("\n" + shortcut if shortcut else "")))
        button.setToolTipDuration(12000)
        button.setAccessibleName(self.t(key))
        button.setCheckable(checkable)
        button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        button.clicked.connect(callback)
        return button

    def t(self, message_key, **values):
        return tr(self.lang, message_key, **values)

    def make_panel(self):
        frame = QFrame(self)
        frame.setObjectName("tools")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(1)
        self.tool_buttons = {}
        for key, glyph, shortcut in TOOLS:
            button = self.tool_button(key, lambda checked=False, k=key: self.set_tool(k), True)
            button.setChecked(key == self.tool)
            layout.addWidget(button)
            self.tool_buttons[key] = button
        self.color_button = QPushButton()
        self.color_button.setFixedSize(26, 26)
        self.color_button.setToolTip(wrapped_tip(self.t("tip_palette")))
        self.color_button.setAccessibleName(self.t("color"))
        self.color_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.color_button.clicked.connect(self.toggle_palette)
        layout.addWidget(self.color_button)
        # Width is shown on demand with the palette, keeping the rail narrow.
        self.palette = QFrame(self)
        self.palette.setObjectName("tools")
        palette_layout = QVBoxLayout(self.palette)
        palette_layout.setContentsMargins(8, 8, 8, 8)
        palette_layout.setSpacing(7)
        swatches = QGridLayout()
        swatches.setSpacing(5)
        self.color_buttons = {}
        for index, color in enumerate(COLORS):
            button = QPushButton()
            button.setFixedSize(22, 22)
            button.setToolTip(self.t("colors")[index])
            button.setAccessibleName(self.t("colors")[index])
            button.clicked.connect(lambda checked=False, c=color: self.choose_color(c))
            swatches.addWidget(button, index // 3, index % 3)
            self.color_buttons[color] = button
        palette_layout.addLayout(swatches)
        more = QPushButton(self.t("more_colors"))
        more.setToolTip(self.t("more_colors"))
        more.setMinimumHeight(26)
        more.clicked.connect(self.custom_color)
        palette_layout.addWidget(more)
        self.set_color(self.color)
        width_row = QHBoxLayout()
        width_row.addWidget(QLabel(self.t("width")))
        width = QSpinBox()
        width.setRange(1, 12)
        width.setValue(self.stroke)
        width.setFixedWidth(48)
        width.setToolTip(self.t("width"))
        width.setAccessibleName(self.t("width"))
        width.valueChanged.connect(self.set_stroke)
        width_row.addWidget(width)
        palette_layout.addLayout(width_row)
        self.actions = QFrame(self)
        self.actions.setObjectName("tools")
        bottom = QHBoxLayout(self.actions)
        bottom.setContentsMargins(3, 3, 3, 3)
        bottom.setSpacing(1)
        for key, callback in (("undo", self.undo), ("redo", self.redo)):
            bottom.addWidget(self.tool_button(key, callback))
        for key in ("copy", "save", "cancel"):
            button = self.tool_button(key, lambda checked=False, k=key: self.complete(k))
            button.setObjectName(key)
            bottom.addWidget(button)
        frame.adjustSize()
        self.actions.adjustSize()
        return frame

    def set_color(self, color):
        self.color = color
        border_color = theme_colors(self.theme)["raised"]
        self.color_button.setStyleSheet(
            f"QPushButton {{ background:{color}; border:5px solid {border_color}; border-radius:3px; min-height:16px; max-height:16px; }}")
        for c, button in self.color_buttons.items():
            border = "#118769" if c == color else "#5f747b"
            button.setStyleSheet(
                f"QPushButton {{ background:{c}; border:2px solid {border}; border-radius:11px; padding:0; min-height:0; }}")

    def choose_color(self, color):
        self.set_color(color)
        self.palette.hide()
        self.setFocus()

    def custom_color(self):
        color = QColorDialog.getColor(QColor(self.color), self, self.t("color"),
                                      QColorDialog.ColorDialogOption.DontUseNativeDialog)
        if color.isValid():
            self.choose_color(color.name())

    def toggle_palette(self):
        if self.palette.isVisible():
            self.palette.hide()
            return
        self.palette.adjustSize()
        x = self.panel.x() + self.panel.width() + 5
        if x + self.palette.width() > self.width() - 4:
            x = self.panel.x() - self.palette.width() - 5
        y = self.panel.y() + self.color_button.y()
        self.palette.move(max(4, x), max(4, min(y, self.height()-self.palette.height()-4)))
        self.palette.show()
        self.palette.raise_()

    def hide_panels(self):
        self.panel.hide()
        self.actions.hide()
        self.palette.hide()

    def set_stroke(self, value):
        self.stroke = value

    def set_tool(self, tool):
        if tool not in self.tool_buttons:
            return
        self.commit_text()
        self.palette.hide()
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
        self.palette.hide()
        self.panel.adjustSize()
        self.actions.adjustSize()
        width, height = self.panel.width(), self.panel.height()
        x = int(self.selection.right()) + 6
        if x + width > self.width()-4:
            x = int(self.selection.left())-width-6
        x = max(4, min(x, self.width()-width-4))
        y = max(4, min(int(self.selection.bottom())-height, self.height()-height-4))
        self.panel.move(x, y)
        aw, ah = self.actions.width(), self.actions.height()
        ax = max(4, min(int(self.selection.right())-aw, self.width()-aw-4))
        ay = int(self.selection.bottom())+6
        if ay+ah > self.height()-4:
            ay = int(self.selection.top())-ah-6
        ay = max(4, min(ay, self.height()-ah-4))
        action_rect = QRect(ax, ay, aw, ah)
        if action_rect.intersects(self.panel.geometry()):
            # When both rails must be clamped inside an edge, keep them separate.
            y = ay-height-4 if ay-height-4 >= 4 else ay+ah+4
            self.panel.move(x, max(4, min(y, self.height()-height-4)))
        self.actions.move(ax, ay)
        self.panel.show()
        self.actions.show()

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
            p.setPen(QPen(QColor("#67cfb1"), 1, Qt.PenStyle.DashLine))
            p.setBrush(Qt.BrushStyle.NoBrush)
            p.drawRect(self.selection)
            if self.tool == "move" or not self.history.items:
                p.setBrush(QColor("#ffffff"))
                p.setPen(QColor("#118769"))
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
        self.palette.hide()
        self.commit_text()
        pos = self.bounded(event.position())
        self.origin = pos
        if self.selection.isEmpty():
            self.chosen.emit(self)
            self.drag_mode = "select"
            self.hide_panels()
            self.selection = QRectF(pos, pos)
        elif self.tool == "move":
            self.old_selection = QRectF(self.selection)
            self.drag_mode = "move" if self.selection.contains(pos) else None
            for key, pt in self.handles().items():
                if (pt-pos).manhattanLength() <= 14:
                    self.drag_mode = key
            if self.drag_mode:
                self.hide_panels()
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
            self.hide_panels()
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
            if self.palette.isVisible():
                self.palette.hide()
            elif self.editor:
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
    QAction, QColor, QFont, QIcon, QLinearGradient, QPainter, QPen, QPixmap, QPalette, QCursor,
)
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtWidgets import (
    QApplication, QComboBox, QFileDialog, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMessageBox, QPushButton, QSystemTrayIcon,
    QVBoxLayout, QWidget, QKeySequenceEdit, QTabWidget, QCheckBox, QFormLayout, QSlider, QToolTip,
    QStyle, QStyleOptionButton,
)

# Accent and light surfaces follow RTLite 3.2.8's palette.
def theme_colors(theme):
    common = {"accent": "#118769", "hover": "#0b7258", "tip_bg": "#163e3b", "tip_fg": "#f7fffc"}
    if theme == "dark":
        common.update(bg="#111b1d", raised="#1b292c", input="#243639", border="#3b5357",
                      fg="#edf5f3", muted="#abc1bd", selected="#254b43", accent_text="#7ad7ba")
    else:
        common.update(bg="#f1f3f4", raised="#f7f8f9", input="#ffffff", border="#dce1e5",
                      fg="#193d43", muted="#5f747b", selected="#e3f3ed", accent_text="#0b7258")
    return common


def theme_style(theme):
    c = theme_colors(theme)
    return f"""
QWidget {{ color: {c['fg']}; font-family: 'Segoe UI'; font-size: 13px; }}
QMainWindow, QWidget#root {{ background: {c['bg']}; }}
QLabel {{ background: transparent; }}
QLabel#muted {{ color: {c['muted']}; }}
QLabel#brand {{ font-size: 22px; font-weight: 700; }}
QLabel#headline {{ font-size: 28px; font-weight: 700; }}
QFrame#card {{ background: {c['raised']}; border: 1px solid {c['border']}; border-radius: 12px; }}
QPushButton {{ background: {c['input']}; border: 1px solid {c['border']};
    border-radius: 7px; padding: 9px 15px; font-weight: 600; }}
QPushButton:hover {{ background: {c['selected']}; border-color: {c['accent']}; }}
QPushButton:pressed {{ background: {c['selected']}; border-color: {c['hover']}; }}
QPushButton#primary {{ background: {c['accent']}; border: none; color: white;
    font-size: 16px; padding: 15px 23px; }}
QPushButton#primary:hover {{ background: {c['hover']}; }}
QPushButton#primary:disabled {{ background: {c['border']}; color: {c['muted']}; }}
QComboBox {{ background: {c['input']}; border: 1px solid {c['border']}; border-radius: 6px;
    padding: 8px 30px 8px 14px; min-width: 120px; }}
QComboBox::drop-down {{ border: none; width: 25px; }}
QComboBox::down-arrow {{ width: 0px; height: 0px; }}
QComboBox QAbstractItemView {{ background: {c['input']}; color: {c['fg']};
    selection-background-color: {c['accent']}; selection-color: white; }}
QKeySequenceEdit, QKeySequenceEdit QLineEdit {{ background: {c['input']}; color: {c['fg']};
    border: 1px solid {c['border']}; border-radius: 6px; padding: 6px; }}
QMenu {{ background: {c['raised']}; color: {c['fg']}; padding: 5px; border: 1px solid {c['border']}; }}
QMenu::item {{ padding: 7px 25px; }}
QMenu::item:selected {{ background: {c['hover']}; color: white; border-radius: 3px; }}
QToolTip {{ color: {c['tip_fg']}; background: {c['tip_bg']}; border: 1px solid #568c7e;
    padding: 7px; border-radius: 4px; font-size: 12px; }}
QMessageBox {{ background: {c['bg']}; }}
QTabWidget::pane {{ background: {c['raised']}; border: 1px solid {c['border']}; border-radius: 8px; top: -1px; }}
QTabBar::tab {{ background: transparent; padding: 10px 19px; border-bottom: 2px solid transparent; }}
QTabBar::tab:selected {{ color: {c['accent_text']}; border-bottom: 2px solid {c['accent']}; font-weight: 600; }}
QCheckBox {{ spacing: 9px; padding: 5px 0; }}
QCheckBox::indicator {{ width: 16px; height: 16px; }}
ContrastCheckBox::indicator {{ width: 20px; height: 20px; background: transparent; border: none; }}
QSpinBox {{ background: {c['input']}; border: 1px solid {c['border']}; border-radius: 5px; padding: 6px; }}
QSpinBox::up-button, QSpinBox::down-button {{ border: none; width: 18px; }}
QWidget:disabled {{ color: {c['muted']}; }}
QSlider::groove:horizontal {{ height: 4px; background: {c['border']}; border-radius: 2px; }}
QSlider::sub-page:horizontal {{ background: {c['accent']}; }}
QSlider::handle:horizontal {{ width: 14px; margin: -5px 0; background: {c['accent']}; border-radius: 7px; }}
QSlider::sub-page:horizontal:disabled {{ background: {c['border']}; }}
QSlider::handle:horizontal:disabled {{ background: {c['muted']}; }}
"""


BASE_STYLE = theme_style("light")


def apply_theme(theme):
    app = QApplication.instance()
    palette = app.style().standardPalette()
    c = theme_colors(theme)
    for role, color in {
        QPalette.ColorRole.Window: c["bg"], QPalette.ColorRole.Base: c["input"],
        QPalette.ColorRole.Button: c["input"], QPalette.ColorRole.WindowText: c["fg"],
        QPalette.ColorRole.Text: c["fg"], QPalette.ColorRole.ButtonText: c["fg"],
        QPalette.ColorRole.Highlight: c["accent"], QPalette.ColorRole.HighlightedText: "#ffffff",
        QPalette.ColorRole.ToolTipBase: c["tip_bg"], QPalette.ColorRole.ToolTipText: c["tip_fg"],
    }.items():
        palette.setColor(role, QColor(color))
    app.setPalette(palette)
    app.setStyleSheet(theme_style(theme))


def app_icon(size=64):
    pix = QPixmap(size, size)
    pix.fill(Qt.GlobalColor.transparent)
    p = QPainter(pix)
    p.scale(size / 64, size / 64)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    gradient = QLinearGradient(0, 0, 64, 64)
    gradient.setColorAt(0, QColor("#27ad8c"))
    gradient.setColorAt(1, QColor("#0b7258"))
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


def native_hotkey(sequence):
    """Translate a single Qt key combination to Windows RegisterHotKey arguments."""
    if sequence.count() != 1:
        raise ValueError("One combination required")
    combo = sequence[0]
    key, mods = combo.key(), combo.keyboardModifiers()
    flags = 0x4000
    for modifier, flag in ((Qt.KeyboardModifier.ControlModifier, 2),
                           (Qt.KeyboardModifier.AltModifier, 1),
                           (Qt.KeyboardModifier.ShiftModifier, 4),
                           (Qt.KeyboardModifier.MetaModifier, 8)):
        if mods & modifier:
            flags |= flag
    if Qt.Key.Key_A <= key <= Qt.Key.Key_Z or Qt.Key.Key_0 <= key <= Qt.Key.Key_9:
        vk = int(key)
    elif Qt.Key.Key_F1 <= key <= Qt.Key.Key_F24:
        vk = 0x70 + int(key) - int(Qt.Key.Key_F1)
    else:
        special = {Qt.Key.Key_Print: 0x2C, Qt.Key.Key_Space: 0x20,
                   Qt.Key.Key_Insert: 0x2D, Qt.Key.Key_Delete: 0x2E,
                   Qt.Key.Key_Home: 0x24, Qt.Key.Key_End: 0x23,
                   Qt.Key.Key_PageUp: 0x21, Qt.Key.Key_PageDown: 0x22,
                   Qt.Key.Key_Left: 0x25, Qt.Key.Key_Right: 0x27,
                   Qt.Key.Key_Up: 0x26, Qt.Key.Key_Down: 0x28,
                   Qt.Key.Key_Pause: 0x13, Qt.Key.Key_Backspace: 0x08}
        if key not in special:
            raise ValueError("Unsupported key")
        vk = special[key]
    if flags == 0x4000 and key != Qt.Key.Key_Print and not Qt.Key.Key_F1 <= key <= Qt.Key.Key_F24:
        raise ValueError("Modifier required")
    return flags, vk


class Hotkeys(QAbstractNativeEventFilter):
    """Register hotkeys without a keyboard hook; report conflicts honestly."""
    def __init__(self, callback, saved="", *, id_base=0x5B60, defaults=True, enabled=True):
        super().__init__()
        self.callback = callback
        self.registered = []
        self.bindings = {}
        self.id_base = id_base
        if sys.platform == "win32" and enabled:
            if saved:
                try:
                    self.replace(QKeySequence(saved, QKeySequence.SequenceFormat.PortableText))
                except ValueError:
                    pass
                return
            if not defaults:
                return
            for identifier, modifiers, key, label in [
                (0x5B51, 0x4000, 0x2C, "Print Screen"),
                (0x5B52, 0x4000 | 0x0002 | 0x0004, 0x78, "Ctrl+Shift+F9"),
            ]:
                if ctypes.windll.user32.RegisterHotKey(None, identifier, modifiers, key):
                    self.registered.append((identifier, label))
                    self.bindings[identifier] = (modifiers, key)

    def replace(self, sequence):
        binding = native_hotkey(sequence)
        label = sequence.toString(QKeySequence.SequenceFormat.PortableText)
        existing = next((identifier for identifier, value in self.bindings.items()
                         if value == binding), None)
        if existing is None:
            if sys.platform != "win32":
                return False
            # Alternate free IDs; acquire the new shortcut before releasing the old.
            identifier = next(i for i in (self.id_base, self.id_base + 1) if i not in self.bindings)
            if not ctypes.windll.user32.RegisterHotKey(None, identifier, *binding):
                return False
        else:
            identifier = existing
        for old, _ in self.registered:
            if old != identifier:
                ctypes.windll.user32.UnregisterHotKey(None, old)
        self.registered = [(identifier, label)]
        self.bindings = {identifier: binding}
        return True

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
        self.bindings.clear()


def capture_cursor(pixmap):
    """Composite the Windows cursor onto native pixels, including its AND/XOR mask."""
    if sys.platform != "win32":
        return pixmap

    class CursorInfo(ctypes.Structure):
        _fields_ = [("size", wintypes.DWORD), ("flags", wintypes.DWORD),
                    ("cursor", wintypes.HANDLE), ("pos", wintypes.POINT)]

    class IconInfo(ctypes.Structure):
        _fields_ = [("icon", wintypes.BOOL), ("x", wintypes.DWORD), ("y", wintypes.DWORD),
                    ("mask", wintypes.HANDLE), ("color", wintypes.HANDLE)]

    class MonitorInfo(ctypes.Structure):
        _fields_ = [("size", wintypes.DWORD), ("monitor", wintypes.RECT),
                    ("work", wintypes.RECT), ("flags", wintypes.DWORD)]

    class BitmapInfo(ctypes.Structure):
        _fields_ = [("size", wintypes.DWORD), ("width", wintypes.LONG), ("height", wintypes.LONG),
                    ("planes", wintypes.WORD), ("bits", wintypes.WORD), ("compression", wintypes.DWORD),
                    ("image_size", wintypes.DWORD), ("xppm", wintypes.LONG), ("yppm", wintypes.LONG),
                    ("used", wintypes.DWORD), ("important", wintypes.DWORD), ("colors", wintypes.DWORD * 3)]

    user, gdi = ctypes.WinDLL("user32", use_last_error=True), ctypes.WinDLL("gdi32", use_last_error=True)
    handle = wintypes.HANDLE
    signatures = [
        (user.GetCursorInfo, [ctypes.POINTER(CursorInfo)], wintypes.BOOL),
        (user.CopyIcon, [handle], handle), (user.DestroyIcon, [handle], wintypes.BOOL),
        (user.GetIconInfo, [handle, ctypes.POINTER(IconInfo)], wintypes.BOOL),
        (user.MonitorFromPoint, [wintypes.POINT, wintypes.DWORD], handle),
        (user.GetMonitorInfoW, [handle, ctypes.POINTER(MonitorInfo)], wintypes.BOOL),
        (user.DrawIconEx, [handle, ctypes.c_int, ctypes.c_int, handle, ctypes.c_int, ctypes.c_int,
                           wintypes.UINT, handle, wintypes.UINT], wintypes.BOOL),
        (gdi.CreateCompatibleDC, [handle], handle), (gdi.DeleteDC, [handle], wintypes.BOOL),
        (gdi.CreateDIBSection, [handle, ctypes.POINTER(BitmapInfo), wintypes.UINT,
                               ctypes.POINTER(ctypes.c_void_p), handle, wintypes.DWORD], handle),
        (gdi.SelectObject, [handle, handle], handle), (gdi.DeleteObject, [handle], wintypes.BOOL),
        (gdi.GdiFlush, [], wintypes.BOOL),
    ]
    for function, arguments, result in signatures:
        function.argtypes, function.restype = arguments, result
    cursor = CursorInfo()
    cursor.size = ctypes.sizeof(cursor)
    if not user.GetCursorInfo(ctypes.byref(cursor)) or not cursor.flags & 1:
        return pixmap
    icon = user.CopyIcon(cursor.cursor)
    info, monitor = IconInfo(), MonitorInfo()
    dc = bitmap = previous = None
    try:
        monitor.size = ctypes.sizeof(monitor)
        if not icon or not user.GetIconInfo(icon, ctypes.byref(info)):
            raise OSError("Cannot read cursor")
        if not user.GetMonitorInfoW(user.MonitorFromPoint(cursor.pos, 2), ctypes.byref(monitor)):
            raise OSError("Cannot locate cursor monitor")
        source = pixmap.toImage().convertToFormat(QImage.Format.Format_RGB32)
        header = BitmapInfo()
        header.size, header.width, header.height = 40, source.width(), -source.height()
        header.planes, header.bits = 1, 32
        data = ctypes.c_void_p()
        dc = gdi.CreateCompatibleDC(None)
        bitmap = gdi.CreateDIBSection(dc, ctypes.byref(header), 0, ctypes.byref(data), None, 0)
        if not dc or not bitmap or not data.value:
            raise OSError("Cannot create cursor bitmap")
        previous = gdi.SelectObject(dc, bitmap)
        if not previous or previous == ctypes.c_void_p(-1).value:
            previous = None
            raise OSError("Cannot select cursor bitmap")
        ctypes.memmove(data, bytes(source.constBits()), source.sizeInBytes())
        x = cursor.pos.x - monitor.monitor.left - info.x
        y = cursor.pos.y - monitor.monitor.top - info.y
        if not user.DrawIconEx(dc, x, y, icon, 0, 0, 0, None, 3):
            raise OSError("Cannot draw cursor")
        gdi.GdiFlush()
        image = QImage(ctypes.string_at(data, source.sizeInBytes()), source.width(), source.height(),
                       source.bytesPerLine(), QImage.Format.Format_RGB32).copy()
        result = QPixmap.fromImage(image)
        result.setDevicePixelRatio(pixmap.devicePixelRatio())
        return result
    finally:
        if previous:
            gdi.SelectObject(dc, previous)
        for obj in (bitmap, info.mask, info.color):
            if obj:
                gdi.DeleteObject(obj)
        if dc:
            gdi.DeleteDC(dc)
        if icon:
            user.DestroyIcon(icon)


class ContrastCheckBox(QCheckBox):
    """Keep native checkbox interaction and draw a clear, scalable indicator."""
    def paintEvent(self, event):
        super().paintEvent(event)
        option = QStyleOptionButton()
        self.initStyleOption(option)
        rect = self.style().subElementRect(QStyle.SubElement.SE_CheckBoxIndicator, option, self)
        dark = self.palette().color(QPalette.ColorRole.Window).lightness() < 128
        border = "#9bbdb3" if dark else "#58796f"
        if option.state & QStyle.StateFlag.State_MouseOver:
            border = "#7ad7ba" if dark else "#0b7258"
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if not self.isEnabled():
            painter.setOpacity(0.5)
        painter.translate(rect.topLeft())
        painter.scale(rect.width() / 20, rect.height() / 20)
        painter.setPen(QPen(QColor("#118769" if self.isChecked() else border), 2))
        painter.setBrush(QColor("#118769") if self.isChecked()
                         else self.palette().color(QPalette.ColorRole.Base))
        painter.drawRoundedRect(QRectF(1, 1, 18, 18), 4, 4)
        if self.isChecked():
            painter.setPen(QPen(QColor("white"), 2.3, Qt.PenStyle.SolidLine,
                                Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            tick = QPainterPath(QPointF(5, 10))
            tick.lineTo(8.5, 13.5)
            tick.lineTo(15, 6.5)
            painter.drawPath(tick)
        painter.end()


class ChoiceBox(QComboBox):
    """A consistent vector chevron in both themes, without extra image files."""
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QPen(self.palette().color(QPalette.ColorRole.Text), 1.5))
        x, y = self.width() - 15, self.height() // 2
        painter.drawLine(x - 4, y - 2, x, y + 2)
        painter.drawLine(x, y + 2, x + 4, y - 2)
        painter.end()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("LumaShot", "LumaShot")
        self.theme = self.settings.value("theme", "light")
        if self.theme not in ("light", "dark"):
            self.theme = "light"
        apply_theme(self.theme)
        self.lang = self.settings.value("language", "ro")
        if self.lang not in LANGUAGES:
            self.lang = "ro"
        pictures = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.PicturesLocation)
        self.folder = self.settings.value("folder", str(Path(pictures) / "LumaShot"))
        self.overlays = []
        self.capture_pending = False
        self.capture_mode = "region"
        self.restore_window = True
        self.quitting = False
        self.setWindowTitle("LumaShot")
        self.setWindowIcon(app_icon())
        self.setMinimumSize(780, 640)
        self.resize(860, 700)
        self.hotkeys = Hotkeys(self.hotkey_capture, self.settings.value("capture_hotkey", ""),
                               enabled=self.option("capture_hotkey_enabled", True))
        self.full_hotkeys = Hotkeys(lambda: self.hotkey_capture("full"),
                                   self.settings.value("full_hotkey", "Ctrl+Shift+F10"),
                                   id_base=0x5B70, defaults=False,
                                   enabled=self.option("full_hotkey_enabled", False))
        QApplication.instance().installNativeEventFilter(self.hotkeys)
        QApplication.instance().installNativeEventFilter(self.full_hotkeys)
        self.tray = QSystemTrayIcon(self.windowIcon(), self)
        self.tray.setToolTip("LumaShot")
        self.tray.activated.connect(self.tray_activated)
        self.rebuild_ui()
        self.rebuild_tray()
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray.show()

    def t(self, message_key, **values):
        return tr(self.lang, message_key, **values)

    def label(self, key, name="", wrap=False):
        label = QLabel(self.t(key))
        if name:
            label.setObjectName(name)
        label.setWordWrap(wrap)
        return label

    def rebuild_ui(self):
        previous_tab = self.tabs.currentIndex() if hasattr(self, "tabs") else 0
        old = self.takeCentralWidget()
        if old:
            old.deleteLater()
        root = QWidget()
        root.setObjectName("root")
        layout = QVBoxLayout(root)
        layout.setContentsMargins(28, 22, 28, 22)
        layout.setSpacing(18)
        header = QHBoxLayout()
        icon = QLabel()
        icon.setPixmap(self.windowIcon().pixmap(36, 36))
        header.addWidget(icon)
        brand = QLabel("LumaShot")
        brand.setObjectName("brand")
        header.addWidget(brand)
        header.addStretch()
        layout.addLayout(header)
        hero = QFrame()
        hero.setObjectName("card")
        hero_layout = QVBoxLayout(hero)
        hero_layout.setContentsMargins(24, 20, 24, 20)
        hero_layout.setSpacing(12)
        hero_layout.addWidget(self.label("tagline", "headline", True))
        row = QHBoxLayout()
        self.capture_button = QPushButton(self.t("capture"))
        self.capture_button.setIcon(ui_icon("capture", "#ffffff"))
        self.capture_button.setIconSize(QSize(22, 22))
        self.capture_button.setObjectName("primary")
        self.capture_button.setMinimumHeight(56)
        self.capture_button.clicked.connect(lambda: self.start_capture())
        row.addWidget(self.capture_button)
        self.full_button = QPushButton(self.t("full_capture"))
        self.full_button.setIcon(ui_icon("monitor", self.icon_color))
        self.full_button.setIconSize(QSize(22, 22))
        self.full_button.setMinimumHeight(56)
        self.full_button.clicked.connect(lambda: self.start_capture("full"))
        row.addWidget(self.full_button)
        row.addStretch()
        hero_layout.addLayout(row)
        hero_layout.addWidget(self.label("screen_note", "muted", True))
        layout.addWidget(hero)

        self.tabs = QTabWidget()
        self.tabs.setAccessibleName(self.t("settings"))
        general = QWidget()
        form = QFormLayout(general)
        form.setContentsMargins(20, 18, 20, 18)
        form.setSpacing(12)
        language = ChoiceBox()
        language.setAccessibleName(self.t("language"))
        language.setToolTip(wrapped_tip(self.t("tip_language")))
        for code, name in LANGUAGES.items():
            language.addItem(name, code)
        language.setCurrentIndex(list(LANGUAGES).index(self.lang))
        language.currentIndexChanged.connect(lambda index: self.change_language(language.itemData(index)))
        form.addRow(self.t("language"), language)
        self.theme_combo = ChoiceBox()
        self.theme_combo.setAccessibleName(self.t("theme"))
        self.theme_combo.setToolTip(wrapped_tip(self.t("tip_theme")))
        for theme in ("light", "dark"):
            self.theme_combo.addItem(self.t(theme), theme)
        self.theme_combo.setCurrentIndex(0 if self.theme == "light" else 1)
        self.theme_combo.currentIndexChanged.connect(
            lambda index: self.change_theme(self.theme_combo.itemData(index)))
        form.addRow(self.t("theme"), self.theme_combo)
        for key, default in (("notifications", True), ("remember_area", False), ("include_cursor", False)):
            checkbox = ContrastCheckBox(self.t(key))
            checkbox.setToolTip(wrapped_tip(self.t("tip_" + key)))
            checkbox.setChecked(self.option(key, default))
            checkbox.toggled.connect(lambda checked, k=key: self.settings.setValue(k, checked))
            form.addRow(checkbox)
        folder_row = QHBoxLayout()
        self.folder_label = QLabel(self.folder)
        self.folder_label.setObjectName("muted")
        self.folder_label.setWordWrap(True)
        self.folder_label.setToolTip(self.folder)
        folder_row.addWidget(self.folder_label, 1)
        choose = QPushButton(self.t("browse"))
        choose.setToolTip(self.t("choose_folder"))
        choose.setIcon(ui_icon("folder", self.icon_color))
        choose.clicked.connect(self.choose_folder)
        folder_row.addWidget(choose)
        form.addRow(self.t("folder"), folder_row)
        self.tabs.addTab(general, self.t("general"))

        shortcuts = QWidget()
        shortcut_layout = QVBoxLayout(shortcuts)
        shortcut_layout.setContentsMargins(20, 18, 20, 18)
        shortcut_layout.setSpacing(12)
        for full in (False, True):
            prefix = "full" if full else "capture"
            key = "full_hotkey" if full else "hotkey_label"
            row = QHBoxLayout()
            enabled = ContrastCheckBox(self.t(key))
            enabled.setToolTip(wrapped_tip(self.t("tip_enable_hotkey")))
            enabled.setChecked(self.option(prefix + "_hotkey_enabled", not full))
            row.addWidget(enabled, 1)
            editor = QKeySequenceEdit()
            editor.setMaximumSequenceLength(1)
            editor.setKeySequence(QKeySequence(self.settings.value(prefix + "_hotkey", "Ctrl+Shift+F10" if full else "Ctrl+Shift+F9")))
            editor.setAccessibleName(self.t(key))
            editor.setToolTip(wrapped_tip(self.t("tip_hotkey")))
            editor.setFixedWidth(200)
            editor.setEnabled(enabled.isChecked())
            enabled.toggled.connect(editor.setEnabled)
            row.addWidget(editor)
            apply_button = QPushButton(self.t("apply"))
            apply_button.setToolTip(wrapped_tip(self.t("tip_apply")))
            apply_button.setIcon(ui_icon("save", self.icon_color))
            apply_button.clicked.connect(lambda checked=False, f=full: self.apply_hotkey(f))
            row.addWidget(apply_button)
            status = QLabel()
            status.setObjectName("muted")
            status.setWordWrap(True)
            if full:
                self.full_hotkey_editor, self.full_hotkey_enabled = editor, enabled
                self.full_shortcuts = status
            else:
                self.hotkey_editor, self.hotkey_enabled = editor, enabled
                self.shortcuts = status
            shortcut_layout.addLayout(row)
            shortcut_layout.addWidget(status)
        shortcut_layout.addStretch()
        self.tabs.addTab(shortcuts, self.t("hotkeys"))

        formats = QWidget()
        formats_form = QFormLayout(formats)
        formats_form.setContentsMargins(20, 18, 20, 18)
        formats_form.setSpacing(18)
        self.format_combo = ChoiceBox()
        self.format_combo.addItems(["PNG", "JPEG"])
        self.format_combo.setCurrentText(self.save_format())
        self.format_combo.setAccessibleName(self.t("default_format"))
        self.format_combo.setToolTip(wrapped_tip(self.t("tip_format")))
        formats_form.addRow(self.t("default_format"), self.format_combo)
        quality_row = QHBoxLayout()
        self.quality_slider = QSlider(Qt.Orientation.Horizontal)
        self.quality_slider.setRange(1, 100)
        self.quality_spin = QSpinBox()
        self.quality_spin.setFixedWidth(100)
        self.quality_spin.setRange(1, 100)
        self.quality_spin.setSuffix(" %")
        for control in (self.quality_slider, self.quality_spin):
            control.setValue(self.jpeg_quality())
            control.setAccessibleName(self.t("jpeg_quality"))
            control.setToolTip(wrapped_tip(self.t("tip_quality")))
            control.setEnabled(self.save_format() == "JPEG")
            quality_row.addWidget(control)
        self.quality_slider.valueChanged.connect(self.quality_spin.setValue)
        self.quality_spin.valueChanged.connect(self.quality_slider.setValue)
        self.quality_spin.valueChanged.connect(lambda value: self.settings.setValue("jpeg_quality", value))
        self.format_combo.currentTextChanged.connect(self.change_format)
        quality_label = self.label("jpeg_quality")
        quality_label.setToolTip(wrapped_tip(self.t("tip_quality")))
        formats_form.addRow(quality_label, quality_row)
        action = ChoiceBox()
        action.setAccessibleName(self.t("full_action"))
        action.setToolTip(wrapped_tip(self.t("tip_full_action")))
        action.addItem(self.t("edit_first"), "edit")
        action.addItem(self.t("save_instant"), "save")
        action.setCurrentIndex(1 if self.settings.value("full_action", "edit") == "save" else 0)
        action.currentIndexChanged.connect(lambda index: self.change_full_action(action.itemData(index)))
        formats_form.addRow(self.t("full_action"), action)
        self.tabs.addTab(formats, self.t("formats"))
        for index, key in enumerate(("tip_general_tab", "tip_shortcuts_tab", "tip_format_tab")):
            self.tabs.setTabToolTip(index, wrapped_tip(self.t(key)))
        self.tabs.setCurrentIndex(previous_tab)
        layout.addWidget(self.tabs, 1)
        layout.addWidget(self.label("settings_saved", "muted", True))
        self.setCentralWidget(root)
        self.refresh_shortcuts()

    @property
    def icon_color(self):
        return theme_colors(self.theme)["fg"]

    def option(self, key, default=False):
        return self.settings.value(key, default, type=bool)

    def save_format(self):
        return "JPEG" if self.settings.value("save_format", "PNG") == "JPEG" else "PNG"

    def jpeg_quality(self):
        try:
            return max(1, min(100, int(self.settings.value("jpeg_quality", 95))))
        except (TypeError, ValueError):
            return 95

    def change_format(self, value):
        self.settings.setValue("save_format", value)
        self.quality_slider.setEnabled(value == "JPEG")
        self.quality_spin.setEnabled(value == "JPEG")

    def change_full_action(self, value):
        self.settings.setValue("full_action", value)
        self.refresh_shortcuts()

    def change_theme(self, theme):
        if theme == self.theme or theme not in ("light", "dark"):
            return
        self.theme = theme
        self.settings.setValue("theme", theme)
        apply_theme(theme)
        QTimer.singleShot(0, self.rebuild_ui)
        QTimer.singleShot(0, self.rebuild_tray)

    def refresh_shortcuts(self):
        for full in (False, True):
            controller = self.full_hotkeys if full else self.hotkeys
            status = self.full_shortcuts if full else self.shortcuts
            prefix = "full" if full else "capture"
            enabled = self.option(prefix + "_hotkey_enabled", not full)
            labels = [label for _, label in controller.registered]
            text = " · ".join(labels) if labels else self.t("shortcut_unavailable" if enabled else "button_only")
            editor = self.full_hotkey_editor if full else self.hotkey_editor
            extra = [label for label in labels if label != editor.keySequence().toString(QKeySequence.SequenceFormat.PortableText)]
            status.setText(" · ".join(extra) if labels else text)
            status.setVisible(not labels or bool(extra))
            description = self.t("tip_area") if not full else self.t(
                "tip_full_save" if self.settings.value("full_action", "edit") == "save" else "tip_full_edit")
            if labels:
                description += "\n" + " · ".join(labels)
            (self.full_button if full else self.capture_button).setToolTip(wrapped_tip(description))
            editor.setToolTip(wrapped_tip(self.t("tip_hotkey") + "\n" + text))

    def rebuild_tray(self):
        self.tray.setToolTip(self.t("tip_tray"))
        old_menu = self.tray.contextMenu()
        menu = QMenu(self)
        menu.setToolTipsVisible(True)
        for key, callback in [("capture", lambda: self.start_capture()),
                              ("open", self.show_main), ("quit", self.quit_app)]:
            action = QAction(ui_icon(key, self.icon_color), self.t(key), menu)
            action.setToolTip(wrapped_tip(self.t("tip_area") if key == "capture" else self.t(key)))
            action.triggered.connect(callback)
            menu.addAction(action)
        self.tray.setContextMenu(menu)
        if old_menu:
            old_menu.deleteLater()

    def hotkey_capture(self, mode="region"):
        focus = QApplication.focusWidget()
        for editor in (self.hotkey_editor, self.full_hotkey_editor):
            if focus and (focus is editor or editor.isAncestorOf(focus)):
                return
        self.start_capture(mode)

    def apply_hotkey(self, full=False):
        controller = self.full_hotkeys if full else self.hotkeys
        editor = self.full_hotkey_editor if full else self.hotkey_editor
        checkbox = self.full_hotkey_enabled if full else self.hotkey_enabled
        prefix = "full" if full else "capture"
        if not checkbox.isChecked():
            controller.close()
            self.settings.setValue(prefix + "_hotkey_enabled", False)
            self.refresh_shortcuts()
            return
        sequence = editor.keySequence()
        try:
            other = self.hotkeys if full else self.full_hotkeys
            binding = native_hotkey(sequence)
            accepted = binding not in other.bindings.values() and controller.replace(sequence)
        except ValueError:
            QMessageBox.warning(self, self.t("error"), self.t("hotkey_invalid"))
            return
        if not accepted:
            QMessageBox.warning(self, self.t("error"), self.t("hotkey_busy"))
            return
        label = sequence.toString(QKeySequence.SequenceFormat.PortableText)
        self.settings.setValue(prefix + "_hotkey", label)
        self.settings.setValue(prefix + "_hotkey_enabled", True)
        self.refresh_shortcuts()

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
            self.folder_label.setToolTip(folder)

    def show_main(self):
        if self.overlays or self.capture_pending:
            return
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.start_capture()

    def start_capture(self, mode="region"):
        if self.overlays or self.capture_pending:
            return
        self.capture_mode = mode
        self.capture_pending = True
        self.restore_window = self.isVisible()
        self.capture_button.setEnabled(False)
        self.full_button.setEnabled(False)
        QToolTip.hideText()
        # Dismiss our tooltip windows before grabbing pixels, including any fade delay.
        for widget in QApplication.topLevelWidgets():
            if widget.windowType() == Qt.WindowType.ToolTip:
                widget.hide()
        self.hide()
        # Let Windows finish removing the main window and tray menu.
        QTimer.singleShot(260, self.capture_screens)

    def capture_screens(self):
        try:
            under_cursor = QApplication.screenAt(QCursor.pos()) or QApplication.primaryScreen()
            screens = [under_cursor] if self.capture_mode == "full" else QApplication.screens()
            shots = [(screen, screen.grabWindow(0)) for screen in screens if screen]
            if not shots or any(pix.isNull() for _, pix in shots):
                raise RuntimeError("Screen capture returned no image")
            if self.option("include_cursor"):
                shots = [(screen, capture_cursor(pix) if screen == under_cursor else pix)
                         for screen, pix in shots]
            if self.capture_mode == "full" and self.settings.value("full_action", "edit") == "save":
                self.save_immediately(shots[0][1].toImage())
                return
            for screen, pix in shots:
                overlay = CaptureOverlay(screen, pix, self.lang, self.theme)
                if self.capture_mode == "full":
                    overlay.selection = QRectF(overlay.rect())
                elif self.option("remember_area"):
                    saved = self.settings.value("last_area", {})
                    if isinstance(saved, dict) and saved.get("screen") == overlay.screen_key:
                        values = saved.get("rect", [])
                        if isinstance(values, list) and len(values) == 4:
                            try:
                                rect = QRectF(*map(float, values)).intersected(QRectF(overlay.rect()))
                                if rect.width() >= 5 and rect.height() >= 5:
                                    overlay.selection = rect
                            except (ValueError, TypeError):
                                pass
                if not overlay.selection.isEmpty():
                    overlay.position_panel()
                overlay.chosen.connect(self.choose_overlay)
                overlay.finished.connect(self.finish_capture)
                self.overlays.append(overlay)
            # Grab all images first, then display the overlays.
            for overlay in self.overlays:
                overlay.show()
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
            self.full_button.setEnabled(True)

    def screenshot_path(self):
        Path(self.folder).mkdir(parents=True, exist_ok=True)
        extension = ".jpg" if self.save_format() == "JPEG" else ".png"
        return str(Path(self.folder) / ("LumaShot_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f") + extension))

    def notify_result(self, message):
        if self.option("notifications", True) and self.tray.isVisible():
            self.tray.showMessage("LumaShot", message, QSystemTrayIcon.MessageIcon.Information, 2000)

    def save_immediately(self, image):
        try:
            filename = self.screenshot_path()
            if not image.save(filename, self.save_format(), self.jpeg_quality()):
                raise OSError("QImage.save returned false")
            self.notify_result(self.t("saved", path=filename))
        except (OSError, ValueError):
            self.show()
            QMessageBox.warning(self, self.t("error"), self.t("save_error"))
        finally:
            if self.restore_window:
                self.show()

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
        selected = self.sender()
        if not isinstance(selected, CaptureOverlay):
            selected = next((w for w in self.overlays if w.isVisible() and not w.selection.isEmpty()), None)
        if action == "save":
            # Keep the editor intact if the save dialog is cancelled or fails.
            editor = next((w for w in self.overlays if w.isVisible()), None)
            for overlay in self.overlays:
                overlay.hide()
            try:
                filename = self.screenshot_path()
                filters = self.t("format").split(";;")
                if self.save_format() == "JPEG":
                    filters.reverse()
                path, file_filter = QFileDialog.getSaveFileName(
                    self, self.t("save_title"), filename, ";;".join(filters))
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
                if not image.save(path, fmt, self.jpeg_quality()):
                    raise OSError("QImage.save returned false")
                self.folder = str(Path(path).parent)
                self.settings.setValue("folder", self.folder)
                self.folder_label.setText(self.folder)
                self.folder_label.setToolTip(self.folder)
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
        if self.capture_mode == "region" and action in ("save", "copy") and self.option("remember_area"):
            if selected:
                r = selected.selection
                self.settings.setValue("last_area", {"screen": selected.screen_key,
                    "rect": [r.x(), r.y(), r.width(), r.height()]})
        self.close_overlays()
        if self.restore_window:
            self.show_main()
        if action != "cancel":
            self.notify_result(message)

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
        self.full_hotkeys.close()
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
    app.aboutToQuit.connect(window.full_hotkeys.close)
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
