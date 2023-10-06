# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['rename.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
a.binaries -= TOC([
    ('opengl32sw.dll', None, None),
    ('qt5dbus.dll', None, None),
    ('qt5network.dll', None, None),
    ('qt5qml.dll', None, None),
    ('qt5qmlmodels.dll', None, None),
    ('qt5quick.dll', None, None),
    ('qt5svg.dll', None, None),
    ('qt5websockets.dll', None, None),
])
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='rename',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
