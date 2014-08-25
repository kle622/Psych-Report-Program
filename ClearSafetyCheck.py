import wx

class ClearSafetyCheck(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, None, wx.ID_ANY)
		self.SetLabel('Clearing All Records')
		self.panel = wx.Panel(self)
		self.parent = parent

		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)

		self.question = wx.StaticText(self.panel, label = 'ARE YOU SURE YOU WANT TO DELETE ALL RECORDS PERMANENTLY?')
		self.question.SetFont(font)
		self.yes_button = wx.Button(self.panel, label = 'YES')
		self.yes_button.Bind(wx.EVT_BUTTON, self.ClearAllRecords)
		self.yes_button.SetFont(font)
		self.no_button = wx.Button(self.panel, label = 'NO')
		self.no_button.Bind(wx.EVT_BUTTON, self.Cancel)
		self.no_button.SetFont(font)

		self.hori_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
		self.hori_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		self.vert_sizer = wx.BoxSizer(wx.VERTICAL)

		self.hori_sizer1.Add(self.question, 0, wx.ALL | wx.EXPAND, 5)

		self.hori_sizer2.AddStretchSpacer(1)
		self.hori_sizer2.Add(self.yes_button, 2, wx.ALL | wx.EXPAND, 5)
		self.hori_sizer2.Add(self.no_button, 2, wx.ALL | wx.EXPAND, 5)
		self.hori_sizer2.AddStretchSpacer(1)

		self.vert_sizer.Add(self.hori_sizer1, 0, wx.ALL | wx.EXPAND)
		self.vert_sizer.Add(self.hori_sizer2, 0, wx.ALL | wx.EXPAND)

		self.panel.SetSizer(self.vert_sizer)
		self.vert_sizer.Fit(self)

		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Center()

	def ClearAllRecords(self, evt):
		self.parent.ClearAllRecords()
		self.Hide()

	def Cancel(self, evt):
		self.Hide()

	def OnClose(self, evt):
		self.Hide()
