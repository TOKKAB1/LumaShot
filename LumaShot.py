# Original LumaShot code and artwork: MIT. Bundled icons retain their own notices.
LUMASHOT_LICENSE = 'MIT License\n\nCopyright (c) 2026 TOKKAB1\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n'

# LumaShot 5.0.0 — Python + PySide6. Run: python LumaShot.py
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
        "colors": ["Mov", "Roșu", "Portocaliu", "Chihlimbar", "Galben", "Verde lime",
                   "Verde", "Smarald", "Verde petrol", "Turcoaz", "Albastru deschis", "Albastru",
                   "Indigo", "Violet", "Roz", "Roz închis", "Maro", "Maro închis",
                   "Alb", "Gri deschis", "Gri", "Gri închis", "Antracit", "Negru"],
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
        "colors": ["Сиреневый", "Красный", "Оранжевый", "Янтарный", "Жёлтый", "Лаймовый",
                   "Зелёный", "Изумрудный", "Нефритовый", "Бирюзовый", "Голубой", "Синий",
                   "Индиго", "Фиолетовый", "Розовый", "Малиновый", "Коричневый", "Тёмно-коричневый",
                   "Белый", "Светло-серый", "Серый", "Тёмно-серый", "Антрацитовый", "Чёрный"],
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
        "colors": ["Lavender", "Red", "Orange", "Amber", "Yellow", "Lime",
                   "Green", "Emerald", "Petrol green", "Cyan", "Sky blue", "Blue",
                   "Indigo", "Violet", "Pink", "Rose", "Brown", "Dark brown",
                   "White", "Light gray", "Gray", "Dark gray", "Charcoal", "Black"],
    },
}


STRINGS["ro"].update({
    "hotkey_label": "Scurtătură pentru captură", "hotkey_hint": "Apasă combinația dorită",
    "apply": "Aplică", "hotkey_invalid": "Alege o singură combinație cu Ctrl, Alt sau Shift, o tastă F sau Print Screen.",
    "hotkey_busy": "Combinația este ocupată sau rezervată de Windows. Scurtătura anterioară rămâne activă.",
    "hotkey_saved": "Scurtătură activă: {key}",
})
STRINGS["ru"].update({
    "hotkey_label": "Сочетание для снимка", "hotkey_hint": "Нажмите нужное сочетание",
    "apply": "Применить", "hotkey_invalid": "Выберите одно сочетание с Ctrl, Alt или Shift, клавишу F или Print Screen.",
    "hotkey_busy": "Сочетание занято или зарезервировано Windows. Предыдущее сочетание остаётся активным.",
    "hotkey_saved": "Активное сочетание: {key}",
})
STRINGS["en"].update({
    "hotkey_label": "Capture shortcut", "hotkey_hint": "Press your preferred shortcut",
    "apply": "Apply", "hotkey_invalid": "Choose one combination with Ctrl, Alt or Shift, an F key, or Print Screen.",
    "hotkey_busy": "This shortcut is in use or reserved by Windows. The previous shortcut remains active.",
    "hotkey_saved": "Active shortcut: {key}",
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
from copy import deepcopy
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
    font_size: float = 0
    text_scale_x: float = 1
    number_radius: float = 0


class History:
    def __init__(self):
        self.items = []
        self.past = []
        self.future = []

    def add(self, mark):
        self.past.append((len(self.items), None, deepcopy(mark)))
        self.items.append(mark)
        self.future.clear()

    def replace(self, index, mark):
        before = deepcopy(self.items[index])
        self.items[index] = deepcopy(mark)
        self.record_edit(index, before)

    def record_edit(self, index, before):
        after = self.items[index]
        if before != after:
            self.past.append((index, deepcopy(before), deepcopy(after)))
            self.future.clear()

    def remove(self, index):
        self.past.append((index, deepcopy(self.items.pop(index)), None))
        self.future.clear()

    def apply(self, command, reverse=False):
        index, before, after = command
        if reverse:
            before, after = after, before
        if after is None:
            self.items.pop(index)
        elif before is None:
            self.items.insert(index, deepcopy(after))
        else:
            self.items[index] = deepcopy(after)

    def undo(self):
        if self.past:
            command = self.past.pop()
            self.apply(command, reverse=True)
            self.future.append(command)

    def redo(self):
        if self.future:
            command = self.future.pop()
            self.apply(command)
            self.past.append(command)


def text_font(mark):
    font = QFont("Segoe UI")
    font.setPixelSize(max(6, round(mark.font_size or (16 + mark.width*2))))
    return font


def mark_bounds(mark):
    from PySide6.QtGui import QFontMetricsF
    if mark.kind == "text":
        r = QFontMetricsF(text_font(mark)).boundingRect(mark.text or " ")
        return QRectF(mark.start.x()+r.x()*mark.text_scale_x, mark.start.y()+r.y(),
                      max(1, r.width()*mark.text_scale_x), max(1, r.height()))
    if mark.kind == "number":
        radius = mark.number_radius or 13+mark.width
        return QRectF(mark.start.x()-radius, mark.start.y()-radius, radius*2, radius*2)
    points = [mark.start, mark.end, *mark.points]
    left, top = min(p.x() for p in points), min(p.y() for p in points)
    return QRectF(left, top, max(1, max(p.x() for p in points)-left),
                  max(1, max(p.y() for p in points)-top))


def rect_handles(rect):
    return {"tl": rect.topLeft(), "tr": rect.topRight(), "bl": rect.bottomLeft(), "br": rect.bottomRight(),
            "t": QPointF(rect.center().x(), rect.top()), "b": QPointF(rect.center().x(), rect.bottom()),
            "l": QPointF(rect.left(), rect.center().y()), "r": QPointF(rect.right(), rect.center().y())}


def segment_distance(point, start, end):
    delta = end-start
    length = delta.x()**2+delta.y()**2
    fraction = max(0, min(1, ((point.x()-start.x())*delta.x()+(point.y()-start.y())*delta.y())/length)) if length else 0
    nearest = start+delta*fraction
    return math.hypot(point.x()-nearest.x(), point.y()-nearest.y())


def mark_hit(mark, point):
    tolerance = max(6, mark.width/2+3)
    bounds = mark_bounds(mark)
    if mark.kind in ("text", "highlight", "mask"):
        return bounds.adjusted(-4, -4, 4, 4).contains(point)
    if mark.kind == "number":
        return math.hypot(point.x()-mark.start.x(), point.y()-mark.start.y()) <= bounds.width()/2+tolerance
    if mark.kind in ("line", "arrow", "pen"):
        points = [mark.start, *(mark.points if mark.kind == "pen" else []), mark.end]
        if any(segment_distance(point, a, b) <= tolerance for a, b in zip(points, points[1:])):
            return True
        if mark.kind == "arrow":
            angle = math.atan2(mark.end.y()-mark.start.y(), mark.end.x()-mark.start.x())
            for offset in (-.48, .48):
                tip = mark.end-QPointF(math.cos(angle+offset), math.sin(angle+offset))*max(12, mark.width*4)
                if segment_distance(point, mark.end, tip) <= tolerance:
                    return True
        return False
    return bounds.adjusted(-tolerance, -tolerance, tolerance, tolerance).contains(point) and not bounds.adjusted(tolerance, tolerance, -tolerance, -tolerance).contains(point)


def resize_mark(mark, target):
    result = deepcopy(mark)
    old = mark_bounds(mark)
    sx, sy = target.width()/old.width(), target.height()/old.height()
    def mapped(point):
        return QPointF(target.left()+(point.x()-old.left())*sx, target.top()+(point.y()-old.top())*sy)
    result.start, result.end = mapped(mark.start), mapped(mark.end)
    result.points = [mapped(point) for point in mark.points]
    if mark.kind == "text":
        result.font_size = max(6, min(512, (mark.font_size or 16+mark.width*2)*sy))
        actual_sy = result.font_size/(mark.font_size or 16+mark.width*2)
        result.text_scale_x = max(.05, min(20, mark.text_scale_x*sx/actual_sy))
    elif mark.kind == "number":
        result.number_radius = max(6, min(target.width(), target.height())/2)
        result.font_size = 16*result.number_radius/(13+mark.width)
    return result


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
        painter.setFont(text_font(mark))
        painter.translate(mark.start)
        painter.scale(mark.text_scale_x, 1)
        painter.drawText(QPointF(), mark.text)
    elif mark.kind == "number":
        radius = mark.number_radius or 13 + mark.width
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(mark.start, radius, radius)
        painter.setPen(QColor("#ffffff") if color.lightness() < 180 else QColor("#111118"))
        font = QFont("Segoe UI", weight=QFont.Weight.Bold)
        font.setPixelSize(max(6, round(mark.font_size or 16)))
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
    QPushButton, QSpinBox, QWidget, QGridLayout,
)


# Official Lucide icons, pinned to c29c276f16590cf017126671535ad8c792be64d8.
# https://github.com/lucide-icons/lucide — ISC / MIT notices retained below.
LUCIDE_LICENSE = 'ISC License\n\nCopyright (c) 2026 Lucide Icons and Contributors\n\nPermission to use, copy, modify, and/or distribute this software for any\npurpose with or without fee is hereby granted, provided that the above\ncopyright notice and this permission notice appear in all copies.\n\nTHE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES\nWITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF\nMERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR\nANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES\nWHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN\nACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF\nOR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.\n\n---\n\nThe following Lucide icons are derived from the Feather project:\n\nairplay, alert-circle, alert-octagon, alert-triangle, aperture, arrow-down-circle, arrow-down-left, arrow-down-right, arrow-down, arrow-left-circle, arrow-left, arrow-right-circle, arrow-right, arrow-up-circle, arrow-up-left, arrow-up-right, arrow-up, at-sign, calendar, cast, check, chevron-down, chevron-left, chevron-right, chevron-up, chevrons-down, chevrons-left, chevrons-right, chevrons-up, circle, clipboard, clock, code, columns, command, compass, corner-down-left, corner-down-right, corner-left-down, corner-left-up, corner-right-down, corner-right-up, corner-up-left, corner-up-right, crosshair, database, divide-circle, divide-square, dollar-sign, download, external-link, feather, frown, hash, headphones, help-circle, info, italic, key, layout, life-buoy, link-2, link, loader, lock, log-in, log-out, maximize, meh, minimize, minimize-2, minus-circle, minus-square, minus, monitor, moon, more-horizontal, more-vertical, move, music, navigation-2, navigation, octagon, pause-circle, percent, plus-circle, plus-square, plus, power, radio, rss, search, server, share, shopping-bag, sidebar, smartphone, smile, square, table-2, tablet, target, terminal, trash-2, trash, triangle, tv, type, upload, x-circle, x-octagon, x-square, x, zoom-in, zoom-out\n\nThe MIT License (MIT) (for the icons listed above)\n\nCopyright (c) 2013-present Cole Bemis\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n'
LUCIDE_SVGS = {
    'circle-dot': '<svg\n  xmlns="http://www.w3.org/2000/svg"\n  width="24"\n  height="24"\n  viewBox="0 0 24 24"\n  fill="none"\n  stroke="currentColor"\n  stroke-width="2"\n  stroke-linecap="round"\n  stroke-linejoin="round"\n>\n  <circle cx="12" cy="12" r="1" />\n  <circle cx="12" cy="12" r="10" />\n</svg>\n',
    'volume-x': '<svg\n  xmlns="http://www.w3.org/2000/svg"\n  width="24"\n  height="24"\n  viewBox="0 0 24 24"\n  fill="none"\n  stroke="currentColor"\n  stroke-width="2"\n  stroke-linecap="round"\n  stroke-linejoin="round"\n>\n  <path d="M11 4.702a.7.7 0 0 0-1.203-.498L6.413 7.587A1.4 1.4 0 0 1 5.416 8H3a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2.416a1.4 1.4 0 0 1 .997.413l3.383 3.384A.7.7 0 0 0 11 19.298z" />\n  <path d="m16.5 14.5 5-5" />\n  <path d="m16.5 9.5 5 5" />\n</svg>\n',
    'volume-2': '<svg\n  xmlns="http://www.w3.org/2000/svg"\n  width="24"\n  height="24"\n  viewBox="0 0 24 24"\n  fill="none"\n  stroke="currentColor"\n  stroke-width="2"\n  stroke-linecap="round"\n  stroke-linejoin="round"\n>\n  <path d="M11 4.702a.705.705 0 0 0-1.203-.498L6.413 7.587A1.4 1.4 0 0 1 5.416 8H3a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2.416a1.4 1.4 0 0 1 .997.413l3.383 3.384A.705.705 0 0 0 11 19.298z" />\n  <path d="M16 9a5 5 0 0 1 0 6" />\n  <path d="M19.364 18.364a9 9 0 0 0 0-12.728" />\n</svg>\n',
    'mic-off': '<svg\n  xmlns="http://www.w3.org/2000/svg"\n  width="24"\n  height="24"\n  viewBox="0 0 24 24"\n  fill="none"\n  stroke="currentColor"\n  stroke-width="2"\n  stroke-linecap="round"\n  stroke-linejoin="round"\n>\n  <path d="M12 19v3" />\n  <path d="M15 9.34V5a3 3 0 0 0-5.68-1.33" />\n  <path d="M16.95 16.95A7 7 0 0 1 5 12v-2" />\n  <path d="M18.89 13.23A7 7 0 0 0 19 12v-2" />\n  <path d="m2 2 20 20" />\n  <path d="M9 9v3a3 3 0 0 0 5.12 2.12" />\n</svg>\n',
    'mic': '<svg\n  xmlns="http://www.w3.org/2000/svg"\n  width="24"\n  height="24"\n  viewBox="0 0 24 24"\n  fill="none"\n  stroke="currentColor"\n  stroke-width="2"\n  stroke-linecap="round"\n  stroke-linejoin="round"\n>\n  <path d="M12 19v3" />\n  <path d="M19 10v2a7 7 0 0 1-14 0v-2" />\n  <rect x="9" y="2" width="6" height="13" rx="3" />\n</svg>\n',
    "video": '<svg\n  xmlns="http://www.w3.org/2000/svg"\n  width="24"\n  height="24"\n  viewBox="0 0 24 24"\n  fill="none"\n  stroke="currentColor"\n  stroke-width="2"\n  stroke-linecap="round"\n  stroke-linejoin="round"\n>\n  <path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5" />\n  <rect x="2" y="6" width="14" height="12" rx="2" />\n</svg>\n',
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

# Simple original transport glyphs, using the same stroke style as the toolbar.
LUCIDE_SVGS.update({
    "ocr": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M7 3H3v4m14-4h4v4M3 17v4h4m14-4v4h-4M8 8h8m-4 0v8m-3 0h6"/></svg>',
    "pause": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/></svg>',
    "resume": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M7 4 20 12 7 20Z"/></svg>',
})


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
COLORS = [
    "#a78bfa", "#ef4444", "#f97316", "#f59e0b", "#facc15", "#a3e635",
    "#22c55e", "#10b981", "#118769", "#06b6d4", "#38bdf8", "#2563eb",
    "#4f46e5", "#9333ea", "#ec4899", "#be185d", "#a16207", "#713f12",
    "#ffffff", "#e5e7eb", "#9ca3af", "#4b5563", "#1f2937", "#111118",
]
PANEL_STYLE = """
QFrame#tools { background: #f2f2f7; border: 1px solid #b7b5c2; border-radius: 4px; }
QPushButton { color: #353341; background: transparent; border: none;
              border-radius: 3px; padding: 0; min-height: 0; }
QPushButton:hover { background: #dedce8; }
QPushButton:checked { background: #dcefe8; }
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
        self.tool = "move"
        self.color = COLORS[1]
        self.stroke = 3
        self.editor = None
        self.editing_text_index = None
        self.ocr_dialog = None
        self.selected_mark = None
        self.shift_pressed = False
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

    def resizeEvent(self, event):
        if hasattr(self, "native_bounds") and self.width():
            self.scale = self.native_bounds.width() / self.width()
        super().resizeEvent(event)

    def tool_button(self, key, callback, checkable=False):
        button = QPushButton()
        button.setFixedSize(26, 26)
        button.setStyleSheet("QPushButton { min-height:26px; max-height:26px; padding:0; }")
        button.setIcon(ui_icon(key, theme_colors(self.theme)["fg"]))
        button.setIconSize(QSize(18, 18))
        shortcut = {"copy": "Ctrl+C", "save": "Ctrl+S", "cancel": "Esc"}.get(key)
        tip = self.t(key) + ("\n" + shortcut if shortcut else "")
        if key == "ocr":
            tip += "\n" + self.t("tip_ocr")
        if key == "move":
            tip += "\n" + self.t("object_hint")
        button.setToolTip(wrapped_tip(tip))
        button.setToolTipDuration(12000)
        button.setAccessibleName(self.t(key))
        button.setCheckable(checkable)
        button.setAutoDefault(False)
        button.setDefault(False)
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
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.clicked.connect(lambda checked=False, c=color: self.choose_color(c))
            swatches.addWidget(button, index // 6, index % 6)
            self.color_buttons[color] = button
        palette_layout.addLayout(swatches)
        self.set_color(self.color)
        width_row = QHBoxLayout()
        width_row.addWidget(QLabel(self.t("width")))
        width = QSpinBox()
        self.stroke_spin = width
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
        self.ocr_button = self.tool_button("ocr", self.start_ocr)
        self.ocr_button.setObjectName("ocr")
        bottom.addWidget(self.ocr_button)
        for key in ("copy", "save", "cancel"):
            button = self.tool_button(key, lambda checked=False, k=key: self.complete(k))
            button.setObjectName(key)
            bottom.addWidget(button)
        frame.adjustSize()
        self.actions.adjustSize()
        return frame

    def set_color(self, color):
        self.color = color
        if self.current_mark() is not None and self.current_mark().color != color:
            mark = deepcopy(self.current_mark())
            mark.color = color
            self.history.replace(self.selected_mark, mark)
            self.update()
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
        if self.current_mark() is not None and self.current_mark().width != value:
            mark = deepcopy(self.current_mark())
            mark.width = value
            if mark.kind == "text":
                mark.font_size = 0
            self.history.replace(self.selected_mark, mark)
            self.update()

    def set_tool(self, tool):
        if tool not in self.tool_buttons:
            return
        self.commit_text()
        self.palette.hide()
        self.tool = tool
        self.selected_mark = None
        for key, button in self.tool_buttons.items():
            button.setChecked(key == tool)
        self.setFocus()
        self.update()

    def undo(self):
        self.commit_text()
        self.history.undo()
        self.selected_mark = None
        self.update()

    def redo(self):
        self.history.redo()
        self.selected_mark = None
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
            for index, mark in enumerate(self.history.items):
                if self.editor and index == self.editing_text_index:
                    continue
                paint_mark(p, mark)
            if self.active_mark:
                paint_mark(p, self.active_mark)
            p.restore()
            p.setPen(QPen(QColor("#67cfb1"), 1, Qt.PenStyle.DashLine))
            p.setBrush(Qt.BrushStyle.NoBrush)
            p.drawRect(self.selection)
            if (self.tool == "move" and not self.shift_pressed and self.current_mark() is None) or not self.history.items:
                p.setBrush(QColor("#ffffff"))
                p.setPen(QColor("#118769"))
                for pt in self.handles().values():
                    p.drawRect(QRectF(pt.x()-3, pt.y()-3, 6, 6))
            if self.tool == "move" and self.current_mark() is not None:
                p.setPen(QPen(QColor("#f2bb53" if self.theme == "dark" else "#9a6309"), 1, Qt.PenStyle.DashLine))
                p.setBrush(Qt.BrushStyle.NoBrush)
                p.drawRect(mark_bounds(self.current_mark()))
                p.setBrush(QColor("white"))
                for point in self.object_handles().values():
                    p.drawRect(QRectF(point.x()-4, point.y()-4, 8, 8))
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
                "bl": r.bottomLeft(), "br": r.bottomRight(),
                "t": QPointF(r.center().x(), r.top()),
                "r": QPointF(r.right(), r.center().y()),
                "b": QPointF(r.center().x(), r.bottom()),
                "l": QPointF(r.left(), r.center().y())}

    def handle_at(self, pos):
        if self.selection.isEmpty():
            return None
        key, point = min(self.handles().items(), key=lambda item: (item[1]-pos).manhattanLength())
        return key if (point-pos).manhattanLength() <= 14 else None

    def bounded(self, point):
        return QPointF(max(0, min(point.x(), self.width())),
                       max(0, min(point.y(), self.height())))

    def current_mark(self):
        if self.selected_mark is not None and 0 <= self.selected_mark < len(self.history.items):
            return self.history.items[self.selected_mark]
        return None

    def object_handles(self):
        mark = self.current_mark()
        if mark is None:
            return {}
        return {"start": mark.start, "end": mark.end} if mark.kind in ("line", "arrow") else rect_handles(mark_bounds(mark))

    def object_handle_at(self, pos):
        handles = self.object_handles()
        if not handles:
            return None
        key, point = min(handles.items(), key=lambda item: (item[1]-pos).manhattanLength())
        mark = self.current_mark()
        bounds = mark_bounds(mark)
        tolerance = 10 if mark.kind in ("line", "arrow") else max(4, min(8, bounds.width()/3, bounds.height()/3))
        return key if (point-pos).manhattanLength() <= tolerance else None

    def object_at(self, pos):
        if not self.selection.contains(pos):
            return None
        return next((index for index in reversed(range(len(self.history.items)))
                     if mark_hit(self.history.items[index], pos)), None)

    def begin_object_drag(self, pos):
        handle = self.object_handle_at(pos)
        if handle is None:
            self.selected_mark = self.object_at(pos)
        if self.current_mark() is not None:
            self.set_color(self.current_mark().color)
            self.stroke = self.current_mark().width
            self.stroke_spin.blockSignals(True)
            self.stroke_spin.setValue(self.stroke)
            self.stroke_spin.blockSignals(False)
            self.object_original = deepcopy(self.current_mark())
            self.object_drag_handle = handle
            self.drag_mode = "object"
            self.hide_panels()
        self.update()

    def drag_object(self, pos):
        mark = self.object_original
        handle = self.object_drag_handle
        pos = QPointF(max(self.selection.left(), min(pos.x(), self.selection.right())),
                      max(self.selection.top(), min(pos.y(), self.selection.bottom())))
        if handle is None:
            delta = pos-self.origin
            bounds = mark_bounds(mark)
            dx = max(self.selection.left()-bounds.left(), min(delta.x(), self.selection.right()-bounds.right()))
            dy = max(self.selection.top()-bounds.top(), min(delta.y(), self.selection.bottom()-bounds.bottom()))
            delta = QPointF(dx, dy)
            result = deepcopy(mark)
            result.start += delta
            result.end += delta
            result.points = [point+delta for point in mark.points]
        elif handle in ("start", "end"):
            result = deepcopy(mark)
            setattr(result, handle, pos)
        else:
            target = mark_bounds(mark)
            if "l" in handle:
                target.setLeft(min(pos.x(), target.right()-3))
            if "r" in handle:
                target.setRight(max(pos.x(), target.left()+3))
            if "t" in handle:
                target.setTop(min(pos.y(), target.bottom()-3))
            if "b" in handle:
                target.setBottom(max(pos.y(), target.top()+3))
            result = resize_mark(mark, target)
        self.history.items[self.selected_mark] = result

    def mouseDoubleClickEvent(self, event):
        if self.tool == "move" and event.modifiers() & Qt.KeyboardModifier.ShiftModifier:
            self.commit_text()
            index = self.object_at(event.position())
            if index is not None and self.history.items[index].kind == "text":
                self.selected_mark = index
                self.drag_mode = None
                self.begin_text(self.history.items[index].start, index)
                return
        super().mouseDoubleClickEvent(event)

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
        self.shift_pressed = bool(event.modifiers() & Qt.KeyboardModifier.ShiftModifier)
        if self.tool == "move" and self.shift_pressed and not self.selection.isEmpty():
            self.begin_object_drag(pos)
            return
        self.selected_mark = None
        if self.selection.isEmpty():
            self.chosen.emit(self)
            self.drag_mode = "select"
            self.hide_panels()
            self.selection = QRectF(pos, pos)
        elif self.tool == "move":
            self.old_selection = QRectF(self.selection)
            self.drag_mode = self.handle_at(pos) or ("move" if self.selection.contains(pos) else None)
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
        self.shift_pressed = bool(event.modifiers() & Qt.KeyboardModifier.ShiftModifier)
        if self.drag_mode == "object":
            self.drag_object(pos)
        elif self.drag_mode == "select":
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
        elif self.drag_mode in ("t", "r", "b", "l"):
            r = QRectF(self.old_selection)
            if self.drag_mode == "t":
                r.setTop(pos.y())
            elif self.drag_mode == "b":
                r.setBottom(pos.y())
            elif self.drag_mode == "l":
                r.setLeft(pos.x())
            else:
                r.setRight(pos.x())
            self.selection = r.normalized()
        cursor = Qt.CursorShape.CrossCursor
        if self.tool == "move" and not self.selection.isEmpty():
            target = self.drag_mode or self.handle_at(pos)
            cursor = {"tl": Qt.CursorShape.SizeFDiagCursor, "br": Qt.CursorShape.SizeFDiagCursor,
                      "tr": Qt.CursorShape.SizeBDiagCursor, "bl": Qt.CursorShape.SizeBDiagCursor,
                      "t": Qt.CursorShape.SizeVerCursor, "b": Qt.CursorShape.SizeVerCursor,
                      "l": Qt.CursorShape.SizeHorCursor, "r": Qt.CursorShape.SizeHorCursor,
                      "move": Qt.CursorShape.SizeAllCursor}.get(target,
                      Qt.CursorShape.SizeAllCursor if self.selection.contains(pos) else cursor)
            if self.shift_pressed or self.drag_mode == "object":
                handle = self.object_drag_handle if self.drag_mode == "object" else self.object_handle_at(pos)
                cursor = {"tl": Qt.CursorShape.SizeFDiagCursor, "br": Qt.CursorShape.SizeFDiagCursor,
                          "tr": Qt.CursorShape.SizeBDiagCursor, "bl": Qt.CursorShape.SizeBDiagCursor,
                          "l": Qt.CursorShape.SizeHorCursor, "r": Qt.CursorShape.SizeHorCursor,
                          "t": Qt.CursorShape.SizeVerCursor, "b": Qt.CursorShape.SizeVerCursor,
                          "start": Qt.CursorShape.SizeAllCursor, "end": Qt.CursorShape.SizeAllCursor}.get(handle,
                          Qt.CursorShape.SizeAllCursor if self.object_at(pos) is not None else Qt.CursorShape.ArrowCursor)
        self.setCursor(cursor)
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() != Qt.MouseButton.LeftButton:
            return
        if self.drag_mode == "draw" and self.active_mark:
            self.history.add(self.active_mark)
            self.active_mark = None
        elif self.drag_mode == "object" and self.current_mark() is not None:
            self.history.record_edit(self.selected_mark, self.object_original)
        self.drag_mode = None
        if self.selection.width() < 4 or self.selection.height() < 4:
            self.selection = QRectF()
            self.hide_panels()
        else:
            self.position_panel()
        self.update()

    def begin_text(self, pos, index=None):
        self.text_pos = pos
        self.editing_text_index = index
        self.editor = QLineEdit(self)
        self.editor.setPlaceholderText(self.t("text_prompt"))
        self.editor.setAccessibleName(self.t("text"))
        self.editor.setGeometry(max(0, min(int(pos.x()), self.width()-350)),
                                max(0, min(int(pos.y())-25, self.height()-44)), 345, 40)
        self.editor.returnPressed.connect(self.commit_text)
        if index is not None:
            mark = self.history.items[index]
            self.editor.setText(mark.text)
            font = text_font(mark)
            font.setPixelSize(min(28, font.pixelSize()))
            self.editor.setFont(font)
            self.editor.selectAll()
        self.editor.show()
        self.editor.setFocus()

    def commit_text(self):
        if self.editor:
            text = self.editor.text().strip()
            self.editor.deleteLater()
            self.editor = None
            index, self.editing_text_index = self.editing_text_index, None
            if index is not None:
                if text:
                    mark = deepcopy(self.history.items[index])
                    mark.text = text
                    self.history.replace(index, mark)
                else:
                    self.history.remove(index)
                    self.selected_mark = None
            elif text:
                self.history.add(Mark("text", self.text_pos, self.text_pos,
                                      self.color, self.stroke, text))
            self.setFocus()
            self.update()

    def start_ocr(self):
        if self.selection.isEmpty():
            return
        if self.ocr_dialog is not None:
            self.ocr_dialog.raise_()
            self.ocr_dialog.activateWindow()
            return
        # Recognize the original selected pixels, without toolbars or annotations.
        image = render_crop(self.screen_image, self.selection, [], self.scale)
        self.ocr_dialog = OcrDialog(image, self.lang, self.theme, self)
        self.ocr_dialog.finished.connect(self.ocr_finished)
        self.ocr_dialog.open()
        self.ocr_dialog.raise_()
        self.ocr_dialog.activateWindow()
        self.ocr_dialog.editor.setFocus()

    def ocr_finished(self, result):
        self.ocr_dialog = None
        self.activateWindow()
        self.setFocus()

    def complete(self, action):
        if action == "cancel":
            self.finished.emit("cancel", None)
        elif not self.selection.isEmpty():
            self.commit_text()
            image = render_crop(self.screen_image, self.selection,
                                self.history.items, self.scale)
            self.finished.emit(action, image)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Shift:
            self.shift_pressed = True
            self.update()
            return
        if event.key() == Qt.Key.Key_Escape:
            if self.palette.isVisible():
                self.palette.hide()
            elif self.editor:
                self.editor.deleteLater()
                self.editor = None
                self.editing_text_index = None
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
        elif event.key() == Qt.Key.Key_Delete and self.shift_pressed and self.current_mark() is not None:
            self.history.remove(self.selected_mark)
            self.selected_mark = None
            self.update()
        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            # Enter only confirms an active text annotation, handled by QLineEdit.
            event.accept()
        elif not event.modifiers():
            for key, glyph, shortcut in TOOLS:
                if event.text().upper() == shortcut:
                    self.set_tool(key)
                    break
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Shift:
            self.shift_pressed = False
            self.update()
        super().keyReleaseEvent(event)


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


def capture_cursor(pixmap, origin=None):
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
        x = cursor.pos.x - (origin.x() if origin is not None else monitor.monitor.left) - info.x
        y = cursor.pos.y - (origin.y() if origin is not None else monitor.monitor.top) - info.y
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



STRINGS['ro'].update({'record': 'Înregistrare video', 'record_start': 'Începe înregistrarea', 'record_start_tip': 'Înregistrează zona selectată. Poți muta sau redimensiona zona înainte de pornire.', 'record_tip': 'Selectează o zonă, inclusiv peste mai multe monitoare, pentru un video MP4.', 'record_stop': 'Oprește și salvează', 'record_starting': 'Se pregătește…', 'record_saving': 'Se salvează…', 'record_saved': 'Video salvat: {path}', 'record_error': 'Înregistrarea nu s-a finalizat corect. {detail}', 'microphone': 'Microfon', 'system_audio': 'Sunetul calculatorului', 'microphone_tip': 'Înregistrează microfonul implicit din Windows. Poți porni sau opri sunetul și în timpul înregistrării.', 'system_audio_tip': 'Înregistrează sunetul dispozitivului de redare implicit din Windows. Poți porni sau opri sunetul în timpul înregistrării.', 'video_note': 'MP4 · 20 cadre/s · salvare locală în dosarul pentru capturi. Selectează zona, apoi apasă Începe înregistrarea. Sunetul poate fi comutat în timpul înregistrării.', 'audio_error': '{source}: indisponibil. {detail}', 'settings_error': 'Verifică fișierul de setări și dreptul de scriere în dosarul programului. Detalii: {detail}', 'settings_saved': 'Preferințele se salvează în LumaShot.settings.json, lângă program. Scurtăturile se confirmă cu Aplică.', 'screen_note': 'Selecția poate traversa mai multe monitoare. Ecran complet capturează monitorul pe care se află cursorul.', 'tip_area': 'Selectează o zonă de pe unul sau mai multe monitoare, apoi adnotează, copiază sau salvează.', 'record_hide': 'Panoul video nu poate fi exclus din captură pe acest sistem. Mută-l în afara zonei înregistrate.'})
STRINGS['ru'].update({'record': 'Запись видео', 'record_start': 'Начать запись', 'record_start_tip': 'Запись выбранной области. Перед запуском её можно переместить или изменить размер.', 'record_tip': 'Выберите область, включая несколько мониторов, для записи видео MP4.', 'record_stop': 'Остановить и сохранить', 'record_starting': 'Подготовка…', 'record_saving': 'Сохранение…', 'record_saved': 'Видео сохранено: {path}', 'record_error': 'Не удалось завершить запись. {detail}', 'microphone': 'Микрофон', 'system_audio': 'Звук компьютера', 'microphone_tip': 'Записывать микрофон Windows по умолчанию. Звук можно включать и выключать во время записи.', 'system_audio_tip': 'Записывать звук устройства вывода Windows по умолчанию. Звук можно включать и выключать во время записи.', 'video_note': 'MP4 · 20 кадров/с · локально в папке снимков. Выделите область и нажмите «Начать запись». Звук можно переключать во время записи.', 'audio_error': '{source}: недоступно. {detail}', 'settings_error': 'Проверьте файл настроек и право записи в папку программы. Подробности: {detail}', 'settings_saved': 'Настройки сохраняются в LumaShot.settings.json рядом с программой. Сочетания клавиш подтверждаются кнопкой «Применить».', 'screen_note': 'Область может охватывать несколько мониторов. Полный экран снимает монитор под указателем мыши.', 'tip_area': 'Выделите область на одном или нескольких мониторах, затем добавьте пометки, скопируйте или сохраните.', 'record_hide': 'Не удалось исключить панель из записи. Переместите её за пределы записываемой области.'})
STRINGS['en'].update({'record': 'Record video', 'record_start': 'Start recording', 'record_start_tip': 'Record the selected area. Move or resize it before starting.', 'record_tip': 'Select an area, including across multiple monitors, to record an MP4 video.', 'record_stop': 'Stop and save', 'record_starting': 'Preparing…', 'record_saving': 'Saving…', 'record_saved': 'Video saved: {path}', 'record_error': 'Recording could not be completed. {detail}', 'microphone': 'Microphone', 'system_audio': 'Computer audio', 'microphone_tip': 'Record the default Windows microphone. You can turn it on or off during recording.', 'system_audio_tip': 'Record the default Windows playback device. You can turn it on or off during recording.', 'video_note': 'MP4 · 20 fps · saved locally in the capture folder. Select an area, then click Start recording. Audio can be toggled while recording.', 'audio_error': '{source}: unavailable. {detail}', 'settings_error': 'Check the settings file and write permission in the program folder. Details: {detail}', 'settings_saved': 'Preferences are saved in LumaShot.settings.json next to the program. Confirm shortcuts with Apply.', 'screen_note': 'Selections can span several monitors. Full screen captures the monitor under the pointer.', 'tip_area': 'Select an area across one or more monitors, then annotate, copy or save.', 'record_hide': 'The recording panel cannot be excluded on this system. Move it outside the recorded area.'})

STRINGS['ro'].update({'bar_start': 'Start', 'bar_stop': 'Stop', 'record_duration': 'Durata înregistrării', 'audio_on': 'pornit', 'audio_off': 'oprit', 'record_hotkey': 'Selectare / Start / Stop video', 'record_hide_blocked': 'Windows nu permite ascunderea barei din video. Selectează o zonă care lasă loc pentru bară deasupra ei.', 'record_start_tip': 'Pornește înregistrarea zonei selectate. Bara rămâne vizibilă pentru tine și este exclusă din video.', 'video_note': 'MP4 · 20 cadre/s · salvare locală. Selectează zona, apoi apasă Start în bara de sus. Microfonul și sunetul calculatorului se pot comuta și în timpul înregistrării.'})
STRINGS['ru'].update({'bar_start': 'Старт', 'bar_stop': 'Стоп', 'record_duration': 'Длительность записи', 'audio_on': 'включён', 'audio_off': 'выключен', 'record_hotkey': 'Выбор / Старт / Стоп видео', 'record_hide_blocked': 'Windows не позволяет исключить панель из видео. Выберите область, оставив место для панели над ней.', 'record_start_tip': 'Начать запись выбранной области. Панель остаётся видимой для вас и исключается из видео.', 'video_note': 'MP4 · 20 кадров/с · локальное сохранение. Выберите область и нажмите «Старт» на верхней панели. Микрофон и звук компьютера можно переключать во время записи.'})
STRINGS['en'].update({'bar_start': 'Start', 'bar_stop': 'Stop', 'record_duration': 'Recording duration', 'audio_on': 'on', 'audio_off': 'off', 'record_hotkey': 'Select / Start / Stop video', 'record_hide_blocked': 'Windows cannot exclude the bar from video. Select an area that leaves room for the bar above it.', 'record_start_tip': 'Start recording the selected area. The bar stays visible to you and is excluded from the video.', 'video_note': 'MP4 · 20 fps · local saving. Select an area, then click Start in the top bar. Microphone and computer audio can also be toggled during recording.'})

import json
import queue
import struct
import threading
import time
from contextlib import contextmanager
from PySide6.QtCore import QObject, QUrl, QEvent


class JsonSettings:
    """Portable preferences; replace atomically, preserving damaged input for recovery."""
    def __init__(self, path=None, migrate=True):
        program = Path(sys.executable if getattr(sys, "frozen", False) else __file__).resolve()
        self.path = Path(path) if path else program.with_name("LumaShot.settings.json")
        self.error = ""
        self.on_error = None
        self.data = dict(language="ro", theme="light", start_windows=False, notifications=True, remember_area=False,
                         include_cursor=False, capture_hotkey_enabled=True, capture_hotkey="",
                         full_hotkey_enabled=False, full_hotkey="Ctrl+Shift+F10",
                         record_hotkey_enabled=True, record_hotkey="Ctrl+Shift+F11", save_format="PNG",
                         jpeg_quality=95, full_action="edit", last_area={}, microphone=False,
                         system_audio=False, folder=str(Path(QStandardPaths.writableLocation(
                             QStandardPaths.StandardLocation.PicturesLocation)) / "LumaShot"))
        existed = self.path.exists()
        try:
            if existed:
                try:
                    data = json.loads(self.path.read_text(encoding="utf-8-sig"))
                    if not isinstance(data, dict):
                        raise ValueError("Expected a JSON object")
                except (ValueError, UnicodeError):
                    backup = self.path.with_name(self.path.name + ".damaged-" + datetime.now().strftime("%Y%m%d%H%M%S%f"))
                    self.path.rename(backup)
                    self.error = str(backup)
                    data = {}
                self.data.update({k: v for k, v in data.items() if k in self.data
                                  and type(v) is type(self.data[k])})
            elif migrate:
                previous = QSettings("LumaShot", "LumaShot")
                for key, default in self.data.items():
                    if previous.contains(key):
                        value = (previous.value(key, default) if isinstance(default, dict)
                                 else previous.value(key, default, type=type(default)))
                        if type(value) is type(default):
                            self.data[key] = value
            self._write()
        except (OSError, ValueError, TypeError) as error:
            self.error = str(error)

    def value(self, key, default=None, type=None):
        value = self.data.get(key, default)
        return type(value) if type is not None else value

    def setValue(self, key, value):
        self.data[key] = value
        try:
            self._write()
            self.error = ""
        except OSError as error:
            message = str(error)
            if self.on_error and message != self.error:
                self.on_error(message)
            self.error = message

    def _write(self):
        # A unique temporary file avoids truncating preferences on interruption.
        import tempfile
        name = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=self.path.parent,
                                             prefix=self.path.name, suffix=".tmp", delete=False) as stream:
                name = stream.name
                json.dump(self.data, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(name, self.path)
        finally:
            if name and os.path.exists(name):
                os.unlink(name)


@contextmanager
def physical_coordinates():
    user = ctypes.WinDLL("user32", use_last_error=True)
    user.SetThreadDpiAwarenessContext.argtypes = [ctypes.c_void_p]
    user.SetThreadDpiAwarenessContext.restype = ctypes.c_void_p
    old = user.SetThreadDpiAwarenessContext(ctypes.c_void_p(-4))
    try:
        yield user
    finally:
        if old:
            user.SetThreadDpiAwarenessContext(old)


def desktop_bounds():
    with physical_coordinates() as user:
        return QRect(*(user.GetSystemMetrics(index) for index in (76, 77, 78, 79)))


class DesktopGrab:
    """Reusable top-down DIB in physical pixels, including negative desktop origins."""
    def __init__(self, rect):
        self.rect = QRect(rect)
        if rect.width() < 1 or rect.height() < 1:
            raise ValueError("Empty capture area")
        self.user = ctypes.WinDLL("user32", use_last_error=True)
        self.gdi = ctypes.WinDLL("gdi32", use_last_error=True)
        handle = wintypes.HANDLE
        for fn, args, result in [
            (self.user.GetDC, [handle], handle), (self.user.ReleaseDC, [handle, handle], ctypes.c_int),
            (self.gdi.CreateCompatibleDC, [handle], handle), (self.gdi.DeleteDC, [handle], wintypes.BOOL),
            (self.gdi.CreateDIBSection, [handle, ctypes.c_void_p, wintypes.UINT,
              ctypes.POINTER(ctypes.c_void_p), handle, wintypes.DWORD], handle),
            (self.gdi.SelectObject, [handle, handle], handle), (self.gdi.DeleteObject, [handle], wintypes.BOOL),
            (self.gdi.BitBlt, [handle, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                              handle, ctypes.c_int, ctypes.c_int, wintypes.DWORD], wintypes.BOOL)]:
            fn.argtypes, fn.restype = args, result
        self.screen = self.dc = self.bitmap = self.previous = None
        self.data = ctypes.c_void_p()
        try:
            with physical_coordinates():
                self.screen = self.user.GetDC(None)
                self.dc = self.gdi.CreateCompatibleDC(self.screen)
                header = ctypes.create_string_buffer(struct.pack("<IiiHHIIiiII", 40, rect.width(),
                    -rect.height(), 1, 32, 0, 0, 0, 0, 0, 0))
                self.bitmap = self.gdi.CreateDIBSection(self.dc, header, 0, ctypes.byref(self.data), None, 0)
                if not all((self.screen, self.dc, self.bitmap, self.data.value)):
                    raise OSError("Cannot allocate desktop capture")
                self.previous = self.gdi.SelectObject(self.dc, self.bitmap)
                if not self.previous or self.previous == ctypes.c_void_p(-1).value:
                    self.previous = None
                    raise OSError("Cannot select desktop bitmap")
        except Exception:
            self.close()
            raise

    def frame(self, cursor=False):
        r = self.rect
        with physical_coordinates():
            if not self.gdi.BitBlt(self.dc, 0, 0, r.width(), r.height(), self.screen,
                                   r.x(), r.y(), 0x00CC0020 | 0x40000000):
                raise OSError("Desktop capture failed")
            self.gdi.GdiFlush()
            image = QImage(ctypes.string_at(self.data, r.width()*r.height()*4), r.width(), r.height(),
                           r.width()*4, QImage.Format.Format_RGB32).copy()
            if cursor:
                image = capture_cursor(QPixmap.fromImage(image), r.topLeft()).toImage()
            return image

    def close(self):
        if self.previous:
            self.gdi.SelectObject(self.dc, self.previous)
        if self.bitmap:
            self.gdi.DeleteObject(self.bitmap)
        if self.dc:
            self.gdi.DeleteDC(self.dc)
        if self.screen:
            self.user.ReleaseDC(None, self.screen)
        self.screen = self.dc = self.bitmap = self.previous = None

    def __del__(self):
        if hasattr(self, "screen"):
            self.close()


class DesktopSurface:
    def __init__(self, rect):
        self.bounds = QRect(rect)

    def geometry(self):
        return QApplication.primaryScreen().geometry()

    def name(self):
        r = self.bounds
        layout = [(s.name(), s.geometry().getRect(), s.devicePixelRatio()) for s in QApplication.screens()]
        return "desktop:" + str((r.getRect(), layout))


def place_desktop_overlay(overlay, bounds):
    overlay.native_bounds = QRect(bounds)
    with physical_coordinates() as user:
        user.SetWindowPos.argtypes = [wintypes.HANDLE, wintypes.HANDLE, ctypes.c_int, ctypes.c_int,
                                     ctypes.c_int, ctypes.c_int, wintypes.UINT]
        if not user.SetWindowPos(int(overlay.winId()), None, bounds.x(), bounds.y(),
                                 bounds.width(), bounds.height(), 0x0014):
            raise OSError("Cannot position desktop selection")
    # One spanning HWND uses a single DPI. Qt mouse positions and painting share it.
    overlay.scale = bounds.width() / overlay.width()


def selected_native_rect(overlay):
    bounds = overlay.native_bounds
    r = overlay.selection
    x, y = round(r.left()*overlay.scale), round(r.top()*overlay.scale)
    right, bottom = round(r.right()*overlay.scale), round(r.bottom()*overlay.scale)
    return QRect(bounds.x()+x, bounds.y()+y, right-x, bottom-y).intersected(bounds)


class RecordingOverlay(CaptureOverlay):
    """Selection-only mode; Enter never starts or copies a capture."""
    selection_ready = Signal(object)

    def make_panel(self):
        self.actions = QFrame(self)
        self.palette = QFrame(self)
        return QFrame(self)

    def position_panel(self):
        self.panel.hide()
        self.actions.hide()
        self.palette.hide()
        self.selection_ready.emit(self)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.MouseButton.LeftButton and not self.selection.isEmpty():
            self.selection_ready.emit(self)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if self.selection.isEmpty():
            self.selection_ready.emit(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.complete("cancel")
        else:
            event.accept()

    def complete(self, action):
        if action == "cancel":
            self.finished.emit(action, None)
        elif action == "record" and not self.selection.isEmpty():
            self.finished.emit(action, None)


class AudioSource:
    """WASAPI source opened only while enabled. All COM use stays on its worker."""
    def __init__(self, kind):
        self.kind = kind
        self.blocks = queue.Queue(maxsize=100)
        self.stop_event = threading.Event()
        self.error = None
        self.thread = threading.Thread(target=self.run, daemon=True, name="LumaShot-"+kind)
        self.thread.start()

    def run(self):
        ole, result = None, None
        try:
            ole = ctypes.OleDLL("ole32")
            result = ole.CoInitializeEx(None, 0)
            import soundcard as sc
            import numpy as np
            if self.kind == "microphone":
                device = sc.default_microphone()
            else:
                speaker = sc.default_speaker()
                if speaker is None:
                    raise RuntimeError("No default output device")
                device = sc.get_microphone(id=speaker.id, include_loopback=True)
            if device is None:
                raise RuntimeError("No default input device")
            # Request stereo in WASAPI shared mode, so Windows performs any native
            # surround downmix. A larger device buffer prevents small-block underruns.
            with device.recorder(samplerate=48000, channels=2, blocksize=4800) as recorder:
                while not self.stop_event.is_set():
                    samples = recorder.record(numframes=960)
                    if samples.shape[1] == 1:
                        samples = np.repeat(samples, 2, axis=1)
                    elif samples.shape[1] != 2:
                        raise RuntimeError("The audio device did not provide a stereo stream")
                    if self.stop_event.is_set():
                        break
                    try:
                        self.blocks.put_nowait(samples.copy())
                    except queue.Full:
                        raise RuntimeError("Audio capture buffer overflow; the computer cannot keep up")
        except Exception as error:
            self.error = str(error)
        finally:
            if result in (0, 1):
                ole.CoUninitialize()

    def close(self):
        self.stop_event.set()


def mix_audio(blocks, frames=960):
    import numpy as np
    result = np.zeros((frames, 2), dtype=np.float32)
    for block in blocks:
        if block is not None:
            result += block
    # Leave headroom when both sources are enabled; never wrap PCM samples.
    if len(blocks) > 1:
        result /= len(blocks)
    return (np.clip(result, -1, 1) * 32767).astype("<i2").tobytes()


class VideoRecording(QObject):
    finished = Signal(str, str)
    audio_failed = Signal(str, str)
    started = Signal()
    paused_changed = Signal(bool)

    def __init__(self, rect, path, cursor=False, parent=None, grab_factory=DesktopGrab):
        super().__init__(parent)
        from PySide6.QtMultimedia import (QAudioBufferInput, QAudioFormat, QMediaCaptureSession,
            QMediaFormat, QMediaRecorder, QVideoFrameInput, QVideoFrameFormat)
        self.path, self.cursor = str(path), cursor
        self.error = ""
        self.sources = {}
        self.audio_enabled = {}
        self.retired_sources = []
        self.active = self.stopping = self.done = False
        self.paused = False
        self.pause_time = self.paused_seconds = 0.0
        self._pumping_audio = False
        self.audio_start_frames = {}
        self.audio_frames = 0
        self.next_video = 0.0
        self.pending_audio = None
        # H.264 requires even dimensions; pad, never discard selected pixels.
        self.size = QSize(rect.width() + rect.width()%2, rect.height() + rect.height()%2)
        self.grabber = grab_factory(rect)
        self.session = QMediaCaptureSession(self)
        self.recorder = QMediaRecorder(self)
        self.session.setRecorder(self.recorder)
        fmt = QMediaFormat(QMediaFormat.FileFormat.MPEG4)
        fmt.setVideoCodec(QMediaFormat.VideoCodec.H264)
        fmt.setAudioCodec(QMediaFormat.AudioCodec.AAC)
        self.recorder.setMediaFormat(fmt)
        self.recorder.setVideoResolution(self.size)
        self.recorder.setVideoFrameRate(20)
        self.recorder.setQuality(QMediaRecorder.Quality.HighQuality)
        self.recorder.setEncodingMode(QMediaRecorder.EncodingMode.AverageBitRateEncoding)
        self.recorder.setVideoBitRate(max(2000000, min(30000000, self.size.width()*self.size.height()*4)))
        self.recorder.setAudioSampleRate(48000)
        self.recorder.setAudioChannelCount(2)
        self.recorder.setAudioBitRate(256000)
        self.recorder.setOutputLocation(QUrl.fromLocalFile(self.path))
        video_format = QVideoFrameFormat(self.size, QVideoFrameFormat.PixelFormat.Format_BGRX8888)
        video_format.setStreamFrameRate(20)
        self.video_input = QVideoFrameInput(video_format, self)
        self.session.setVideoFrameInput(self.video_input)
        self.audio_format = QAudioFormat()
        self.audio_format.setSampleRate(48000)
        self.audio_format.setChannelCount(2)
        self.audio_format.setSampleFormat(QAudioFormat.SampleFormat.Int16)
        self.audio_input = QAudioBufferInput(self.audio_format, self)
        self.session.setAudioBufferInput(self.audio_input)
        self.recorder.recorderStateChanged.connect(self.state_changed)
        self.recorder.errorOccurred.connect(self.recorder_error)
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.TimerType.PreciseTimer)
        self.timer.timeout.connect(self.pump)

    def set_audio(self, kind, enabled):
        if self.active and not self.stopping and not self._pumping_audio:
            self.pump_audio(self.elapsed())
        self.audio_enabled[kind] = enabled
        self.retired_sources = [source for source in self.retired_sources
                                if getattr(source, "thread", None) and source.thread.is_alive()]
        previous = self.sources.pop(kind, None)
        if previous:
            previous.close()
            self.retired_sources.append(previous)
        # Discard queued PCM on any mute change, so muted samples cannot leak later.
        self.pending_audio = None
        if enabled and self.active and not self.paused and not self.stopping and not self.done:
            self.audio_start_frames[kind] = round(self.elapsed()*50)*960
            self.sources[kind] = AudioSource(kind)

    def start(self):
        if self.done or self.stopping:
            return
        self.start_time = time.monotonic()
        self.recorder.record()
        if not self.done:
            self.timer.start(10)
        QTimer.singleShot(5000, self.check_started)

    def check_started(self):
        if not self.active and not self.done:
            self.recorder_error(None, "Video encoder did not start")

    def state_changed(self, state):
        from PySide6.QtMultimedia import QMediaRecorder
        if state == QMediaRecorder.RecorderState.RecordingState:
            self.active = True
            self.start_time = time.monotonic()
            for kind, enabled in list(self.audio_enabled.items()):
                self.set_audio(kind, enabled)
            self.started.emit()
        elif state == QMediaRecorder.RecorderState.StoppedState and (self.active or self.stopping):
            self.finalize()

    def recorder_error(self, code, message):
        if self.done:
            return
        self.error = message or "Video encoder failed"
        self.stop()

    def elapsed(self):
        if not self.active:
            return 0
        now = self.pause_time if self.paused else time.monotonic()
        return max(0, now - getattr(self, "start_time", now) - self.paused_seconds)

    def set_paused(self, paused):
        if not self.active or self.stopping or self.done or self.paused == paused:
            return
        if paused:
            self.pause_time = time.monotonic()
            self.paused = True
            self.pump_audio(self.elapsed())
            # Release the actual inputs while paused; keep queued pre-pause samples
            # until the encoder accepts the end of the active segment.
            for source in self.sources.values():
                source.close()
        else:
            self.pump_audio(self.elapsed())
            self.paused_seconds += time.monotonic() - self.pause_time
            self.paused = False
            for kind, enabled in list(self.audio_enabled.items()):
                self.set_audio(kind, enabled)
        self.paused_changed.emit(self.paused)

    def pump_audio(self, target):
        from PySide6.QtMultimedia import QAudioBuffer
        self._pumping_audio = True
        try:
            for _ in range(25):
                if self.audio_frames / 48000 >= target:
                    break
                if self.pending_audio is None:
                    blocks = []
                    for kind, source in list(self.sources.items()):
                        if source.error:
                            self.set_audio(kind, False)
                            self.audio_failed.emit(kind, source.error)
                            continue
                        if self.audio_frames < self.audio_start_frames.get(kind, 0):
                            continue
                        try:
                            blocks.append(source.blocks.get_nowait())
                        except queue.Empty:
                            blocks.append(None)
                    self.pending_audio = QAudioBuffer(QByteArray(mix_audio(blocks)), self.audio_format,
                                                       round(self.audio_frames * 1000000 / 48000))
                if not self.audio_input.sendAudioBuffer(self.pending_audio):
                    break
                self.pending_audio = None
                self.audio_frames += 960
        finally:
            self._pumping_audio = False

    def pump(self):
        from PySide6.QtMultimedia import QVideoFrame
        if not self.active or self.done:
            return
        try:
            if self.stopping:
                self.pump_audio(self.stop_elapsed)
                if self.audio_frames/48000 >= self.stop_elapsed or time.monotonic() >= self.stop_deadline:
                    if self.audio_frames/48000 < self.stop_elapsed and not self.error:
                        self.error = "Audio encoder did not finish pending samples"
                    self.finish_stop()
                return
            elapsed = self.elapsed()
            # Audio is submitted 150 ms behind the live clock to absorb WASAPI
            # scheduling jitter. Its timestamps remain unchanged, preserving A/V sync.
            self.pump_audio(elapsed if self.paused else max(0, elapsed-.15))
            if self.paused:
                return
            if elapsed >= self.next_video:
                image = self.grabber.frame(self.cursor)
                if image.size() != self.size:
                    padded = QImage(self.size, QImage.Format.Format_RGB32)
                    padded.fill(Qt.GlobalColor.black)
                    painter = QPainter(padded)
                    painter.drawImage(0, 0, image)
                    painter.end()
                    image = padded
                frame = QVideoFrame(image)
                frame.setStartTime(round(elapsed * 1000000))
                frame.setEndTime(round((elapsed + .05) * 1000000))
                if self.video_input.sendVideoFrame(frame):
                    self.next_video = (int(elapsed*20)+1) / 20
            # A stalled encoder must not build an ever-growing A/V delay.
            if elapsed - self.audio_frames / 48000 > 3:
                raise RuntimeError("Encoder cannot keep up with the selected area")
        except Exception as error:
            if self.stopping:
                self.error = str(error)
                self.finish_stop()
            else:
                self.recorder_error(None, str(error))

    def stop(self):
        if self.done or self.stopping:
            return
        self.stopping = True
        self.stop_elapsed = self.elapsed()
        self.stop_deadline = time.monotonic()+1.5
        for source in self.sources.values():
            source.close()
        self.grabber.close()
        if self.active:
            self.pump()
        else:
            self.finish_stop()

    def finish_stop(self):
        self.timer.stop()
        self.recorder.stop()
        from PySide6.QtMultimedia import QMediaRecorder
        if self.recorder.recorderState() == QMediaRecorder.RecorderState.StoppedState:
            self.finalize()

    def finalize(self):
        if self.done:
            return
        self.done = True
        self.timer.stop()
        self.grabber.close()
        for source in [*self.sources.values(), *self.retired_sources]:
            source.close()
        if not self.error and (self.next_video == 0 or not Path(self.path).exists()
                               or Path(self.path).stat().st_size < 100):
            self.error = "No video frames were saved"
        self.finished.emit(self.path, self.error)


def exclude_from_capture(widget):
    """Keep a top-level control clickable while Windows omits it from captures."""
    if sys.platform != "win32" or QApplication.platformName() == "offscreen":
        return False
    user = ctypes.WinDLL("user32", use_last_error=True)
    user.SetWindowDisplayAffinity.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    user.GetWindowDisplayAffinity.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
    value = wintypes.DWORD()
    hwnd = int(widget.winId())
    return bool(user.SetWindowDisplayAffinity(hwnd, 0x11)
                and user.GetWindowDisplayAffinity(hwnd, ctypes.byref(value)) and value.value == 0x11)


def native_window_rect(widget):
    if QApplication.platformName() == "offscreen":
        return widget.geometry()
    with physical_coordinates() as user:
        user.GetWindowRect.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.RECT)]
        rect = wintypes.RECT()
        if not user.GetWindowRect(int(widget.winId()), ctypes.byref(rect)):
            raise OSError("Cannot locate recording controls")
        return QRect(rect.left, rect.top, rect.right-rect.left, rect.bottom-rect.top)


def recording_bar_position(region, size, work_area):
    """Prefer above the selection; stay on one usable monitor at desktop edges."""
    width, height = size.width(), size.height()
    x = region.x() + (region.width()-width)//2
    y = region.y()-height-8
    if y < work_area.top():
        y = region.y()+8
    x = max(work_area.x(), min(x, work_area.x()+work_area.width()-width))
    y = max(work_area.y(), min(y, work_area.y()+work_area.height()-height))
    return QPoint(x, y)


def place_recording_bar(widget, region):
    if QApplication.platformName() == "offscreen":
        work = QApplication.primaryScreen().availableGeometry()
        widget.move(recording_bar_position(region, widget.size(), work))
        return
    class MonitorInfo(ctypes.Structure):
        _fields_ = [("size", wintypes.DWORD), ("monitor", wintypes.RECT),
                    ("work", wintypes.RECT), ("flags", wintypes.DWORD)]
    with physical_coordinates() as user:
        user.MonitorFromPoint.argtypes = [wintypes.POINT, wintypes.DWORD]
        user.MonitorFromPoint.restype = wintypes.HANDLE
        user.GetMonitorInfoW.argtypes = [wintypes.HANDLE, ctypes.POINTER(MonitorInfo)]
        user.SetWindowPos.argtypes = [wintypes.HANDLE, wintypes.HANDLE, ctypes.c_int, ctypes.c_int,
                                     ctypes.c_int, ctypes.c_int, wintypes.UINT]
        info = MonitorInfo()
        info.size = ctypes.sizeof(info)
        monitor = user.MonitorFromPoint(wintypes.POINT(region.center().x(), region.top()), 2)
        if not user.GetMonitorInfoW(monitor, ctypes.byref(info)):
            raise OSError("Cannot locate recording monitor")
        work = QRect(info.work.left, info.work.top, info.work.right-info.work.left,
                     info.work.bottom-info.work.top)
        # Moving to another DPI can resize the HWND; anchor again using its new size.
        for _ in range(2):
            position = recording_bar_position(region, native_window_rect(widget).size(), work)
            if not user.SetWindowPos(int(widget.winId()), None, position.x(), position.y(), 0, 0, 0x0015):
                raise OSError("Cannot position recording controls")


STRINGS["ro"].update(record_pause="Pauză", record_resume="Continuă", record_paused="Înregistrare în pauză",
                    record_pause_tip="Pune filmarea pe pauză. Imaginea și sunetul din pauză nu se salvează.",
                    record_resume_tip="Continuă în același videoclip, fără durata pauzei.")
STRINGS["ru"].update(record_pause="Пауза", record_resume="Продолжить", record_paused="Запись приостановлена",
                    record_pause_tip="Приостановить запись. Изображение и звук во время паузы не сохраняются.",
                    record_resume_tip="Продолжить тот же ролик, исключив длительность паузы.")
STRINGS["en"].update(record_pause="Pause", record_resume="Resume", record_paused="Recording paused",
                    record_pause_tip="Pause recording. Video and audio during the pause are not saved.",
                    record_resume_tip="Continue in the same video, without the paused time.")


class RecordingBoundary:
    """Four click-through strips mark native pixels without covering the workspace."""
    def __init__(self, rect):
        self.region = QRect(rect)
        self.strips = []
        for _ in range(4):
            strip = QWidget(None, Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.WindowTransparentForInput |
                            Qt.WindowType.WindowDoesNotAcceptFocus)
            strip.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
            strip.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
            strip.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
            strip.setObjectName("recordBoundary")
            self.strips.append(strip)
        self.set_paused(False)

    def rectangles(self, outside=False):
        r, d = self.region, 3
        x, y, w, h = r.getRect()
        if outside:
            return [QRect(x-d, y-d, w+2*d, d), QRect(x-d, y+h, w+2*d, d),
                    QRect(x-d, y, d, h), QRect(x+w, y, d, h)]
        return [QRect(x, y, w, min(d, h)), QRect(x, y+h-min(d, h), w, min(d, h)),
                QRect(x, y, min(d, w), h), QRect(x+w-min(d, w), y, min(d, w), h)]

    def show(self):
        for strip, inside, outside in zip(self.strips, self.rectangles(), self.rectangles(True)):
            strip.setGeometry(inside)
            strip.show()
            # If Windows cannot exclude a strip, keep every pixel outside the crop.
            target = inside if exclude_from_capture(strip) else outside
            if sys.platform == "win32" and QApplication.platformName() != "offscreen":
                place_desktop_overlay(strip, target)
            else:
                strip.setGeometry(target)

    def set_paused(self, paused):
        color = "#d79b2e" if paused else "#eb5b5b"
        for strip in self.strips:
            strip.setStyleSheet(f"QWidget#recordBoundary {{ background: {color}; }}")

    def close(self):
        for strip in self.strips:
            strip.close()
            strip.deleteLater()
        self.strips.clear()


class RecordingControls(QWidget):
    start_requested = Signal()
    cancel_requested = Signal()

    def __init__(self, owner, recording=None, rect=None):
        super().__init__(None, Qt.WindowType.Tool | Qt.WindowType.WindowStaysOnTopHint |
                         Qt.WindowType.FramelessWindowHint)
        self.owner, self.recording = owner, None
        self.region = QRect(rect) if rect is not None else None
        self.closing = self.preparing = self.capture_excluded = False
        self.boundary = None
        self.setObjectName("recordBar")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setWindowTitle("LumaShot — " + owner.t("record"))
        self.setWindowIcon(app_icon())
        colors = theme_colors(owner.theme)
        self.foreground = colors["fg"]
        self.setStyleSheet(f"""
            QWidget#recordBar {{ background: {colors['raised']}; border: 1px solid {colors['border']}; border-radius: 9px; }}
            QPushButton {{ background: transparent; color: {colors['fg']}; border: none; border-radius: 5px; padding: 0; min-width: 32px; max-width: 32px; min-height: 32px; max-height: 32px; }}
            QPushButton:hover {{ background: {colors['selected']}; }}
            QPushButton:checked {{ background: {colors['selected']}; }}
            QPushButton#recordAction {{ background: {colors['accent']}; color: white; font-weight: 600; min-width: 94px; max-width: 94px; }}
            QPushButton#recordAction:hover {{ background: {colors['hover']}; }}
            QPushButton#recordAction:disabled {{ background: {colors['border']}; color: {colors['muted']}; }}
            QLabel {{ color: {colors['muted']}; background: transparent; border: none; }}
        """)
        row = QHBoxLayout(self)
        row.setContentsMargins(6, 6, 6, 6)
        row.setSpacing(6)
        self.start_button = QPushButton(owner.t("bar_start"))
        self.start_button.setObjectName("recordAction")
        self.start_button.setFixedSize(94, 32)
        self.start_button.setIcon(ui_icon("circle-dot", "#ffffff"))
        self.start_button.setToolTip(wrapped_tip(owner.t("record_start_tip")))
        self.start_button.clicked.connect(self.primary_action)
        row.addWidget(self.start_button)
        self.stop_button = self.start_button
        self.duration = QLabel("00:00:00")
        self.duration.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.duration.setFixedWidth(76)
        self.duration.setFont(QFont("Consolas", 10))
        self.duration.setToolTip(owner.t("record_duration"))
        row.addWidget(self.duration)
        self.pause_button = QPushButton()
        self.pause_button.setFixedSize(32, 32)
        self.pause_button.setIcon(ui_icon("pause", self.foreground))
        self.pause_button.setAccessibleName(owner.t("record_pause"))
        self.pause_button.setToolTip(wrapped_tip(owner.t("record_pause_tip")))
        self.pause_button.setEnabled(False)
        self.pause_button.clicked.connect(self.toggle_pause)
        row.addWidget(self.pause_button)
        self.checks = {}
        for key in ("microphone", "system_audio"):
            button = QPushButton()
            button.setFixedSize(32, 32)
            button.setIconSize(QSize(20, 20))
            button.setCheckable(True)
            button.setChecked(owner.option(key))
            button.toggled.connect(lambda enabled, k=key: self.toggle(k, enabled))
            self.checks[key] = button
            self.update_audio_button(key)
            row.addWidget(button)
        self.error_label = QLabel("!")
        self.error_label.setFixedWidth(16)
        self.error_label.setStyleSheet("QLabel { color: #c66b16; font-weight: bold; }")
        self.error_label.hide()
        row.addWidget(self.error_label)
        separator = QFrame()
        separator.setFixedSize(1, 20)
        separator.setStyleSheet(f"QFrame {{ background: {colors['border']}; }}")
        row.addWidget(separator)
        self.close_button = QPushButton()
        self.close_button.setFixedSize(30, 32)
        self.close_button.setIcon(ui_icon("cancel", self.foreground))
        self.close_button.setToolTip(owner.t("cancel"))
        self.close_button.setAccessibleName(owner.t("cancel"))
        self.close_button.clicked.connect(self.request_close)
        row.addWidget(self.close_button)
        for button in self.findChildren(QPushButton):
            button.setAutoDefault(False)
            button.setDefault(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(200)
        QApplication.instance().installEventFilter(self)
        self.adjustSize()
        if recording is not None:
            self.attach_recording(recording)

    def eventFilter(self, watched, event):
        # Qt tooltips are separate windows, so exclude them as well as the bar.
        if (not self.closing and self.isVisible() and event.type() == QEvent.Type.Show
                and isinstance(watched, QWidget) and watched.windowType() == Qt.WindowType.ToolTip):
            if not exclude_from_capture(watched) and self.recording is not None:
                watched.hide()
        return super().eventFilter(watched, event)

    def set_region(self, rect):
        self.region = QRect(rect)
        self.adjustSize()
        self.show()
        self.capture_excluded = exclude_from_capture(self)
        place_recording_bar(self, self.region)
        self.raise_()
        if not self.safe_to_record():
            self.show_error(self.owner.t("record_hide_blocked"))

    def safe_to_record(self):
        return (self.capture_excluded or self.region is None
                or not native_window_rect(self).intersects(self.region))

    def show_error(self, text):
        self.error_label.setToolTip(wrapped_tip(text))
        self.error_label.setAccessibleName(text)
        self.error_label.show()
        self.adjustSize()
        if self.region is not None:
            place_recording_bar(self, self.region)

    def primary_action(self):
        if not self.start_button.isEnabled() or self.preparing:
            return
        if self.recording is not None:
            self.stop()
        elif self.safe_to_record():
            self.start_requested.emit()
        else:
            self.show_error(self.owner.t("record_hide_blocked"))

    def set_preparing(self):
        self.preparing = True
        self.start_button.setEnabled(False)
        self.start_button.setToolTip(self.owner.t("record_starting"))
        self.close_button.setEnabled(False)
        for button in self.checks.values():
            button.setEnabled(False)

    def attach_recording(self, recording):
        self.recording = recording
        recording.audio_failed.connect(self.audio_failed)
        recording.started.connect(self.on_started)
        recording.paused_changed.connect(self.on_paused)
        self.start_button.setText(self.owner.t("bar_stop"))
        self.start_button.setIcon(ui_icon("rect", "#ffffff"))
        self.start_button.setToolTip(self.owner.t("record_stop"))
        self.close_button.setToolTip(self.owner.t("record_stop"))
        self.close_button.setAccessibleName(self.owner.t("record_stop"))
        if recording.active:
            self.on_started()

    def on_started(self):
        self.preparing = False
        self.start_button.setEnabled(True)
        self.close_button.setEnabled(True)
        self.pause_button.setEnabled(True)
        if self.region is not None and self.boundary is None:
            self.boundary = RecordingBoundary(self.region)
            self.boundary.show()
            self.raise_()
        for button in self.checks.values():
            button.setEnabled(True)
        self.refresh()

    def toggle_pause(self):
        if self.recording is not None:
            self.recording.set_paused(not self.recording.paused)

    def on_paused(self, paused):
        action = "record_resume" if paused else "record_pause"
        self.pause_button.setIcon(ui_icon("resume" if paused else "pause", self.foreground))
        self.pause_button.setAccessibleName(self.owner.t(action))
        self.pause_button.setToolTip(wrapped_tip(self.owner.t(action + "_tip")))
        self.duration.setToolTip(self.owner.t("record_paused" if paused else "record_duration"))
        if self.boundary:
            self.boundary.set_paused(paused)
        self.refresh()

    def update_audio_button(self, kind):
        enabled = self.checks[kind].isChecked()
        names = ("mic", "mic-off") if kind == "microphone" else ("volume-2", "volume-x")
        self.checks[kind].setIcon(ui_icon(names[0 if enabled else 1], self.foreground))
        text = self.owner.t(kind) + ": " + self.owner.t("audio_on" if enabled else "audio_off")
        self.checks[kind].setAccessibleName(text)
        self.checks[kind].setToolTip(wrapped_tip(text + "\n" + self.owner.t(kind + "_tip")))

    def toggle(self, kind, enabled):
        self.owner.settings.setValue(kind, enabled)
        self.update_audio_button(kind)
        if self.recording is not None:
            self.recording.set_audio(kind, enabled)

    def audio_failed(self, kind, error):
        self.checks[kind].setChecked(False)
        self.show_error(self.owner.t("audio_error", source=self.owner.t(kind), detail=error))

    def refresh(self):
        seconds = int(self.recording.elapsed()) if self.recording is not None else 0
        self.duration.setText(f"{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02}")

    def stop(self):
        if self.recording is None:
            self.cancel_requested.emit()
            return
        if self.recording.stopping or self.recording.done:
            return
        self.start_button.setEnabled(False)
        self.start_button.setToolTip(self.owner.t("record_saving"))
        self.close_button.setEnabled(False)
        self.pause_button.setEnabled(False)
        for button in self.checks.values():
            button.setEnabled(False)
        self.recording.stop()

    def request_close(self):
        if self.recording is None:
            self.cancel_requested.emit()
        else:
            self.stop()

    def dispose(self):
        self.closing = True
        if self.boundary:
            self.boundary.close()
            self.boundary = None
        self.timer.stop()
        QApplication.instance().removeEventFilter(self)
        self.close()

    def closeEvent(self, event):
        if self.closing or (self.recording is not None and self.recording.done):
            self.timer.stop()
            QApplication.instance().removeEventFilter(self)
            event.accept()
        else:
            event.ignore()
            self.request_close()



from PySide6.QtWidgets import QDialog
import tempfile
import shutil
import subprocess


NEW_COPY = {
    "ro": {
        "startup": "Pornește odată cu Windows", "tip_startup": "Pornește LumaShot în tray la conectarea în Windows. Poți dezactiva oricând această opțiune.",
        "record_stop": "Oprește și previzualizează", "video_note": "MP4 · 20 cadre/s. Selectează zona și apasă Start. După Stop, revezi filmarea și alegi dacă și unde o salvezi.",
        "startup_error": "Pornirea cu Windows nu a putut fi modificată. {detail}",
        "review": "Previzualizare video", "review_note": "Revezi filmarea, apoi alege dacă și unde o păstrezi.",
        "video_save": "Salvează…", "video_default": "În dosarul implicit", "video_custom": "Alege locația…",
        "video_discard": "Renunță la filmare", "video_keep": "Înapoi la video", "video_unsaved": "Filmarea nu este salvată. Ce dorești să faci?",
        "video_play": "Redă", "video_pause_playback": "Pauză redare", "video_seek": "Poziție în videoclip", "video_mute": "Oprește sunetul previzualizării", "video_unmute": "Pornește sunetul previzualizării",
        "video_save_title": "Salvează filmarea", "video_saving": "Se salvează… {percent}%", "video_save_error": "Nu s-a putut salva filmarea. Originalul este păstrat pentru a încerca din nou. {detail}",
        "video_preview_error": "Previzualizarea nu este disponibilă: {detail}. Poți salva în continuare fișierul.",
        "object_hint": "Ține Shift pentru a selecta, muta sau redimensiona desenele. Shift + dublu clic pe text pentru a-l rescrie.",
    },
    "ru": {
        "startup": "Запускать вместе с Windows", "tip_startup": "Запускать LumaShot в трее при входе в Windows. Эту опцию можно отключить в любое время.",
        "record_stop": "Остановить и просмотреть", "video_note": "MP4 · 20 кадров/с. Выделите область и нажмите Старт. После остановки просмотрите запись и выберите, сохранять ли её и куда.",
        "startup_error": "Не удалось изменить автозапуск. {detail}",
        "review": "Просмотр видео", "review_note": "Просмотрите запись и выберите, сохранять ли её и в какую папку.",
        "video_save": "Сохранить…", "video_default": "В папку по умолчанию", "video_custom": "Выбрать расположение…",
        "video_discard": "Удалить черновик", "video_keep": "Вернуться к видео", "video_unsaved": "Запись не сохранена. Что вы хотите сделать?",
        "video_play": "Воспроизвести", "video_pause_playback": "Пауза просмотра", "video_seek": "Позиция в видео", "video_mute": "Выключить звук просмотра", "video_unmute": "Включить звук просмотра",
        "video_save_title": "Сохранить запись", "video_saving": "Сохранение… {percent}%", "video_save_error": "Не удалось сохранить запись. Оригинал сохранён для повторной попытки. {detail}",
        "video_preview_error": "Просмотр недоступен: {detail}. Файл по-прежнему можно сохранить.",
        "object_hint": "Удерживайте Shift, чтобы выбирать, перемещать и менять размер пометок. Shift + двойной щелчок по тексту — изменить текст.",
    },
    "en": {
        "startup": "Start with Windows", "tip_startup": "Start LumaShot in the tray when you sign in to Windows. You can turn this off at any time.",
        "record_stop": "Stop and review", "video_note": "MP4 · 20 fps. Select an area and click Start. After Stop, review the recording and choose whether and where to save it.",
        "startup_error": "Could not change startup with Windows. {detail}",
        "review": "Video preview", "review_note": "Review your recording, then choose whether and where to keep it.",
        "video_save": "Save…", "video_default": "Default folder", "video_custom": "Choose location…",
        "video_discard": "Discard recording", "video_keep": "Back to video", "video_unsaved": "This recording has not been saved. What would you like to do?",
        "video_play": "Play", "video_pause_playback": "Pause playback", "video_seek": "Video position", "video_mute": "Mute preview audio", "video_unmute": "Unmute preview audio",
        "video_save_title": "Save recording", "video_saving": "Saving… {percent}%", "video_save_error": "Could not save the recording. The original is kept so you can try again. {detail}",
        "video_preview_error": "Preview is unavailable: {detail}. You can still save the file.",
        "object_hint": "Hold Shift to select, move or resize annotations. Shift + double-click text to rewrite it.",
    },
}
for _language, _copy in NEW_COPY.items():
    STRINGS[_language].update(_copy)


class WindowsStartup:
    KEY = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"

    def registry(self):
        return QSettings(self.KEY, QSettings.Format.NativeFormat)

    def command(self):
        if getattr(sys, "frozen", False):
            parts = [str(Path(sys.executable).resolve()), "--tray"]
        else:
            executable = Path(sys.executable).resolve()
            windowed = executable.with_name("pythonw.exe")
            parts = [str(windowed if windowed.exists() else executable), str(Path(__file__).resolve()), "--tray"]
        return subprocess.list2cmdline(parts)

    def enabled(self):
        return sys.platform == "win32" and bool(self.registry().value("LumaShot", ""))

    def set_enabled(self, enabled):
        if sys.platform != "win32":
            raise OSError("Windows startup is only available on Windows")
        registry = self.registry()
        if enabled:
            registry.setValue("LumaShot", self.command())
        else:
            registry.remove("LumaShot")
        registry.sync()
        if registry.status() != QSettings.Status.NoError:
            raise OSError(str(registry.status()))


class VideoDraft:
    def __init__(self):
        self.directory = tempfile.TemporaryDirectory(prefix="LumaShot-recording-")
        self.root = Path(self.directory.name).resolve()
        self.path = self.root / ("LumaShot_"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")+".mp4")

    def cleanup(self, attempts=0):
        # Only our freshly created draft directory may be recursively removed.
        if self.root.parent != Path(tempfile.gettempdir()).resolve() or not self.root.name.startswith("LumaShot-recording-"):
            raise OSError("Unexpected draft directory")
        try:
            self.directory.cleanup()
        except PermissionError:
            if attempts < 10:
                QTimer.singleShot(200, lambda: self.cleanup(attempts+1))


def save_video_draft(source, target, overwrite=False, progress=None):
    source, target = Path(source), Path(target)
    if target.resolve().is_relative_to(source.parent.resolve()):
        raise OSError("Choose a destination outside the temporary recording folder")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and not overwrite:
        raise FileExistsError(str(target))
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".LumaShot-save-", suffix=".tmp", dir=target.parent, delete=False) as output:
            temporary = Path(output.name)
            size, copied = source.stat().st_size, 0
            with source.open("rb") as video:
                while block := video.read(1024*1024):
                    output.write(block)
                    copied += len(block)
                    if progress:
                        progress(round(copied*100/max(1, size)))
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


class VideoReview(QDialog):
    saved = Signal(str)
    copy_done = Signal(str, str)
    copy_progress = Signal(int)

    def __init__(self, draft, folder, language, parent=None):
        super().__init__(parent)
        from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoSink
        from PySide6.QtWidgets import QSizePolicy
        self.draft, self.folder, self.lang = draft, Path(folder), language
        self.saved_path = None
        self.saving = self.allow_close = False
        self.setWindowTitle(self.t("review"))
        self.setWindowIcon(app_icon())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.resize(840, 580)
        self.setMinimumSize(600, 430)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        title = QLabel(self.t("review_note"))
        title.setWordWrap(True)
        layout.addWidget(title)
        self.video = QLabel()
        self.video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video.setStyleSheet("background: #101618; border-radius: 8px;")
        self.video.setMinimumSize(320, 240)
        self.video.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        self.video_image = QImage()
        layout.addWidget(self.video, 1)
        self.player = QMediaPlayer(self)
        self.audio = QAudioOutput(self)
        self.audio.setVolume(1)
        self.player.setAudioOutput(self.audio)
        self.video_sink = QVideoSink(self)
        self.video_sink.videoFrameChanged.connect(self.present_frame)
        self.player.setVideoSink(self.video_sink)
        controls = QHBoxLayout()
        self.play_button = QPushButton(self.t("video_play"))
        self.play_button.clicked.connect(self.toggle_playback)
        controls.addWidget(self.play_button)
        self.seek = QSlider(Qt.Orientation.Horizontal)
        self.seek.setAccessibleName(self.t("video_seek"))
        self.seek.setToolTip(self.t("video_seek"))
        self.seek.sliderMoved.connect(self.player.setPosition)
        controls.addWidget(self.seek, 1)
        self.time_label = QLabel("00:00 / 00:00")
        controls.addWidget(self.time_label)
        self.mute = QPushButton()
        self.foreground = QApplication.palette().color(QPalette.ColorRole.WindowText).name()
        self.mute.setCheckable(True)
        self.mute.setIcon(ui_icon("volume-2", self.foreground))
        self.mute.setToolTip(self.t("video_mute"))
        self.mute.setAccessibleName(self.t("video_mute"))
        self.mute.toggled.connect(self.change_mute)
        controls.addWidget(self.mute)
        layout.addLayout(controls)
        self.status = QLabel()
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        actions = QHBoxLayout()
        self.discard_button = QPushButton(self.t("video_discard"))
        self.discard_button.clicked.connect(self.discard)
        actions.addWidget(self.discard_button)
        actions.addStretch()
        self.save_button = QPushButton(self.t("video_save"))
        self.save_button.setObjectName("primary")
        menu = QMenu(self.save_button)
        default = menu.addAction(self.t("video_default"))
        default.setToolTip(wrapped_tip(str(self.folder)))
        default.triggered.connect(self.save_default)
        custom = menu.addAction(self.t("video_custom"))
        custom.triggered.connect(self.save_custom)
        menu.setToolTipsVisible(True)
        self.save_button.setMenu(menu)
        actions.addWidget(self.save_button)
        layout.addLayout(actions)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.positionChanged.connect(self.position_changed)
        self.player.playbackStateChanged.connect(self.playback_changed)
        self.player.errorOccurred.connect(lambda code, detail: self.status.setText(self.t("video_preview_error", detail=detail)))
        self.copy_done.connect(self.saved_result)
        self.copy_progress.connect(lambda percent: self.status.setText(self.t("video_saving", percent=percent)))
        self.player.setSource(QUrl.fromLocalFile(str(draft.path)))

    def t(self, key, **values):
        return tr(self.lang, key, **values)

    def present_frame(self, frame):
        if frame.isValid():
            self.video_image = frame.toImage()
            self.update_video_image()

    def update_video_image(self):
        if not self.video_image.isNull():
            self.video.setPixmap(QPixmap.fromImage(self.video_image).scaled(
                self.video.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "video_image"):
            self.update_video_image()

    @staticmethod
    def clock(milliseconds):
        seconds = milliseconds//1000
        return f"{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02}" if seconds >= 3600 else f"{seconds//60:02}:{seconds%60:02}"

    def duration_changed(self, duration):
        self.seek.setRange(0, max(0, duration))
        self.position_changed(self.player.position())

    def position_changed(self, position):
        if not self.seek.isSliderDown():
            self.seek.setValue(position)
        self.time_label.setText(self.clock(position)+" / "+self.clock(self.player.duration()))

    def playback_changed(self, state):
        from PySide6.QtMultimedia import QMediaPlayer
        self.play_button.setText(self.t("video_pause_playback" if state == QMediaPlayer.PlaybackState.PlayingState else "video_play"))

    def toggle_playback(self):
        from PySide6.QtMultimedia import QMediaPlayer
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            if self.player.position() >= self.player.duration():
                self.player.setPosition(0)
            self.player.play()

    def release_player(self):
        self.player.stop()
        self.player.setSource(QUrl())

    def change_mute(self, muted):
        self.audio.setMuted(muted)
        self.mute.setIcon(ui_icon("volume-x" if muted else "volume-2", self.foreground))
        self.mute.setToolTip(self.t("video_unmute" if muted else "video_mute"))
        self.mute.setAccessibleName(self.mute.toolTip())

    def save_default(self):
        self.save_to(self.folder/self.draft.path.name)

    def save_custom(self):
        path, _ = QFileDialog.getSaveFileName(self, self.t("video_save_title"), str(self.folder/self.draft.path.name), "MP4 (*.mp4)")
        if path:
            target = Path(path)
            if not target.suffix:
                target = target.with_suffix(".mp4")
            self.save_to(target, overwrite=True)

    def save_to(self, target, overwrite=False):
        if self.saving or self.allow_close:
            return
        self.saving = True
        self.release_player()
        for button in (self.save_button, self.discard_button, self.play_button, self.mute, self.seek):
            button.setEnabled(False)
        self.status.setText(self.t("video_saving", percent=0))
        def copy():
            try:
                save_video_draft(self.draft.path, target, overwrite, self.copy_progress.emit)
                self.copy_done.emit(str(target), "")
            except Exception as error:
                self.copy_done.emit("", str(error))
        threading.Thread(target=copy, name="LumaShot-save-video", daemon=True).start()

    def saved_result(self, path, error):
        self.saving = False
        if error:
            for button in (self.save_button, self.discard_button, self.play_button, self.mute, self.seek):
                button.setEnabled(True)
            self.status.setText(self.t("video_save_error", detail=error))
            self.player.setSource(QUrl.fromLocalFile(str(self.draft.path)))
            return
        self.saved_path = path
        self.allow_close = True
        self.saved.emit(path)
        self.accept()

    def discard(self):
        if self.saving:
            return
        self.release_player()
        self.allow_close = True
        super().reject()

    def reject(self):
        if self.allow_close:
            super().reject()
        elif not self.saving:
            question = QMessageBox(self)
            question.setWindowTitle(self.t("review"))
            question.setText(self.t("video_unsaved"))
            save = question.addButton(self.t("video_save"), QMessageBox.ButtonRole.AcceptRole)
            discard = question.addButton(self.t("video_discard"), QMessageBox.ButtonRole.DestructiveRole)
            cancel = question.addButton(self.t("video_keep"), QMessageBox.ButtonRole.RejectRole)
            question.setDefaultButton(cancel)
            question.exec()
            if question.clickedButton() is discard:
                self.discard()
            elif question.clickedButton() is save:
                self.save_button.showMenu()


# Windows' built-in OCR is called through its supported WinRT API in Windows
# PowerShell 5.1. No image or recognized text is uploaded or logged.
import base64
from PySide6.QtWidgets import QPlainTextEdit, QProgressBar
from PySide6.QtGui import QDesktopServices

OCR_SCRIPT = r'''
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$reply = @{ok=$false; code='backend'; languages=@()}
$stream = $null
$bitmap = $null
try {
    Add-Type -AssemblyName System.Runtime.WindowsRuntime
    [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime] > $null
    [Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime] > $null
    [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime] > $null
    [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType=WindowsRuntime] > $null
    [Windows.Globalization.Language, Windows.Globalization, ContentType=WindowsRuntime] > $null
    $script:asTask = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and
        $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
    } | Select-Object -First 1
    function Await($operation, [Type]$resultType) {
        $task = $script:asTask.MakeGenericMethod($resultType).Invoke($null, @($operation))
        return $task.GetAwaiter().GetResult()
    }
    $available = [Windows.Media.Ocr.OcrEngine]::AvailableRecognizerLanguages
    $reply.languages = @($available | ForEach-Object { @{tag=$_.LanguageTag; name=$_.NativeName} })
    if ($available.Count -eq 0) {
        $reply.code = 'no_languages'
    } else {
        $engine = $null
        if ($env:LUMASHOT_OCR_LANGUAGE) {
            $language = [Windows.Globalization.Language]::new($env:LUMASHOT_OCR_LANGUAGE)
            $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($language)
        } else {
            $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
            if ($null -eq $engine) {
                $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($available[0])
            }
        }
        if ($null -eq $engine) { throw 'The selected OCR language is unavailable.' }
        $file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($env:LUMASHOT_OCR_IMAGE)) ([Windows.Storage.StorageFile])
        $stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
        $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
        $transform = [Windows.Graphics.Imaging.BitmapTransform]::new()
        $limit = [Windows.Media.Ocr.OcrEngine]::MaxImageDimension
        $factor = [Math]::Min(1.0, $limit / [double][Math]::Max($decoder.PixelWidth, $decoder.PixelHeight))
        $transform.ScaledWidth = [uint32][Math]::Max(1, [Math]::Floor($decoder.PixelWidth * $factor))
        $transform.ScaledHeight = [uint32][Math]::Max(1, [Math]::Floor($decoder.PixelHeight * $factor))
        $bitmap = Await ($decoder.GetSoftwareBitmapAsync(
            [Windows.Graphics.Imaging.BitmapPixelFormat]::Bgra8,
            [Windows.Graphics.Imaging.BitmapAlphaMode]::Ignore, $transform,
            [Windows.Graphics.Imaging.ExifOrientationMode]::IgnoreExifOrientation,
            [Windows.Graphics.Imaging.ColorManagementMode]::DoNotColorManage)) ([Windows.Graphics.Imaging.SoftwareBitmap])
        $result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
        $reply.ok = $true
        $reply.code = ''
        $reply.text = ($result.Lines | ForEach-Object { $_.Text }) -join "`n"
        $reply.language = $engine.RecognizerLanguage.LanguageTag
    }
} catch {
    $reply.detail = $_.Exception.Message
} finally {
    if ($null -ne $bitmap) { $bitmap.Dispose() }
    if ($null -ne $stream) { $stream.Dispose() }
}
$json = ConvertTo-Json -InputObject $reply -Depth 4 -Compress
[Console]::Out.Write([Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($json)))
'''


class OcrFailure(Exception):
    def __init__(self, code, detail=""):
        super().__init__(detail or code)
        self.code, self.detail = code, detail


def recognize_text(image, language="", cancelled=None, timeout=30):
    """Recognize immutable selected pixels locally; bound time and clean temp files."""
    if sys.platform != "win32":
        raise OcrFailure("unavailable")
    executable = Path(os.environ.get("SystemRoot", "C:/Windows")) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    if not executable.is_file():
        raise OcrFailure("unavailable")
    if image.isNull():
        raise OcrFailure("image")
    cancelled = cancelled or threading.Event()
    if cancelled.is_set():
        raise OcrFailure("cancelled")
    with tempfile.TemporaryDirectory(prefix="LumaShot-ocr-") as folder:
        path = Path(folder) / "selection.png"
        if not image.save(str(path), "PNG"):
            raise OcrFailure("image")
        environment = os.environ.copy()
        environment["LUMASHOT_OCR_IMAGE"] = str(path)
        environment["LUMASHOT_OCR_LANGUAGE"] = language
        command = [str(executable), "-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand",
                   base64.b64encode(OCR_SCRIPT.encode("utf-16-le")).decode("ascii")]
        process = subprocess.Popen(command, env=environment, stdin=subprocess.DEVNULL,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
        deadline = time.monotonic() + timeout
        try:
            while True:
                if cancelled.is_set():
                    raise OcrFailure("cancelled")
                if time.monotonic() >= deadline:
                    raise OcrFailure("timeout")
                try:
                    stdout, stderr = process.communicate(timeout=.1)
                    break
                except subprocess.TimeoutExpired:
                    continue
        finally:
            if process.poll() is None:
                process.kill()
                process.communicate()
        if process.returncode:
            raise OcrFailure("backend")
        try:
            result = json.loads(base64.b64decode(stdout.strip(), validate=True).decode("utf-8-sig"))
            if not isinstance(result, dict) or not isinstance(result.get("languages"), list):
                raise ValueError("Invalid OCR response")
        except (ValueError, UnicodeError):
            raise OcrFailure("backend") from None
        return result


OCR_COPY = {
    "ro": {
        "ocr": "Extrage textul", "tip_ocr": "Recunoaște textul din zona selectată. Poți verifica și copia rezultatul fără să închizi captura.",
        "ocr_title": "Text din captură", "ocr_note": "Selectează sau corectează textul înainte de copiere. Recunoașterea se face local, pe calculator.",
        "ocr_busy": "Se recunoaște textul…", "ocr_language": "Limba textului", "ocr_auto": "Automat (Windows)",
        "ocr_copy": "Copiază textul", "ocr_copy_tip": "Copiază textul selectat sau, dacă nu ai selectat nimic, tot textul.",
        "ocr_close": "Înapoi la captură", "ocr_copied": "Text copiat.", "ocr_empty": "Nu am găsit text. Încearcă o zonă mai clară sau altă limbă.",
        "ocr_ready": "Text recunoscut · {recognized_language}", "ocr_retry": "Încearcă din nou", "ocr_result": "Text recunoscut, editabil",
        "ocr_no_languages": "Nu este instalată nicio limbă pentru recunoașterea textului în Windows. Adaugă un pachet OCR din setările de limbă, apoi încearcă din nou.",
        "ocr_timeout": "Recunoașterea a durat prea mult. Încearcă o zonă mai mică.", "ocr_unavailable": "Recunoașterea locală Windows nu este disponibilă pe acest calculator.",
        "ocr_backend": "Windows nu a putut recunoaște textul. Verifică pachetele OCR instalate sau încearcă din nou.",
        "ocr_image": "Imaginea selectată nu a putut fi pregătită pentru recunoaștere.", "ocr_windows": "Limbi Windows…",
    },
    "ru": {
        "ocr": "Извлечь текст", "tip_ocr": "Распознать текст выбранной области. Проверьте и скопируйте результат, не закрывая снимок.",
        "ocr_title": "Текст со снимка", "ocr_note": "Выделите или исправьте текст перед копированием. Распознавание выполняется локально на компьютере.",
        "ocr_busy": "Распознавание текста…", "ocr_language": "Язык текста", "ocr_auto": "Автоматически (Windows)",
        "ocr_copy": "Копировать текст", "ocr_copy_tip": "Копировать выделенный текст или весь текст, если ничего не выделено.",
        "ocr_close": "Назад к снимку", "ocr_copied": "Текст скопирован.", "ocr_empty": "Текст не найден. Выберите более чёткую область или другой язык.",
        "ocr_ready": "Текст распознан · {recognized_language}", "ocr_retry": "Повторить", "ocr_result": "Распознанный текст, доступный для правки",
        "ocr_no_languages": "В Windows не установлен ни один язык OCR. Добавьте пакет распознавания в настройках языков и повторите попытку.",
        "ocr_timeout": "Распознавание заняло слишком много времени. Выберите область поменьше.", "ocr_unavailable": "Локальное распознавание Windows недоступно на этом компьютере.",
        "ocr_backend": "Windows не удалось распознать текст. Проверьте установленные пакеты OCR или повторите попытку.",
        "ocr_image": "Не удалось подготовить выбранное изображение для распознавания.", "ocr_windows": "Языки Windows…",
    },
    "en": {
        "ocr": "Extract text", "tip_ocr": "Recognize text in the selected area. Review and copy it without closing the capture.",
        "ocr_title": "Text from screenshot", "ocr_note": "Select or correct the text before copying. Recognition runs locally on your computer.",
        "ocr_busy": "Recognizing text…", "ocr_language": "Text language", "ocr_auto": "Automatic (Windows)",
        "ocr_copy": "Copy text", "ocr_copy_tip": "Copy the selected text, or all text when nothing is selected.",
        "ocr_close": "Back to capture", "ocr_copied": "Text copied.", "ocr_empty": "No text found. Try a clearer area or another language.",
        "ocr_ready": "Text recognized · {recognized_language}", "ocr_retry": "Try again", "ocr_result": "Recognized text, editable",
        "ocr_no_languages": "No Windows OCR languages are installed. Add an OCR language pack in Windows language settings, then try again.",
        "ocr_timeout": "Recognition took too long. Try a smaller area.", "ocr_unavailable": "Local Windows text recognition is unavailable on this computer.",
        "ocr_backend": "Windows could not recognize the text. Check the installed OCR language packs or try again.",
        "ocr_image": "The selected image could not be prepared for recognition.", "ocr_windows": "Windows languages…",
    },
}
for _language, _copy in OCR_COPY.items():
    STRINGS[_language].update(_copy)


class OcrJob(QObject):
    done = Signal(object, object)

    def __init__(self, image, language, backend=recognize_text):
        super().__init__()  # Independent lifetime: a closing capture must not delete a running job.
        self.image, self.language, self.backend = image.copy(), language, backend
        self.cancelled = threading.Event()

    def start(self):
        threading.Thread(target=self.run, daemon=True, name="LumaShot-OCR").start()

    def run(self):
        try:
            result = self.backend(self.image, self.language, self.cancelled)
        except OcrFailure as error:
            result = {"ok": False, "code": error.code}
        except Exception:
            result = {"ok": False, "code": "backend"}
        if not self.cancelled.is_set():
            self.done.emit(self, result)

    def cancel(self):
        self.cancelled.set()


class OcrDialog(QDialog):
    def __init__(self, image, language, theme="light", parent=None, backend=recognize_text):
        flags = Qt.WindowType.Dialog
        # A normal dialog can remain behind the always-on-top capture tool on
        # Windows, even when it is modal. Keep both windows in the same band.
        if parent is not None and parent.windowFlags() & Qt.WindowType.WindowStaysOnTopHint:
            flags |= Qt.WindowType.WindowStaysOnTopHint
        super().__init__(parent, flags)
        self.image, self.lang, self.backend = image.copy(), language, backend
        self.job = None
        self.setWindowTitle(self.t("ocr_title"))
        self.setWindowIcon(app_icon())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.resize(680, 460)
        self.setMinimumSize(460, 320)
        colors = theme_colors(theme)
        self.setStyleSheet(theme_style(theme) + f"""
QDialog {{ background: {colors['bg']}; }}
QPlainTextEdit {{ background: {colors['input']}; color: {colors['fg']}; border: 1px solid {colors['border']}; border-radius: 6px; padding: 10px; font-size: 15px; }}
QProgressBar {{ border: none; background: {colors['border']}; min-height: 3px; max-height: 3px; }}
QProgressBar::chunk {{ background: {colors['accent']}; }}
""")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)
        note = QLabel(self.t("ocr_note"))
        note.setWordWrap(True)
        layout.addWidget(note)
        row = QHBoxLayout()
        row.addWidget(QLabel(self.t("ocr_language")))
        self.languages = ChoiceBox()
        self.languages.setAccessibleName(self.t("ocr_language"))
        self.languages.addItem(self.t("ocr_auto"), "")
        self.languages.currentIndexChanged.connect(self.start_recognition)
        row.addWidget(self.languages, 1)
        self.retry = QPushButton(self.t("ocr_retry"))
        self.retry.clicked.connect(self.start_recognition)
        row.addWidget(self.retry)
        layout.addLayout(row)
        self.editor = QPlainTextEdit()
        self.editor.setAccessibleName(self.t("ocr_result"))
        self.editor.textChanged.connect(self.refresh_copy)
        layout.addWidget(self.editor, 1)
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setTextVisible(False)
        layout.addWidget(self.progress)
        self.status = QLabel()
        self.status.setObjectName("muted")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        footer = QHBoxLayout()
        self.windows_languages = QPushButton(self.t("ocr_windows"))
        self.windows_languages.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("ms-settings:regionlanguage")))
        self.windows_languages.hide()
        footer.addWidget(self.windows_languages)
        footer.addStretch()
        close = QPushButton(self.t("ocr_close"))
        close.clicked.connect(self.reject)
        self.copy = QPushButton(self.t("ocr_copy"))
        self.copy.setObjectName("primary")
        self.copy.setIcon(ui_icon("copy", "#ffffff"))
        self.copy.setToolTip(wrapped_tip(self.t("ocr_copy_tip")))
        self.copy.clicked.connect(self.copy_text)
        for button in (close, self.copy, self.retry, self.windows_languages):
            button.setAutoDefault(False)
            button.setDefault(False)
        footer.addWidget(close)
        footer.addWidget(self.copy)
        layout.addLayout(footer)
        self.copy.setEnabled(False)
        QTimer.singleShot(0, self.start_recognition)

    def t(self, key, **values):
        return tr(self.lang, key, **values)

    def start_recognition(self, *args):
        if self.job:
            self.job.cancel()
        self.editor.clear()
        self.editor.setEnabled(False)
        self.retry.setEnabled(False)
        self.progress.show()
        self.windows_languages.hide()
        self.status.setText(self.t("ocr_busy"))
        self.job = OcrJob(self.image, self.languages.currentData() or "", self.backend)
        self.job.done.connect(self.recognized)
        self.job.start()

    def recognized(self, job, result):
        if job is not self.job:
            return
        self.job = None
        self.progress.hide()
        self.retry.setEnabled(True)
        self.editor.setEnabled(True)
        if "languages" in result:
            selected = self.languages.currentData()
            self.languages.blockSignals(True)
            self.languages.clear()
            self.languages.addItem(self.t("ocr_auto"), "")
            for language in result["languages"]:
                self.languages.addItem(language["name"], language["tag"])
            index = self.languages.findData(selected)
            self.languages.setCurrentIndex(max(0, index))
            self.languages.blockSignals(False)
        if not result.get("ok"):
            code = result.get("code", "backend")
            key = "ocr_" + code
            self.status.setText(self.t(key if key in OCR_COPY[self.lang] else "ocr_backend"))
            self.windows_languages.setVisible(code in ("no_languages", "backend"))
        else:
            text = result.get("text", "")
            self.editor.setPlainText(text)
            self.status.setText(self.t("ocr_ready", recognized_language=result.get("language", "")) if text.strip() else self.t("ocr_empty"))
        self.refresh_copy()

    def refresh_copy(self):
        self.copy.setEnabled(self.editor.isEnabled() and bool(self.editor.toPlainText().strip()))

    def copy_text(self):
        if not self.copy.isEnabled():
            return
        selected = self.editor.textCursor().selectedText()
        text = selected.replace("\u2029", "\n") if selected else self.editor.toPlainText()
        if text.strip():
            QApplication.clipboard().setText(text)
            self.status.setText(self.t("ocr_copied"))

    def reject(self):
        if self.job:
            self.job.cancel()
        super().reject()

    def closeEvent(self, event):
        if self.job:
            self.job.cancel()
        super().closeEvent(event)


# GitHub is contacted only after a manual check or an explicit startup opt-in.
import hashlib
import re
import urllib.error
import urllib.request
import urllib.parse
from zipfile import ZipFile, BadZipFile

APP_VERSION = "5.0.0"
UPDATE_REPOSITORY = "TOKKAB1/LumaShot"
UPDATE_PAGE = "https://github.com/" + UPDATE_REPOSITORY + "/releases/latest"
UPDATE_API = "https://api.github.com/repos/" + UPDATE_REPOSITORY + "/releases/latest"
MAX_UPDATE_SIZE = 512 * 1024 * 1024


class UpdateFailure(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def version_tuple(value):
    match = re.fullmatch(r"v?(\d+)\.(\d+)\.(\d+)", str(value))
    return tuple(map(int, match.groups())) if match else None


def release_installer(release):
    """Use an installer's exact version; a legacy tag such as v4 means no 4.0 upgrade."""
    if not isinstance(release, dict) or release.get("draft") or release.get("prerelease"):
        return None
    candidates = []
    for asset in release.get("assets", []):
        match = re.fullmatch(r"LumaShot-Setup-(\d+\.\d+\.\d+)-Windows-x64\.(exe|zip)", asset.get("name", ""))
        url = asset.get("browser_download_url", "")
        if not match or not url.startswith("https://github.com/" + UPDATE_REPOSITORY + "/releases/download/"):
            continue
        version, extension = match.groups()
        tag = version_tuple(release.get("tag_name"))
        if tag and tag != version_tuple(version):
            continue
        size = asset.get("size", 0)
        if not isinstance(size, int) or not 0 < size <= MAX_UPDATE_SIZE:
            continue
        candidates.append({"version": version, "extension": extension, "asset": asset,
                           "notes": str(release.get("body") or "")[:50000],
                           "page": "https://github.com/" + UPDATE_REPOSITORY + "/releases/tag/" +
                                   urllib.parse.quote(str(release.get("tag_name", "")), safe="")})
    return max(candidates, key=lambda item: (version_tuple(item["version"]), item["extension"] == "exe")) if candidates else None


def check_release(cancelled):
    request = urllib.request.Request(UPDATE_API, headers={"Accept": "application/vnd.github+json",
        "User-Agent": "LumaShot/" + APP_VERSION, "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read(2*1024*1024+1)
        if len(data) > 2*1024*1024:
            raise UpdateFailure("invalid")
        release = release_installer(json.loads(data))
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return {"state": "current"}
        raise UpdateFailure("network") from None
    except (OSError, ValueError):
        raise UpdateFailure("network") from None
    if cancelled.is_set():
        raise UpdateFailure("cancelled")
    if release is None:
        raise UpdateFailure("invalid")
    return {"state": "available" if version_tuple(release["version"]) > version_tuple(APP_VERSION) else "current", "release": release}


def download_installer(release, cancelled, progress, opener=urllib.request.urlopen):
    asset = release["asset"]
    url = asset["browser_download_url"]
    if not url.startswith("https://github.com/" + UPDATE_REPOSITORY + "/releases/download/"):
        raise UpdateFailure("invalid")
    digest = str(asset.get("digest") or "")
    if not re.fullmatch(r"sha256:[a-fA-F0-9]{64}", digest):
        raise UpdateFailure("checksum_missing")
    expected_size = asset["size"]
    if not isinstance(expected_size, int) or not 0 < expected_size <= MAX_UPDATE_SIZE:
        raise UpdateFailure("invalid")
    directory = tempfile.TemporaryDirectory(prefix="LumaShot-update-")
    try:
        downloaded = Path(directory.name) / "download.bin"
        checksum, received = hashlib.sha256(), 0
        request = urllib.request.Request(url, headers={"User-Agent": "LumaShot/" + APP_VERSION})
        with opener(request, timeout=15) as response, downloaded.open("wb") as target:
            final = urllib.parse.urlparse(response.geturl())
            if final.scheme != "https" or final.hostname not in ("github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com"):
                raise UpdateFailure("invalid")
            while True:
                if cancelled.is_set():
                    raise UpdateFailure("cancelled")
                block = response.read(128*1024)
                if not block:
                    break
                received += len(block)
                if received > expected_size or received > MAX_UPDATE_SIZE:
                    raise UpdateFailure("invalid")
                checksum.update(block)
                target.write(block)
                progress(min(100, received*100//expected_size))
        if cancelled.is_set():
            raise UpdateFailure("cancelled")
        if received != expected_size or checksum.hexdigest().lower() != digest[7:].lower():
            raise UpdateFailure("checksum")
        installer = Path(directory.name) / ("LumaShot-Setup-" + release["version"] + "-Windows-x64.exe")
        if release["extension"] == "zip":
            with ZipFile(downloaded) as archive:
                matches = [entry for entry in archive.infolist() if not entry.is_dir() and Path(entry.filename).name == installer.name]
                if len(matches) != 1 or matches[0].file_size > MAX_UPDATE_SIZE or matches[0].flag_bits & 1:
                    raise UpdateFailure("invalid")
                # Copy one known entry to a fixed filename; never extract archive paths.
                with archive.open(matches[0]) as source, installer.open("wb") as target:
                    written = 0
                    while block := source.read(128*1024):
                        if cancelled.is_set():
                            raise UpdateFailure("cancelled")
                        written += len(block)
                        if written > MAX_UPDATE_SIZE:
                            raise UpdateFailure("invalid")
                        target.write(block)
        else:
            downloaded.replace(installer)
        with installer.open("rb") as source:
            if source.read(2) != b"MZ":
                raise UpdateFailure("invalid")
        return {"state": "downloaded", "directory": directory, "installer": installer}
    except Exception:
        directory.cleanup()
        raise


UPDATE_HANDOFF_SCRIPT = r'''
$ErrorActionPreference = 'Stop'
$installer = $env:LUMASHOT_UPDATE_INSTALLER
$folder = [IO.Path]::GetDirectoryName($installer)
Wait-Process -Id ([int]$env:LUMASHOT_UPDATE_PID) -ErrorAction SilentlyContinue
Start-Sleep -Milliseconds 400
try {
    $setup = Start-Process -FilePath $installer -PassThru
    $setup.WaitForExit()
} finally {
    # Delete only files created by this download, then the empty temporary folder.
    Remove-Item -LiteralPath $installer -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath (Join-Path $folder 'download.bin') -Force -ErrorAction SilentlyContinue
    try { [IO.Directory]::Delete($folder) } catch {}
}
'''


def launch_update(installer):
    """Start the interactive installer after this app exits; never run it silently."""
    installer = Path(installer).resolve()
    folder = installer.parent
    if folder.parent != Path(tempfile.gettempdir()).resolve() or not folder.name.startswith("LumaShot-update-") or not installer.is_file():
        raise UpdateFailure("install")
    powershell = Path(os.environ.get("SystemRoot", "C:/Windows")) / "System32/WindowsPowerShell/v1.0/powershell.exe"
    environment = os.environ.copy()
    environment.update(LUMASHOT_UPDATE_INSTALLER=str(installer), LUMASHOT_UPDATE_PID=str(os.getpid()))
    encoded = base64.b64encode(UPDATE_HANDOFF_SCRIPT.encode("utf-16-le")).decode("ascii")
    return subprocess.Popen([str(powershell), "-NoLogo", "-NoProfile", "-NonInteractive", "-EncodedCommand", encoded],
                            env=environment, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                            creationflags=subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP)


UPDATE_COPY = {
    "ro": {
        "updates": "Actualizări", "update_check": "Verifică actualizările", "update_auto": "Verifică actualizările la pornire",
        "tip_update_auto": "Contactează GitHub la pornire pentru a verifica versiunile noi. Nu descarcă și nu instalează automat.",
        "update_note": "Actualizările se verifică pe GitHub. Capturile și textul recunoscut nu sunt trimise. Descărcarea și instalarea pornesc numai când le alegi.",
        "update_version": "Versiunea instalată: {version}", "update_checking": "Se verifică versiunile de pe GitHub…",
        "update_current": "Nu există o versiune stabilă mai nouă decât {version}.", "update_available": "Este disponibilă versiunea {version}.",
        "update_download": "Descarcă actualizarea", "update_downloading": "Se descarcă… {percent}%", "update_install": "Instalează și închide LumaShot",
        "update_ready": "Installerul este descărcat și verificat. Instalarea va închide LumaShot; urmează pașii din installer.",
        "update_open": "Deschide pe GitHub", "update_close": "Închide", "update_retry": "Reîncearcă", "update_notes": "Modificările versiunii",
        "update_network": "Nu am putut verifica sau descărca actualizarea. Verifică internetul și încearcă din nou.",
        "update_invalid": "Versiunea publicată nu are un installer Windows x64 compatibil. Poți deschide pagina de pe GitHub.",
        "update_checksum": "Fișierul descărcat nu corespunde verificării de integritate. Nu va fi pornit; încearcă din nou.",
        "update_checksum_missing": "GitHub nu furnizează suma de control pentru acest fișier. Folosește pagina versiunii pentru descărcare.",
        "update_install_error": "Installerul nu a putut fi pornit. Poți descărca actualizarea de pe pagina GitHub.",
        "update_busy": "Încheie captura sau filmarea și salvează ori renunță la ciornă înainte de instalare.",
    },
    "ru": {
        "updates": "Обновления", "update_check": "Проверить обновления", "update_auto": "Проверять обновления при запуске",
        "tip_update_auto": "Проверять новые версии на GitHub при запуске. Не скачивает и не устанавливает автоматически.",
        "update_note": "Версии проверяются на GitHub. Снимки и распознанный текст не отправляются. Скачивание и установка начинаются только по вашему выбору.",
        "update_version": "Установлена версия: {version}", "update_checking": "Проверка версий на GitHub…",
        "update_current": "Нет стабильной версии новее {version}.", "update_available": "Доступна версия {version}.",
        "update_download": "Скачать обновление", "update_downloading": "Скачивание… {percent}%", "update_install": "Установить и закрыть LumaShot",
        "update_ready": "Установщик скачан и проверен. LumaShot закроется; следуйте шагам установщика.",
        "update_open": "Открыть на GitHub", "update_close": "Закрыть", "update_retry": "Повторить", "update_notes": "Изменения версии",
        "update_network": "Не удалось проверить или скачать обновление. Проверьте интернет и повторите попытку.",
        "update_invalid": "У версии нет совместимого установщика Windows x64. Можно открыть страницу на GitHub.",
        "update_checksum": "Скачанный файл не прошёл проверку целостности и не будет запущен. Повторите попытку.",
        "update_checksum_missing": "GitHub не предоставляет контрольную сумму файла. Используйте страницу версии для скачивания.",
        "update_install_error": "Не удалось запустить установщик. Скачайте обновление со страницы GitHub.",
        "update_busy": "Завершите снимок или запись и сохраните либо удалите черновик перед установкой.",
    },
    "en": {
        "updates": "Updates", "update_check": "Check for updates", "update_auto": "Check for updates at startup",
        "tip_update_auto": "Contact GitHub at startup to check for newer versions. Does not download or install automatically.",
        "update_note": "Versions are checked on GitHub. Screenshots and recognized text are not sent. Downloads and installation start only when you choose them.",
        "update_version": "Installed version: {version}", "update_checking": "Checking GitHub for releases…",
        "update_current": "There is no stable release newer than {version}.", "update_available": "Version {version} is available.",
        "update_download": "Download update", "update_downloading": "Downloading… {percent}%", "update_install": "Install and close LumaShot",
        "update_ready": "The installer is downloaded and verified. LumaShot will close; follow the installer steps.",
        "update_open": "Open on GitHub", "update_close": "Close", "update_retry": "Try again", "update_notes": "Release changes",
        "update_network": "Could not check or download the update. Check your internet connection and try again.",
        "update_invalid": "This release has no compatible Windows x64 installer. You can open its GitHub page.",
        "update_checksum": "The downloaded file failed its integrity check and will not be launched. Try again.",
        "update_checksum_missing": "GitHub does not provide a checksum for this file. Use the release page to download it.",
        "update_install_error": "Could not start the installer. Download the update from GitHub instead.",
        "update_busy": "Finish the capture or recording and save or discard the draft before installing.",
    },
}
for _language, _copy in UPDATE_COPY.items():
    STRINGS[_language].update(_copy)


class UpdateJob(QObject):
    done = Signal(object, object)
    progress = Signal(object, int)

    def __init__(self, release=None):
        super().__init__()
        self.release = release
        self.cancelled = threading.Event()

    def start(self):
        threading.Thread(target=self.run, daemon=True, name="LumaShot-Update").start()

    def run(self):
        try:
            result = download_installer(self.release, self.cancelled,
                lambda percent: self.progress.emit(self, percent)) if self.release else check_release(self.cancelled)
        except UpdateFailure as error:
            result = {"state": "error", "code": error.code}
        except Exception:
            result = {"state": "error", "code": "network"}
        if not self.cancelled.is_set():
            self.done.emit(self, result)
        elif result.get("directory"):
            result["directory"].cleanup()

    def cancel(self):
        self.cancelled.set()


class UpdateDialog(QDialog):
    def __init__(self, owner, initial_release=None):
        super().__init__(owner)
        self.owner, self.lang = owner, owner.lang
        self.initial_release = initial_release
        self.job = self.release = self.directory = self.installer = None
        self.setWindowTitle("LumaShot — " + self.t("updates"))
        self.setWindowIcon(app_icon())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.resize(640, 410)
        self.setMinimumSize(480, 320)
        colors = theme_colors(owner.theme)
        self.setStyleSheet(theme_style(owner.theme) + f"QDialog {{ background: {colors['bg']}; }} QPlainTextEdit {{ background: {colors['input']}; color: {colors['fg']}; padding: 8px; border: 1px solid {colors['border']}; border-radius: 6px; }}")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)
        layout.addWidget(QLabel(self.t("update_version", version=APP_VERSION)))
        self.status = QLabel(self.t("update_checking"))
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        self.notes = QPlainTextEdit()
        self.notes.setReadOnly(True)
        self.notes.setAccessibleName(self.t("update_notes"))
        layout.addWidget(self.notes, 1)
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        layout.addWidget(self.progress)
        buttons = QHBoxLayout()
        self.page = QPushButton(self.t("update_open"))
        self.page.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(self.release["page"] if self.release else UPDATE_PAGE)))
        buttons.addWidget(self.page)
        buttons.addStretch()
        self.close_button = QPushButton(self.t("update_close"))
        self.close_button.clicked.connect(self.reject)
        buttons.addWidget(self.close_button)
        self.action = QPushButton(self.t("update_check"))
        self.action.setObjectName("primary")
        self.action.setEnabled(False)
        self.action.clicked.connect(self.activate_action)
        buttons.addWidget(self.action)
        for button in (self.page, self.close_button, self.action):
            button.setAutoDefault(False)
            button.setDefault(False)
        layout.addLayout(buttons)
        QTimer.singleShot(0, self.initialize_check)

    def t(self, key, **values):
        return tr(self.lang, key, **values)

    def initialize_check(self):
        if self.initial_release:
            self.completed(None, {"state": "available", "release": self.initial_release})
        else:
            self.check()

    def check(self):
        self.status.setText(self.t("update_checking"))
        self.begin_job(UpdateJob())

    def begin_job(self, job):
        if self.job:
            self.job.cancel()
        self.job = job
        self.action.setEnabled(False)
        self.progress.setRange(0, 0)
        self.progress.show()
        job.done.connect(self.completed)
        job.progress.connect(self.download_progress)
        job.start()

    def completed(self, job, result):
        if job is not self.job:
            if result.get("directory"):
                result["directory"].cleanup()
            return
        self.job = None
        self.progress.hide()
        if result["state"] == "available":
            self.release = result["release"]
            self.notes.setPlainText(self.release["notes"])
            self.status.setText(self.t("update_available", version=self.release["version"]))
            self.action.setText(self.t("update_download"))
        elif result["state"] == "downloaded":
            self.directory, self.installer = result["directory"], result["installer"]
            self.status.setText(self.t("update_ready"))
            self.action.setText(self.t("update_install"))
        elif result["state"] == "current":
            self.status.setText(self.t("update_current", version=APP_VERSION))
            self.action.setText(self.t("update_check"))
        else:
            code = result.get("code", "network")
            key = "update_" + code
            self.status.setText(self.t(key if key in UPDATE_COPY[self.lang] else "update_network"))
            self.action.setText(self.t("update_download") if self.release else self.t("update_retry"))
        self.action.setEnabled(True)

    def download_progress(self, job, percent):
        if job is self.job:
            self.progress.setRange(0, 100)
            self.progress.setValue(percent)
            self.status.setText(self.t("update_downloading", percent=percent))

    def activate_action(self):
        if self.installer:
            self.install()
        elif self.release:
            self.begin_job(UpdateJob(self.release))
        else:
            self.check()

    def install(self):
        if self.owner.recording or self.owner.overlays or self.owner.review_dialog or self.owner.capture_pending:
            self.status.setText(self.t("update_busy"))
            return
        try:
            launch_update(self.installer)
        except (OSError, UpdateFailure):
            self.status.setText(self.t("update_install_error"))
            return
        # The detached helper owns these files until the installer closes.
        self.directory._finalizer.detach()
        self.directory = None
        self.owner.quit_app()

    def reject(self):
        if self.job:
            self.job.cancel()
        if self.directory:
            self.directory.cleanup()
            self.directory = None
        super().reject()

    def closeEvent(self, event):
        self.reject()
        event.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings = JsonSettings()
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
        self.recording = None
        self.record_controls = None
        self.recording_draft = None
        self.review_dialog = None
        self.update_dialog = None
        self.update_job = None
        self.pending_update = None
        self.startup = WindowsStartup()
        self.quit_after_recording = False
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
        self.record_hotkeys = Hotkeys(lambda: self.hotkey_capture("record"),
                                     self.settings.value("record_hotkey", "Ctrl+Shift+F11"),
                                     id_base=0x5B80, defaults=False,
                                     enabled=self.option("record_hotkey_enabled", True))
        QApplication.instance().installNativeEventFilter(self.hotkeys)
        QApplication.instance().installNativeEventFilter(self.full_hotkeys)
        QApplication.instance().installNativeEventFilter(self.record_hotkeys)
        self.tray = QSystemTrayIcon(self.windowIcon(), self)
        self.tray.setToolTip("LumaShot")
        self.tray.activated.connect(self.tray_activated)
        self.settings.on_error = lambda detail: QMessageBox.warning(
            self, self.t("error"), self.t("settings_error", detail=detail))
        self.rebuild_ui()
        self.rebuild_tray()
        if self.settings.error:
            QTimer.singleShot(0, lambda: self.settings.on_error(self.settings.error))
        if QSystemTrayIcon.isSystemTrayAvailable():
            self.tray.show()
        if self.option("check_updates", False):
            QTimer.singleShot(2500, lambda: self.check_updates(quiet=True))

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
        self.record_button = QPushButton(self.t("record"))
        self.record_button.setIcon(ui_icon("video", self.icon_color))
        self.record_button.setToolTip(wrapped_tip(self.t("record_tip")))
        self.record_button.setMinimumHeight(56)
        self.record_button.clicked.connect(lambda: self.start_capture("record"))
        row.addWidget(self.record_button)
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
        self.startup_check = ContrastCheckBox(self.t("startup"))
        self.startup_check.setToolTip(wrapped_tip(self.t("tip_startup")))
        self.startup_check.setChecked(self.startup.enabled())
        self.startup_check.setEnabled(sys.platform == "win32")
        self.startup_check.toggled.connect(self.change_startup)
        form.addRow(self.startup_check)
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
        for full, prefix, key, default, default_enabled in (
                (False, "capture", "hotkey_label", "Ctrl+Shift+F9", True),
                (True, "full", "full_hotkey", "Ctrl+Shift+F10", False),
                ("record", "record", "record_hotkey", "Ctrl+Shift+F11", True)):

            row = QHBoxLayout()
            enabled = ContrastCheckBox(self.t(key))
            enabled.setToolTip(wrapped_tip(self.t("tip_enable_hotkey")))
            enabled.setChecked(self.option(prefix + "_hotkey_enabled", default_enabled))
            row.addWidget(enabled, 1)
            editor = QKeySequenceEdit()
            editor.setMaximumSequenceLength(1)
            editor.setKeySequence(QKeySequence(self.settings.value(prefix + "_hotkey", default)))
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
            if full == "record":
                self.record_hotkey_editor, self.record_hotkey_enabled = editor, enabled
                self.record_shortcuts = status
            elif full:
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
        video = QWidget()
        video_form = QVBoxLayout(video)
        video_form.setContentsMargins(20, 18, 20, 18)
        video_form.setSpacing(14)
        for key in ("microphone", "system_audio"):
            check = ContrastCheckBox(self.t(key))
            check.setToolTip(wrapped_tip(self.t(key + "_tip")))
            check.setChecked(self.option(key))
            check.toggled.connect(lambda value, k=key: self.settings.setValue(k, value))
            video_form.addWidget(check)
        video_form.addWidget(self.label("video_note", "muted", True))
        video_form.addStretch()
        self.tabs.addTab(video, self.t("record"))
        self.tabs.setTabToolTip(3, wrapped_tip(self.t("record_tip")))
        updates = QWidget()
        update_layout = QVBoxLayout(updates)
        update_layout.setContentsMargins(20, 18, 20, 18)
        update_layout.setSpacing(14)
        update_layout.addWidget(QLabel(self.t("update_version", version=APP_VERSION)))
        update_layout.addWidget(self.label("update_note", "muted", True))
        automatic = ContrastCheckBox(self.t("update_auto"))
        automatic.setToolTip(wrapped_tip(self.t("tip_update_auto")))
        automatic.setChecked(self.option("check_updates", False))
        automatic.toggled.connect(lambda checked: self.settings.setValue("check_updates", checked))
        update_layout.addWidget(automatic)
        check_updates = QPushButton(self.t("update_check"))
        check_updates.setIcon(ui_icon("resume", self.icon_color))
        check_updates.clicked.connect(lambda: self.check_updates())
        update_layout.addWidget(check_updates, 0, Qt.AlignmentFlag.AlignLeft)
        update_layout.addStretch()
        self.tabs.addTab(updates, self.t("updates"))
        self.tabs.setTabToolTip(4, wrapped_tip(self.t("update_note")))
        self.tabs.setCurrentIndex(previous_tab)
        layout.addWidget(self.tabs, 1)
        layout.addWidget(self.label("settings_saved", "muted", True))
        self.setCentralWidget(root)
        self.refresh_shortcuts()

    def check_updates(self, quiet=False):
        if self.quitting:
            return
        if self.update_dialog is not None:
            if not quiet:
                self.update_dialog.raise_()
                self.update_dialog.activateWindow()
            return
        if quiet:
            if self.update_job:
                return
            self.update_job = UpdateJob()
            self.update_job.done.connect(self.background_update_finished)
            self.update_job.start()
            return
        if self.update_job:
            self.update_job.cancel()
            self.update_job = None
        self.update_dialog = UpdateDialog(self)
        self.update_dialog.finished.connect(self.update_finished)
        self.update_dialog.open()

    def background_update_finished(self, job, result):
        if job is not self.update_job:
            return
        self.update_job = None
        if result.get("state") == "available" and not self.quitting:
            self.pending_update = result["release"]
            QTimer.singleShot(0, self.present_pending_update)

    def present_pending_update(self):
        if not self.pending_update or self.quitting:
            return
        if self.update_dialog:
            self.pending_update = None
            return
        if self.recording or self.overlays or self.review_dialog or self.capture_pending:
            QTimer.singleShot(1000, self.present_pending_update)
            return
        self.update_dialog = UpdateDialog(self, initial_release=self.pending_update)
        self.pending_update = None
        self.update_dialog.finished.connect(self.update_finished)
        self.update_dialog.open()

    def update_finished(self, result):
        self.update_dialog = None

    @property
    def icon_color(self):
        return theme_colors(self.theme)["fg"]

    def option(self, key, default=False):
        return self.settings.value(key, default, type=bool)

    def change_startup(self, enabled):
        try:
            self.startup.set_enabled(enabled)
            self.settings.setValue("start_windows", enabled)
        except OSError as error:
            self.startup_check.blockSignals(True)
            self.startup_check.setChecked(self.startup.enabled())
            self.startup_check.blockSignals(False)
            QMessageBox.warning(self, self.t("error"), self.t("startup_error", detail=str(error)))

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
        QTimer.singleShot(0, self.rebuild_tray)

    def change_theme(self, theme):
        if theme == self.theme or theme not in ("light", "dark"):
            return
        self.theme = theme
        self.settings.setValue("theme", theme)
        apply_theme(theme)
        QTimer.singleShot(0, self.rebuild_ui)
        QTimer.singleShot(0, self.rebuild_tray)

    def shortcut_controls(self, mode):
        if mode == "record":
            return self.record_hotkeys, self.record_hotkey_editor, self.record_hotkey_enabled, self.record_shortcuts, "record"
        if mode:
            return self.full_hotkeys, self.full_hotkey_editor, self.full_hotkey_enabled, self.full_shortcuts, "full"
        return self.hotkeys, self.hotkey_editor, self.hotkey_enabled, self.shortcuts, "capture"

    def refresh_shortcuts(self):
        for mode in (False, True, "record"):
            controller, editor, checkbox, status, prefix = self.shortcut_controls(mode)
            enabled = self.option(prefix + "_hotkey_enabled", prefix != "full")
            labels = [label for _, label in controller.registered]
            text = " · ".join(labels) if labels else self.t("shortcut_unavailable" if enabled else "button_only")
            extra = [label for label in labels if label != editor.keySequence().toString(QKeySequence.SequenceFormat.PortableText)]
            status.setText(" · ".join(extra) if labels else text)
            status.setVisible(not labels or bool(extra))
            if mode == "record":
                description, button = self.t("record_tip"), self.record_button
            elif mode:
                description = self.t("tip_full_save" if self.settings.value("full_action", "edit") == "save" else "tip_full_edit")
                button = self.full_button
            else:
                description, button = self.t("tip_area"), self.capture_button
            if labels:
                description += "\n" + " · ".join(labels)
            button.setToolTip(wrapped_tip(description))
            editor.setToolTip(wrapped_tip(self.t("tip_hotkey") + "\n" + text))

    def rebuild_tray(self):
        self.tray.setToolTip(self.t("tip_tray"))
        old_menu = self.tray.contextMenu()
        menu = QMenu(self)
        menu.setToolTipsVisible(True)
        for key, callback in [("capture", lambda: self.start_capture()),
                              ("full_capture", lambda: self.start_capture("full")),
                              ("record_stop", self.stop_recording) if self.recording else
                              ("record", lambda: self.record_controls.primary_action() if self.record_controls else self.start_capture("record")),
                              ("open", self.show_main), ("quit", self.quit_app)]:
            icon = {"full_capture": "monitor", "record": "video", "record_stop": "cancel"}.get(key, key)
            tip = {"capture": "tip_area", "record": "record_tip",
                   "full_capture": "tip_full_save" if self.settings.value("full_action") == "save" else "tip_full_edit"}.get(key, key)
            action = QAction(ui_icon(icon, self.icon_color), self.t(key), menu)
            action.setToolTip(wrapped_tip(self.t(tip)))
            if key in ("capture", "full_capture"):
                action.setEnabled(self.recording is None)
            action.triggered.connect(callback)
            menu.addAction(action)
        self.tray.setContextMenu(menu)
        if old_menu:
            old_menu.deleteLater()

    def hotkey_capture(self, mode="region"):
        focus = QApplication.focusWidget()
        for editor in (self.hotkey_editor, self.full_hotkey_editor, self.record_hotkey_editor):
            if focus and (focus is editor or editor.isAncestorOf(focus)):
                return
        if mode == "record" and self.record_controls:
            self.record_controls.primary_action()
            return
        self.start_capture(mode)

    def apply_hotkey(self, full=False):
        controller, editor, checkbox, status, prefix = self.shortcut_controls(full)
        if not checkbox.isChecked():
            controller.close()
            self.settings.setValue(prefix + "_hotkey_enabled", False)
            self.refresh_shortcuts()
            return
        sequence = editor.keySequence()
        try:
            binding = native_hotkey(sequence)
            others = (other for other in (self.hotkeys, self.full_hotkeys, self.record_hotkeys) if other is not controller)
            accepted = all(binding not in other.bindings.values() for other in others) and controller.replace(sequence)
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
        if self.review_dialog is not None:
            self.review_dialog.show()
            self.review_dialog.raise_()
            self.review_dialog.activateWindow()
            return
        if self.recording and self.record_controls:
            self.record_controls.show()
            self.record_controls.raise_()
            return
        if self.overlays or self.capture_pending:
            return
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.start_capture()

    def start_capture(self, mode="region"):
        if self.review_dialog is not None:
            self.show_main()
            return
        if self.recording:
            self.show_main()
            return
        if self.overlays or self.capture_pending:
            return
        self.capture_mode = mode
        self.capture_pending = True
        self.restore_window = self.isVisible()
        self.capture_button.setEnabled(False)
        self.full_button.setEnabled(False)
        self.record_button.setEnabled(False)
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
            if self.capture_mode == "record" or (self.capture_mode == "region" and len(QApplication.screens()) > 1):
                self.capture_desktop()
                return
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
            self.record_button.setEnabled(True)

    def capture_desktop(self):
        bounds = desktop_bounds()
        grab = DesktopGrab(bounds)
        try:
            pix = QPixmap.fromImage(grab.frame(self.option("include_cursor")))
        finally:
            grab.close()
        cls = RecordingOverlay if self.capture_mode == "record" else CaptureOverlay
        overlay = cls(DesktopSurface(bounds), pix, self.lang, self.theme)
        self.overlays.append(overlay)
        if isinstance(overlay, RecordingOverlay):
            overlay.selection_ready.connect(self.update_recording_bar)
        overlay.finished.connect(self.finish_capture)
        overlay.chosen.connect(self.choose_overlay)
        overlay.show()
        place_desktop_overlay(overlay, bounds)
        if self.option("remember_area"):
            saved = self.settings.value("last_area", {})
            if isinstance(saved, dict) and saved.get("screen") == overlay.screen_key:
                try:
                    values = saved["native_rect"]
                    r = QRect(*values).intersected(bounds)
                    if r.width() >= 5 and r.height() >= 5:
                        overlay.selection = QRectF((r.x()-bounds.x())/overlay.scale,
                            (r.y()-bounds.y())/overlay.scale, r.width()/overlay.scale, r.height()/overlay.scale)
                        overlay.position_panel()
                except (KeyError, TypeError, ValueError):
                    pass
        overlay.raise_()
        overlay.activateWindow()
        overlay.setFocus()
        if self.record_controls:
            self.record_controls.raise_()

    def update_recording_bar(self, overlay):
        if overlay.selection.width() < 4 or overlay.selection.height() < 4:
            self.dismiss_recording_bar()
            return
        rect = selected_native_rect(overlay)
        if self.record_controls is None:
            self.record_controls = RecordingControls(self, rect=rect)
            self.record_controls.start_requested.connect(self.start_selected_recording)
            self.record_controls.cancel_requested.connect(lambda: self.finish_capture("cancel", None))
        self.record_controls.set_region(rect)

    def start_selected_recording(self):
        selected = next((w for w in self.overlays if isinstance(w, RecordingOverlay)), None)
        if selected and self.record_controls and self.record_controls.safe_to_record():
            selected.complete("record")

    def dismiss_recording_bar(self):
        if self.record_controls:
            self.record_controls.dispose()
            self.record_controls.deleteLater()
            self.record_controls = None

    def begin_recording(self, rect):
        self.capture_pending = False
        if self.quitting:
            return
        recording = None
        try:
            # Load optional audio dependencies before starting an output file.
            import numpy
            import soundcard
            self.recording_draft = VideoDraft()
            path = self.recording_draft.path
            recording = VideoRecording(rect, path, self.option("include_cursor"), self)
            self.recording = recording
            recording.finished.connect(self.recording_finished)
            if self.record_controls is None:
                self.record_controls = RecordingControls(self, rect=rect)
                self.record_controls.set_region(rect)
            self.record_controls.attach_recording(recording)
            if not self.record_controls.safe_to_record():
                raise RuntimeError(self.t("record_hide_blocked"))
            for key in ("microphone", "system_audio"):
                recording.set_audio(key, self.option(key))
            self.rebuild_tray()
            # Allow the control window's capture exclusion to reach the compositor.
            QTimer.singleShot(180, recording.start)
        except Exception as error:
            if recording:
                recording.error = str(error)
                recording.stop()
            else:
                self.recording = None
                if self.recording_draft:
                    self.recording_draft.cleanup()
                    self.recording_draft = None
                self.dismiss_recording_bar()
                self.show_main()
                QMessageBox.warning(self, self.t("error"), self.t("record_error", detail=str(error)))

    def stop_recording(self):
        if self.record_controls:
            self.record_controls.stop()

    def recording_finished(self, path, error):
        old = self.recording
        self.recording = None
        self.dismiss_recording_bar()
        if old:
            old.deleteLater()
        self.rebuild_ui()
        self.rebuild_tray()
        if error:
            if self.recording_draft:
                self.recording_draft.cleanup()
                self.recording_draft = None
            QMessageBox.warning(self, self.t("error"), self.t("record_error", detail=error))
        else:
            draft = self.recording_draft
            if draft is not None:
                dialog = VideoReview(draft, self.folder, self.lang, self)
                self.review_dialog = dialog
                dialog.saved.connect(lambda saved: self.notify_result(self.t("record_saved", path=saved)))
                dialog.finished.connect(lambda result, view=dialog, video=draft: self.review_finished(view, video))
                dialog.show()
                dialog.raise_()
                dialog.player.play()
                return
        if self.quit_after_recording:
            self.quit_app()
        elif self.restore_window:
            self.show_main()

    def review_finished(self, dialog, draft):
        dialog.release_player()
        dialog.deleteLater()
        if self.review_dialog is dialog:
            self.review_dialog = None
            self.recording_draft = None
        draft.cleanup()
        if self.quit_after_recording:
            self.quit_app()
        elif self.restore_window:
            self.show_main()

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

    def close_overlays(self, keep_recording_bar=False):
        if not keep_recording_bar and not self.recording:
            self.dismiss_recording_bar()
        for overlay in self.overlays:
            overlay.close()
        self.overlays.clear()

    def finish_capture(self, action, image):
        selected = self.sender()
        if not isinstance(selected, CaptureOverlay):
            selected = next((w for w in self.overlays if w.isVisible() and not w.selection.isEmpty()), None)
        if action == "record" and selected:
            rect = selected_native_rect(selected)
            if rect.width() < 4 or rect.height() < 4:
                return
            if self.record_controls:
                self.record_controls.set_preparing()
            self.close_overlays(keep_recording_bar=True)
            self.capture_pending = True
            QTimer.singleShot(260, lambda: self.begin_recording(rect))
            return
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
                saved = {"screen": selected.screen_key, "rect": [r.x(), r.y(), r.width(), r.height()]}
                if hasattr(selected, "native_bounds"):
                    saved["native_rect"] = list(selected_native_rect(selected).getRect())
                self.settings.setValue("last_area", saved)
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
        if self.review_dialog is not None:
            dialog = self.review_dialog
            self.quit_after_recording = True
            dialog.reject()
            if self.review_dialog is not None and not dialog.saving and not dialog.allow_close:
                self.quit_after_recording = False
            return
        if self.recording:
            self.quit_after_recording = True
            self.stop_recording()
            return
        self.quitting = True
        self.close_overlays()
        self.tray.hide()
        self.hotkeys.close()
        self.full_hotkeys.close()
        self.record_hotkeys.close()
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
        socket.write(b"tray" if "--tray" in sys.argv else b"show")
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
            def request():
                if bytes(connection.readAll()) == b"show":
                    window.show_main()
                connection.disconnectFromServer()
                connection.deleteLater()
            connection.readyRead.connect(request)
            if connection.bytesAvailable():
                request()
    server.newConnection.connect(connected)
    app.aboutToQuit.connect(window.hotkeys.close)
    app.aboutToQuit.connect(window.full_hotkeys.close)
    app.aboutToQuit.connect(window.record_hotkeys.close)
    if "--tray" not in sys.argv or not window.tray.isVisible():
        window.show()
    return app.exec()


def check_installation(report_path):
    """Optional packaging check using synthetic pixels; no screen/audio capture."""
    import tempfile
    import traceback
    result = {"ok": False}
    try:
        os.environ["QT_QPA_PLATFORM"] = "offscreen"
        application = QApplication.instance() or QApplication([])
        from PySide6.QtMultimedia import QMediaPlayer, QVideoSink
        import soundcard
        import numpy
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "synthetic.mp4"
            class SyntheticGrab:
                def __init__(self, rect):
                    self.size = rect.size()
                def frame(self, cursor=False):
                    image = QImage(self.size, QImage.Format.Format_RGB32)
                    image.fill(QColor("#118769"))
                    return image
                def close(self):
                    pass
            recording = VideoRecording(QRect(0, 0, 321, 241), path, grab_factory=SyntheticGrab)
            completed = []
            recording.finished.connect(lambda saved, error: completed.append(error))
            recording.start()
            QTimer.singleShot(1200, recording.stop)
            deadline = time.monotonic()+15
            while not completed and time.monotonic() < deadline:
                application.processEvents()
                time.sleep(.005)
            if not completed or completed[0]:
                raise RuntimeError(str(completed) or "Encoder timeout")
            player, sink, frames = QMediaPlayer(), QVideoSink(), []
            player.setVideoSink(sink)
            sink.videoFrameChanged.connect(lambda frame: frames.append(frame.toImage()) if frame.isValid() else None)
            player.setSource(QUrl.fromLocalFile(str(path)))
            player.play()
            deadline = time.monotonic()+10
            while not frames and time.monotonic() < deadline:
                application.processEvents()
                time.sleep(.005)
            player.stop()
            player.setSource(QUrl())
            if not frames or frames[0].size() != QSize(322, 242):
                raise RuntimeError("Bundled video decoder failed: " + player.errorString())
            from PySide6.QtGui import QFontDatabase
            QFontDatabase.addApplicationFont(str(Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts/segoeui.ttf"))
            ocr_image = QImage(800, 160, QImage.Format.Format_RGB32)
            ocr_image.fill(QColor("white"))
            ocr_painter = QPainter(ocr_image)
            ocr_painter.setPen(QColor("black"))
            ocr_painter.setFont(QFont("Segoe UI", 28))
            ocr_painter.drawText(25, 85, "LumaShot OCR test 123")
            ocr_painter.end()
            ocr_result = recognize_text(ocr_image)
            if ocr_result.get("ok"):
                if any(v["tag"].startswith("en") for v in ocr_result["languages"]):
                    ocr_result = recognize_text(ocr_image, "en-US")
                    if ocr_result.get("text") != "LumaShot OCR test 123":
                        raise RuntimeError("Bundled OCR did not recognize generated text")
                result["ocr"] = True
            elif ocr_result.get("code") == "no_languages":
                result["ocr"] = "No installed Windows OCR language packs"
            else:
                raise RuntimeError("Bundled OCR backend failed")
            if release_installer({"tag_name": "v4", "assets": [{"name":"LumaShot-Setup-0.4.0-Windows-x64.zip", "size":100,
                "browser_download_url":"https://github.com/TOKKAB1/LumaShot/releases/download/v4/LumaShot-Setup-0.4.0-Windows-x64.zip"}]})["version"] != "0.4.0":
                raise RuntimeError("Update version parsing failed")
            result["update_version_parser"] = True
            draft = VideoDraft()
            try:
                shutil.copyfile(path, draft.path)
                review = VideoReview(draft, folder, "en")
                review.audio.setMuted(True)
                review.player.play()
                deadline = time.monotonic()+10
                while review.video_image.isNull() and time.monotonic() < deadline:
                    application.processEvents()
                    time.sleep(.005)
                if review.video_image.isNull():
                    raise RuntimeError("Bundled preview did not display a video frame")
                review.save_default()
                deadline = time.monotonic()+10
                while review.saved_path is None and review.saving and time.monotonic() < deadline:
                    application.processEvents()
                    time.sleep(.005)
                if review.saved_path is None or Path(review.saved_path).read_bytes() != path.read_bytes():
                    raise RuntimeError("Bundled preview save failed")
                review.release_player()
                review.allow_close = True
                review.close()
                review.deleteLater()
                application.processEvents()
            finally:
                draft.cleanup()
            result.update(ok=True, video_bytes=path.stat().st_size,
                          decoded_size=[frames[0].width(), frames[0].height()],
                          preview_and_save=True,
                          numpy=numpy.__version__, frozen=bool(getattr(sys, "frozen", False)))
    except Exception:
        result["error"] = traceback.format_exc()
    Path(report_path).write_text(json.dumps(result, indent=2), encoding="utf-8")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--check-installation":
        sys.exit(check_installation(sys.argv[2]))
    sys.exit(main())
