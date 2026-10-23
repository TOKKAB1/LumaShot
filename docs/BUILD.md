# Build the Windows application

## Română

Descarcă întregul proiect și extrage ZIP-ul. Instalează Python 3.10+ pe 64 de biți pentru Windows, apoi apasă de două ori pe **build_exe.bat**. Prima construire necesită internet pentru descărcarea bibliotecilor.

Executabilul apare în **dist/LumaShot/LumaShot.exe**. Pentru distribuire sau GitHub Releases folosește **dist/LumaShot-v0.4.0-Windows-x64.zip** și fișierul `.sha256` alăturat. Arhiva include executabilul, bibliotecile, codul și licențele. Ceilalți utilizatori nu au nevoie de Python; trebuie să extragă întregul dosar, inclusiv **_internal**.

## English

Download and extract the complete source repository. Install 64-bit Python 3.10+ on Windows x64, then double-click **build_exe.bat**. The script creates an isolated `.build-venv`, installs the pinned build requirements and uses PyInstaller to create a windowed portable application.

Output: **dist/LumaShot/LumaShot.exe**. Distribute **dist/LumaShot-v0.4.0-Windows-x64.zip** and its `.sha256` checksum. Extract the entire archive; the executable requires the accompanying **_internal** directory. No administrator privileges or separate Python installation are required to run it. Keep the application in a writable folder so preferences can be saved beside the executable.

For unattended builds: `build_exe.bat --no-pause`. Builds update `build/` and `dist/LumaShot/`; do not store captures there. Rebuild the executable from the included source after modifying it. Qt and other shared libraries remain in `_internal` and can be replaced with compatible builds. Dependency versions are recorded in `BUILD-INFO.json`; notices are in `licenses/`. LumaShot's MIT license applies to its own code, not to dependencies.

The executable is unsigned. This build does not create an installer or a single self-extracting file. Build behavior follows the [PyInstaller documentation](https://pyinstaller.org/en/stable/usage.html).

## Русский

Скачайте и распакуйте весь проект. Установите 64-битный Python 3.10+ для Windows и запустите **build_exe.bat**. Для первой сборки нужен интернет.

Программа появится в **dist/LumaShot/LumaShot.exe**. Для GitHub Releases используйте **dist/LumaShot-v0.4.0-Windows-x64.zip** и файл `.sha256`. Пользователям Python не нужен: нужно распаковать весь архив вместе с папкой **_internal**. Настройки сохраняются рядом с exe, поэтому папка должна быть доступна для записи.

Diagnostic check (no desktop or microphone capture): `LumaShot.exe --check-installation report.json`. It verifies a synthetic MP4 encode/decode round trip and writes the result to the chosen JSON file.
