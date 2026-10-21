<p align="center">
  <img src="assets/icon.png" width="88" height="88" alt="LumaShot icon">
</p>
<h1 align="center">LumaShot</h1>
<p align="center"><strong>A screenshot. Just how you need it.</strong></p>
<p align="center">A compact Windows screenshot tool built with Python and PySide6.<br>Select an area, add clear annotations, and copy or save it.</p>
<p align="center">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-desktop-118769">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-118769"></a>
  <img alt="Python 3.10 or newer" src="https://img.shields.io/badge/Python-3.10%2B-3776AB">
  <img alt="PySide6" src="https://img.shields.io/badge/GUI-PySide6-41CD52">
  <img alt="Languages: Romanian, Russian, English" src="https://img.shields.io/badge/Languages-RO%20%7C%20RU%20%7C%20EN-118769">
</p>
<p align="center">
  <a href="docs/README.ro.md">Română</a> ·
  <a href="docs/README.ru.md">Русский</a> · <strong>English</strong>
</p>
<p align="center">
  <a href="https://github.com/TOKKAB1/LumaShot/raw/refs/heads/main/LumaShot.py">Download Python file</a> ·
  <a href="https://github.com/TOKKAB1/LumaShot/raw/refs/heads/main/LumaShot.ico">Download Windows icon</a> ·
  <a href="https://github.com/TOKKAB1/LumaShot/issues">Report a problem</a>
</p>

![LumaShot's compact interface in English](assets/interface-en.png)

## Made for quick explanations

LumaShot takes inspiration from Lightshot's direct selection workflow and useful annotation tools found in Greenshot. It is an independent personal project, with its own interface and icon.

| Capture | Annotate | Keep |
|---|---|---|
| Select a region on any monitor | Pen, line, arrow and rectangle | Copy the finished image |
| Print Screen or Ctrl+Shift+F9 | Text, translucent highlight and numbered steps | Save as PNG or JPEG |
| Move or resize the selection | Undo and redo | Choose your screenshot folder |

**Romanian, Russian and English** are built in. Choose your language and a light or dark appearance in **General**; both choices are remembered.

The toolbar uses [Lucide](https://lucide.dev/) icons. The 22 SVGs are embedded in the Python file, rendered at several sizes and cached for reuse. No icon download or extra icon package is needed at runtime.

## Get started

Download the full source from **Code → Download ZIP**, or use the single-file download below. Anyone may use, modify and redistribute the original LumaShot code under the [MIT license](LICENSE), including commercially, provided the license and copyright notice are retained.

Requires **Windows**, **Python 3.10+** and **PySide6**. Development and local tests were run on Windows with Python 3.14 and PySide6 6.12.0.

Download [`LumaShot.py`](LumaShot.py), open a terminal in its folder, then run:

```powershell
python -m pip install PySide6==6.12.0
python LumaShot.py
```

The application lives in **one Python file**. There is no installer or executable release in this version. The `.ico` file is optional: the app draws its own icon even when you only download the script.

<details>
<summary>Prefer a separate Python environment?</summary>

```powershell
git clone https://github.com/TOKKAB1/LumaShot.git
cd LumaShot
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe LumaShot.py
```

</details>

## Capture and annotate

Click **Select an area**, left-click the tray icon, or use an available global shortcut. Drag to select an area, then choose a tool from the floating toolbar. Copy with **Ctrl+C** or save with **Ctrl+S**.

The compact editor has a vertical tool strip beside the selection and a small action strip below it. Click the current color to open the palette; choosing a color closes it again. The palette also contains custom colors and stroke width. Ellipse and redaction are no longer offered in the toolbar or its shortcuts.

### Set your own shortcut

In **Global shortcuts → Area capture**, click the shortcut field, press your desired combination and click **Apply**. The choice replaces the default shortcuts and is remembered after restarting. If the combination is occupied or reserved by Windows, an error appears and the previous shortcut stays active. If a saved shortcut is unavailable at startup, use the capture button and choose another combination.

Enable or disable each shortcut with its checkbox and confirm with **Apply**. The full-screen shortcut is optional and starts disabled; its suggested combination is `Ctrl+Shift+F10`. Disabling a shortcut keeps the corresponding capture button available.

Use a combination such as `Ctrl+Alt+K`, an F key, or `Print Screen`. Sequences of multiple combinations and plain letter shortcuts are not accepted.

![The LumaShot editor displaying annotated sample content](assets/editor-demo.png)

*The screenshots show the current Qt interface. The editor example uses synthetic content, not a user's desktop.*

| Key | Action |
|---|---|
| `Print Screen` / `Ctrl+Shift+F9` | Start a capture, when available |
| `V` | Move the selection or resize it using the corners |
| `P` / `L` / `A` | Pen / line / arrow |
| `R` | Rectangle |
| `T` | Add text; Enter confirms it |
| `H` / `N` | Highlight / numbered step |
| `Ctrl+Z` / `Ctrl+Y` | Undo / redo an annotation |
| `Ctrl+C` / `Enter` | Copy the image |
| `Ctrl+S` | Save the image |
| `Esc` / right-click | Cancel the capture |

When a text field is open, **Esc** discards that text first. Moving the selection changes the crop; annotations remain anchored to their original screen positions.

Left-click the tray icon to select an area. Right-click it for the three actions: **Select an area**, **Open LumaShot**, and **Quit**.

Closing the main window keeps LumaShot in the system tray when it is available. Right-click its petrol-green icon and choose **Quit** to exit completely. A second launch reopens the running app.

## Preferences

| Tab | Settings |
|---|---|
| General | Language, light/dark theme, copy/save notifications, remembered selection, cursor capture, destination folder |
| Global shortcuts | Enable, disable and customize the area and full-screen shortcuts independently |
| Format | Default PNG/JPEG format, JPEG quality (1–100), full-screen action |

**Full screen** captures the monitor under the cursor at capture time, at its native pixel resolution. By default it opens the editor with the whole monitor selected. In **Format → When capturing the full screen**, choose **Save immediately to folder** to skip the editor and save directly using the chosen format and quality. This behavior applies to the full-screen button and shortcut. It never uploads an image.

General and format preferences save automatically; shortcut changes require **Apply**. Remembered areas are restored after a successful copy or save on the same monitor, and clipped if its resolution changes. Full-screen captures do not replace the remembered area. Cursor capture includes the Windows cursor on its monitor; the editor controls are excluded from exported images.

![LumaShot in dark mode](assets/interface-en-dark.png)

## Local by design

- No account, cloud upload or telemetry in the application.
- Captures are saved when you choose Save or explicitly enable immediate saving for full-screen captures. Copy places the image on the Windows clipboard.
- Exports contain the selected pixels with annotations applied. They do not embed the original image or editing history.
- Windows clipboard history or cloud sync, if enabled by you, is managed by Windows.

## Windows icon

[`LumaShot.ico`](LumaShot.ico) contains **16, 24, 32, 48, 64, 128 and 256 px** versions with a transparent background.

Use it for a Windows shortcut through **Properties → Change Icon**. A `.py` file itself usually keeps the icon of its associated Python application in File Explorer.

## Current limits

This is **version 0.1**, a first usable version.

- A capture stays within one monitor. Cross-monitor selections are not supported.
- Scrolling capture, OCR and automatic window selection are not included.
- Global shortcuts can be occupied by Windows or another screenshot app. The dashboard lists successfully registered shortcuts; the capture button remains available.
- HDR displays and protected video content have not been validated.
- The application does not add itself to Windows startup.

## Development

```powershell
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

The 28 local tests cover themes, optional independent shortcuts, tray clicks, cursor routing, remembered areas, full-screen editing and instant saving, notifications, crop resolution, rendering, undo/redo, PNG/JPEG export, copy, cancelled saves, language switching, toolbar placement, the collapsed palette, shortcut persistence, conflict handling and tooltip content, sizing and dismissal. They use Qt's offscreen backend; they do not replace testing real multi-monitor or global-hotkey behavior.

| File | Purpose |
|---|---|
| [`LumaShot.py`](LumaShot.py) | Complete application |
| [`LumaShot.ico`](LumaShot.ico) | Windows icon |
| [`requirements.txt`](requirements.txt) | Python dependency |
| [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) | Lucide and Qt notices |
| [`tests/test_capture.py`](tests/test_capture.py) | Local checks |
| [`docs/`](docs/) | Romanian and Russian guides |
| [`assets/`](assets/) | Icon and interface images |

For bug reports, include your Windows version, Python version, display scaling, and steps to reproduce. Use sample screenshots without personal information.

Built with [Qt for Python / PySide6](https://doc.qt.io/qtforpython-6/) and [Lucide icons](https://lucide.dev/). Third-party licenses are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); the Lucide notices are also embedded in the standalone script. LumaShot is not affiliated with Lightshot or Greenshot.

## License and contributions

The original LumaShot application code, documentation and petrol-green app icon are offered under the [MIT license](LICENSE), with notice `Copyright (c) 2026 TOKKAB1`. The license is also embedded in the script so it travels with single-file downloads.

Bundled Lucide SVGs retain their ISC/MIT terms and notices. PySide6 and Qt are installed separately and retain their own licenses; the MIT license for LumaShot does not replace those licenses. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for sources and notices.

This repository distributes Python source and original project assets, not Lightshot or Greenshot code, logos or binaries. The project is independent of those products.

Improvements and translations are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
