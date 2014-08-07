# -*- mode: python -*-
a = Analysis(['Main.py', 'Report', 'Creator'],
             pathex=['C:\\Users\\Kevin\\Desktop\\Psych Report Program'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Record.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
