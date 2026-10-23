"""Build an unsigned, portable Windows application. Run through build_exe.bat."""
from pathlib import Path
from importlib.metadata import distribution
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
from zipfile import ZipFile, ZIP_DEFLATED

VERSION = "0.4.0"
ROOT = Path(__file__).resolve().parent


def main():
    if sys.platform != "win32" or platform.machine().lower() not in ("amd64", "x86_64") or sys.maxsize <= 2**32:
        raise SystemExit("Use 64-bit Python on Windows x64 to build this release.")
    # Unrelated tools on PATH can supply incompatible DLLs with the same names
    # (for example an ICU build instead of the Windows ICU used by Qt).
    environment = os.environ.copy()
    windows = Path(os.environ.get("SystemRoot", "C:/Windows"))
    environment["PATH"] = os.pathsep.join(map(str, [Path(sys.executable).parent,
        Path(sys.base_prefix), Path(sys.base_prefix)/"DLLs", windows/"System32", windows]))
    environment.pop("PYTHONPATH", None)
    # Onedir keeps Qt shared libraries replaceable and avoids extraction on each launch.
    subprocess.run([sys.executable, "-m", "PyInstaller", "--noconfirm", "--clean",
                    "--onedir", "--windowed", "--name", "LumaShot", "--icon", str(ROOT / "LumaShot.ico"),
                    "--specpath", "build", "--distpath", "dist", "--workpath", "build/pyinstaller",
                    "--collect-all", "soundcard", "--hidden-import", "_cffi_backend",
                    "--exclude-module", "PyQt5", "--exclude-module", "PyQt6",
                    "--exclude-module", "PySide2", "LumaShot.py"], cwd=ROOT, env=environment, check=True)
    bundle = ROOT / "dist/LumaShot"
    # Explicit allowlist: never include personal JSON settings, recordings or local environments.
    for name in ("LICENSE", "THIRD_PARTY_NOTICES.md", "LumaShot.py", "LumaShot.ico",
                 "build_exe.bat", "build_release.py", "requirements.txt", "requirements-build.txt"):
        shutil.copy2(ROOT / name, bundle / name)
    shutil.copy2(ROOT / "docs/BUILD.md", bundle / "BUILD.md")
    shutil.copy2(ROOT / "docs/PORTABLE.txt", bundle / "README.txt")
    (bundle / "docs").mkdir(exist_ok=True)
    for name in ("BUILD.md", "PORTABLE.txt"):
        shutil.copy2(ROOT / "docs" / name, bundle / "docs" / name)
    licenses = bundle / "licenses"
    licenses.mkdir(exist_ok=True)
    versions = {"Python": platform.python_version(), "LumaShot": VERSION}
    for name in ("PySide6", "PySide6_Essentials", "PySide6_Addons", "shiboken6",
                 "SoundCard", "numpy", "cffi", "pycparser", "PyInstaller"):
        package = distribution(name)
        versions[name] = package.version
        for item in package.files or []:
            if any("license" in part.lower() or part.lower() in ("copying", "copying.lesser", "notice") for part in item.parts):
                src = Path(package.locate_file(item))
                if src.is_file():
                    dest = licenses / name / str(item).replace("../", "")
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dest)
    python_license = Path(sys.base_prefix) / "LICENSE.txt"
    if python_license.exists():
        shutil.copy2(python_license, licenses / "Python-LICENSE.txt")
    for item in (ROOT / "licenses").glob("*"):
        if item.is_file():
            shutil.copy2(item, licenses / item.name)
    (bundle / "BUILD-INFO.json").write_text(json.dumps(versions, indent=2)+"\n", encoding="utf-8")
    archive = ROOT / f"dist/LumaShot-v{VERSION}-Windows-x64.zip"
    with ZipFile(archive, "w", ZIP_DEFLATED) as output:
        for item in sorted(bundle.rglob("*")):
            if item.is_file() and not item.name.startswith("LumaShot.settings.json") and item.suffix.lower() != ".mp4":
                output.write(item, item.relative_to(bundle.parent))
    with ZipFile(archive) as check:
        if check.testzip() is not None:
            raise SystemExit("ZIP integrity check failed")
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    archive.with_suffix(".sha256").write_text(f"{checksum}  {archive.name}\n", encoding="ascii")
    print(f"Created {archive} ({archive.stat().st_size / 1024**2:.1f} MB)")


if __name__ == "__main__":
    main()
