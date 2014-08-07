import wx
import sys
from RecordWindow import RecordWindow
from RecordController import RecordController

if __name__ == '__main__':
	null_log = wx.LogNull()
	app = wx.App(False)
	RecordController()
	app.MainLoop()	
	sys.exit(0)	