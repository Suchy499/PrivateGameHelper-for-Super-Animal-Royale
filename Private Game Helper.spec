# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['.\\src\\__main__.py'],
    pathex=['.\\.venv\\Lib\\site-packages'],
    binaries=[],
    datas=[('.\\src\\core\\presets.json', 'core'), ('.\\src\\images\\rc_images.qrc', 'images'), ('.\\src\\styles\\styles', 'styles\\styles')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Private Game Helper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['.\\icon.ico'],
    contents_directory='data',
    hide_console='hide-early',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Private Game Helper',
)
