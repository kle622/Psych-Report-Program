# -*- mode: python -*-
a = Analysis(['Prog', 'ClearSafetyCheck.py', 'Main.py', 'Record.py', 'RecordController.py', 'RecordCreate.py', 'RecordWindow.py'],
             pathex=['C:\\Users\\Kevin\\Documents\\GitHub\\Psych-Report-Program'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ame.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
