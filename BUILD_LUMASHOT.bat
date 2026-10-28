@echo off
setlocal EnableExtensions DisableDelayedExpansion
rem Standalone builder. Place next to LumaShot.py, LumaShot.ico, requirements.txt.
rem Python build code is embedded below; no other build scripts are required.
set "PYTHONHOME="
set "PYTHONPATH="
pushd "%~dp0" || exit /b 1
set "BUILD_PYTHON=.lumashot-build\venv\Scripts\python.exe"

echo.
echo ============================================================
echo LumaShot - construirea unui singur EXE
echo ============================================================
echo.
for %%F in ("LumaShot.py" "LumaShot.ico" "requirements.txt") do (
    if not exist "%%~F" (
        echo [EROARE] Lipseste "%%~F" de langa acest BAT.
        goto failed
    )
)

if exist "%BUILD_PYTHON%" goto check_python
echo [1/3] Creez mediul separat pentru construire...
where py >nul 2>&1
if errorlevel 1 goto fallback_python
py -3 -c "import sys,platform; sys.exit(0 if sys.version_info >= (3,10) and sys.maxsize > 2**32 and platform.machine().lower() in ('amd64','x86_64') else 1)" >nul 2>&1
if errorlevel 1 goto fallback_python
py -3 -m venv ".lumashot-build\venv"
if errorlevel 1 goto failed
goto check_python

:fallback_python
where python >nul 2>&1
if errorlevel 1 goto no_python
python -c "import sys,platform; sys.exit(0 if sys.version_info >= (3,10) and sys.maxsize > 2**32 and platform.machine().lower() in ('amd64','x86_64') else 1)" >nul 2>&1
if errorlevel 1 goto no_python
python -m venv ".lumashot-build\venv"
if errorlevel 1 goto failed

:check_python
"%BUILD_PYTHON%" -c "import sys,platform; sys.exit(0 if sys.platform == 'win32' and sys.version_info >= (3,10) and sys.maxsize > 2**32 and platform.machine().lower() in ('amd64','x86_64') else 1)"
if errorlevel 1 (
    echo [EROARE] Mediul existent nu poate fi folosit cu acest Python.
    echo Redenumeste dosarul .lumashot-build si porneste din nou BAT-ul.
    goto failed
)

echo [2/3] Instalez sau verific bibliotecile de construire...
echo Este necesar internet pentru descarcarea bibliotecilor.
"%BUILD_PYTHON%" -m pip --require-virtualenv --disable-pip-version-check install -r "requirements.txt" "PyInstaller==6.22.3"
if errorlevel 1 goto failed

echo [3/3] Construiesc LumaShot.exe...
"%BUILD_PYTHON%" -c "import pathlib,sys; p=pathlib.Path(sys.argv[1]); lines=p.read_text(encoding='utf-8-sig').splitlines(); exec(compile('\n'.join(lines[lines.index('# LUMASHOT_BUILD_PYTHON')+1:]),str(p),'exec'))" "%~f0"
if errorlevel 1 goto failed

echo.
echo ============================================================
echo GATA: "%~dp0LumaShot.exe"
echo EXE-ul este langa LumaShot.py si nu necesita Python instalat.
echo Nu necesita un dosar _internal alaturi.
echo Versiunea si iconita sunt preluate din sursa si LumaShot.ico.
echo Fisierele de lucru raman in dosarul .lumashot-build.
echo ============================================================
popd
if /I not "%~1"=="--no-pause" pause
exit /b 0

:no_python
echo [EROARE] Este necesar Python 3.10 sau mai nou, Windows x64.
echo Instaleaza Python cu optiunea Python Launcher sau Add Python to PATH.
goto failed

:failed
echo.
echo [EROARE] Construirea nu a reusit. Verifica mesajele de mai sus.
echo Nu folosi un EXE mai vechi ca rezultat al acestei incercari.
popd
if /I not "%~1"=="--no-pause" pause
exit /b 1

# LUMASHOT_BUILD_PYTHON
import ast
import os
import re
import subprocess
import sys
import traceback
from pathlib import Path


def build():
    root = Path(sys.argv[1]).resolve().parent
    work = root / '.lumashot-build'
    work.mkdir(exist_ok=True)
    source = root / 'LumaShot.py'
    tree = ast.parse(source.read_text(encoding='utf-8-sig'), filename=str(source))
    version = None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == 'APP_VERSION'
            for target in node.targets
        ):
            version = ast.literal_eval(node.value)
            break
    if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('LumaShot.py trebuie sa contina APP_VERSION = "X.Y.Z".')
    numbers = tuple(map(int, version.split('.'))) + (0,)
    if any(value > 65535 for value in numbers):
        raise ValueError('Numerele versiunii trebuie sa fie intre 0 si 65535.')

    from PyInstaller.utils.win32.versioninfo import (
        FixedFileInfo, StringFileInfo, StringStruct, StringTable,
        VarFileInfo, VarStruct, VSVersionInfo,
    )
    strings = {
        'CompanyName': 'TOKKAB1',
        'FileDescription': 'LumaShot',
        'FileVersion': version,
        'ProductName': 'LumaShot',
        'ProductVersion': version,
        'OriginalFilename': 'LumaShot.exe',
        'LegalCopyright': 'Copyright (c) 2026 TOKKAB1',
    }
    info = VSVersionInfo(
        ffi=FixedFileInfo(filevers=numbers, prodvers=numbers, mask=0x3f,
                          flags=0, OS=0x40004, fileType=0x1, subtype=0, date=(0, 0)),
        kids=[StringFileInfo([StringTable('040904b0', [
            StringStruct(key, value) for key, value in strings.items()
        ])]), VarFileInfo([VarStruct('Translation', [1033, 1200])])],
    )
    version_file = work / 'version_info.txt'
    version_file.write_text(str(info), encoding='utf-8')

    # Prevent unrelated applications on PATH from supplying incompatible Qt DLLs.
    environment = os.environ.copy()
    windows = Path(os.environ.get('SystemRoot', 'C:/Windows'))
    environment['PATH'] = os.pathsep.join(map(str, [
        Path(sys.executable).parent, Path(sys.base_prefix),
        Path(sys.base_prefix) / 'DLLs', windows / 'System32', windows,
    ]))
    for key in ('PYTHONPATH', 'PYTHONHOME', 'QT_PLUGIN_PATH', 'QT_QPA_PLATFORM_PLUGIN_PATH'):
        environment.pop(key, None)
    print(f'Construiesc LumaShot {version}...', flush=True)
    subprocess.run([
        sys.executable, '-m', 'PyInstaller', '--noconfirm', '--clean',
        '--onefile', '--windowed', '--noupx', '--name', 'LumaShot',
        '--icon', str(root / 'LumaShot.ico'), '--version-file', str(version_file),
        '--specpath', str(work), '--distpath', str(work / 'output'),
        '--workpath', str(work / 'pyinstaller'),
        '--collect-all', 'soundcard', '--hidden-import', '_cffi_backend',
        '--exclude-module', 'PyQt5', '--exclude-module', 'PyQt6',
        '--exclude-module', 'PySide2', str(source),
    ], cwd=root, env=environment, check=True)
    executable = work / 'output' / 'LumaShot.exe'
    if not executable.is_file() or executable.stat().st_size == 0:
        raise RuntimeError('Compilarea nu a produs un executabil.')
    # Replace the previous EXE only after compilation succeeds. A running EXE
    # cannot be replaced on Windows; report the error and keep both files.
    try:
        os.replace(executable, root / 'LumaShot.exe')
    except PermissionError:
        raise RuntimeError(
            'Inchide LumaShot inclusiv din tray si porneste BAT-ul din nou. '
            f'EXE-ul nou este pastrat in: {executable}'
        ) from None
    print(f'EXE creat: {root / "LumaShot.exe"}', flush=True)


try:
    build()
except Exception:
    traceback.print_exc()
    sys.exit(1)
