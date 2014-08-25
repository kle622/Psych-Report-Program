import wx
import sys
from datetime import datetime
from Record import Record
from RecordCreate import RecordCreate
from ObjectListView import ObjectListView, ColumnDefn, EVT_CELL_EDIT_FINISHED
from ClearSafetyCheck import ClearSafetyCheck

class RecordWindow(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, None, wx.ID_ANY)
		self.SetLabel('Record Report Creator')

		self.panel = wx.Panel(self)

		self.record_list = parent.record_list
		self.parent = parent

		font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

		self.list_ctrl = ObjectListView(self.panel,
			sortable = False,
			style = wx.LC_REPORT |
			wx.BORDER_SUNKEN |
			wx.LC_SINGLE_SEL
		)

		self.list_ctrl.SetFont(font)

		self.list_ctrl.cellEditMode = self.list_ctrl.CELLEDIT_DOUBLECLICK

		self.list_ctrl.SetColumns([
			ColumnDefn('Doctor/Source', 'left', 120, 'source'),
			ColumnDefn('Type', 'left', 120, 'type_source'),
			ColumnDefn('Report Date', 'left', 120, 'date'),
			ColumnDefn('Pages', 'left', 120, 'pages'),
			ColumnDefn('Comment', 'left', 120, 'comment')
		])

		self.source_text = wx.StaticText(self.panel, label = 'Doctor/Source:   ')
		self.type_text = wx.StaticText(self.panel, label = 'Type:                    ')
		self.report_date_text = wx.StaticText(self.panel, label = 'Report Date:       ')
		self.pages_text = wx.StaticText(self.panel, label = 'Pages:                 ')
		self.comment_text = wx.StaticText(self.panel, label = 'Comment:            ')

		self.source_text.SetFont(font)
		self.type_text.SetFont(font)
		self.report_date_text.SetFont(font)
		self.pages_text.SetFont(font)
		self.comment_text.SetFont(font)

		self.source_box = wx.TextCtrl(self.panel)
		self.type_box = wx.TextCtrl(self.panel)
		self.report_date_box = wx.TextCtrl(self.panel)
		self.pages_box = wx.TextCtrl(self.panel)
		self.comment_box = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE, size=(350, 100))

		self.source_box.SetFont(font)
		self.type_box.SetFont(font)
		self.report_date_box.SetFont(font)
		self.pages_box.SetFont(font)
		self.comment_box.SetFont(font)

		self.add_button = wx.Button(self.panel, label = 'Add Record')
		self.add_button.Bind(wx.EVT_BUTTON, self.AddRecord)
		self.add_button.SetFont(font)

		self.delete_button = wx.Button(self.panel, label = 'Delete Record')
		self.delete_button.Bind(wx.EVT_BUTTON, self.DeleteRecord)
		self.delete_button.SetFont(font)

		self.create_button = wx.Button(self.panel, label = 'Create Record Report')
		self.create_button.Bind(wx.EVT_BUTTON, self.CreateRecordReport)
		self.create_button.SetFont(font)

		self.clear_button = wx.Button(self.panel, label = 'Clear All Records')
		self.clear_button.Bind(wx.EVT_BUTTON, self.ClearAllRecords)
		self.clear_button.SetFont(font)

		self.status_bar = wx.StatusBar(self.panel)
		self.status_bar.SetFont(font)

		vert_sizer1 = wx.BoxSizer(wx.VERTICAL)
		vert_sizer2 = wx.BoxSizer(wx.VERTICAL)
		hor_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer3 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer4 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer5 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer6 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer7 = wx.BoxSizer(wx.HORIZONTAL)
		hor_sizer8 = wx.BoxSizer(wx.HORIZONTAL)

		hor_sizer1.Add(self.source_text, 0, wx.ALL | wx.EXPAND)
		hor_sizer1.Add(self.source_box, 0, wx.ALL | wx.EXPAND)
		hor_sizer2.Add(self.type_text, 0, wx.ALL | wx.EXPAND)
		hor_sizer2.Add(self.type_box, 0, wx. ALL | wx.EXPAND)

		hor_sizer3.Add(self.report_date_text, 0, wx.ALL | wx.EXPAND)
		hor_sizer3.Add(self.report_date_box, 0, wx.ALL | wx.EXPAND)

		hor_sizer4.Add(self.pages_text, 0, wx.ALL | wx.EXPAND)
		hor_sizer4.Add(self.pages_box, 0, wx.ALL | wx.EXPAND)

		hor_sizer5.Add(self.comment_text, 0, wx.ALL | wx.EXPAND)
		hor_sizer5.Add(self.comment_box, 0, wx.ALL | wx.EXPAND)

		hor_sizer6.Add(self.add_button, 3, wx.ALL | wx.EXPAND, 5)
		hor_sizer6.AddStretchSpacer(1)
		hor_sizer6.Add(self.create_button, 3, wx.ALL | wx.EXPAND, 5)

		hor_sizer8.Add(self.delete_button, 3, wx.ALL | wx.EXPAND, 5)
		hor_sizer8.AddStretchSpacer(1)
		hor_sizer8.Add(self.clear_button, 3, wx.ALL | wx.EXPAND, 5)

		vert_sizer1.Add(self.list_ctrl, 5, wx.ALL |  wx.GROW)
		vert_sizer2.Add(hor_sizer1, 0, wx.ALL | wx.EXPAND, 5)
		vert_sizer2.AddStretchSpacer(1)
		vert_sizer2.Add(hor_sizer2, 0, wx.ALL | wx.EXPAND, 5)
		vert_sizer2.AddStretchSpacer(1)
		vert_sizer2.Add(hor_sizer3, 0, wx.ALL | wx.EXPAND, 5)
		vert_sizer2.AddStretchSpacer(1)
		vert_sizer2.Add(hor_sizer4, 0, wx.ALL | wx.EXPAND, 5)
		vert_sizer2.AddStretchSpacer(1)
		vert_sizer2.Add(hor_sizer5, 0, wx.ALL | wx.EXPAND, 5)
		vert_sizer2.AddStretchSpacer(1)
		vert_sizer2.Add(hor_sizer6, 0, wx.ALL | wx.EXPAND, 5)
		vert_sizer2.AddStretchSpacer(1)
		vert_sizer2.Add(hor_sizer8, 0, wx.ALL | wx.EXPAND, 5)

		hor_sizer7.AddStretchSpacer(2)
		hor_sizer7.Add(vert_sizer2, 0, wx.ALL | wx.EXPAND)
		hor_sizer7.AddStretchSpacer(2)

		vert_sizer1.Add(hor_sizer7, 0, wx.ALL | wx.EXPAND | wx.CENTER, 1)
		vert_sizer1.Add(self.status_bar, 0, wx.ALL | wx.EXPAND, 1)
		self.panel.SetSizer(vert_sizer1)
		vert_sizer1.Fit(self)
		self.Center()
		self.Show()
		self.safety_check = ClearSafetyCheck(self.parent)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Bind(EVT_CELL_EDIT_FINISHED, self.SaveOnEdit)

	def AddRecord(self, evt):
		source = self.source_box.GetValue()
		type_source = self.type_box.GetValue()
		report_date = self.report_date_box.GetValue()
		pages = self.pages_box.GetValue()
		comment = self.comment_box.GetValue()

		try:
			datetime.strptime(report_date, '%m/%d/%y')
			self.parent.AddRecord(source, type_source, report_date, pages, comment)
			self.ClearTextBoxes()
			self.status_bar.SetStatusText('Record successfully added.')
		except ValueError:
			self.status_bar.SetStatusText('Invalid date format for record. Expected format: ##/##/##')
	def DeleteRecord(self, evt):
		try:
			index = self.list_ctrl.GetFocusedItem()
			self.parent.DeleteRecord(index)
			self.status_bar.SetStatusText('Record successfully deleted.')
		except IndexError:
			self.status_bar.SetStatusText('No valid record to delete.')

	def CreateRecordReport(self, evt):
		if self.parent.record_list:
			self.status_bar.SetStatusText('Loading record report, please wait.')
			self.parent.CreateRecordReport()
			self.status_bar.SetStatusText('Record report successfully created.')
		else:
			self.status_bar.SetStatusText('No records to create report from.')

	def ClearAllRecords(self, evt):
		self.safety_check.Show()

	def ClearTextBoxes(self):
		self.source_box.Clear()
		self.type_box.Clear()
		self.report_date_box.Clear()
		self.pages_box.Clear()
		self.comment_box.Clear()

	def OnClose(self, evt):
		self.Destroy()
		sys.exit(0)

	def SaveOnEdit(self, evt):
		self.parent.SaveRecordReport()
		print 'gettin here'





