import win32com.client as win32
from Record import Record

class RecordCreate:
	def __init__(self, records):
		self.records = records

	def CreateTable(self):
		self.records.sort(Record.Compare)
		word = win32.gencache.EnsureDispatch('Word.Application')
		word.Visible = True
		word.Documents.Add()
		self.global_doc = doc = word.ActiveDocument

		my_range = doc.Range(0, 0)
		doc.Tables.Add(my_range, 1, 4)
		doc.Tables(1).Cell(1, 1).Range.Text = 'Doctor/Source'
		doc.Tables(1).Cell(1, 2).Range.Text = 'Type'
		doc.Tables(1).Cell(1, 3).Range.Text = 'Report Date'
		doc.Tables(1).Cell(1, 4).Range.Text = 'Pages'

		doc.Tables(1).Cell(1, 1).Range.Bold = True
		doc.Tables(1).Cell(1, 2).Range.Bold = True
		doc.Tables(1).Cell(1, 3).Range.Bold = True
		doc.Tables(1).Cell(1, 4).Range.Bold = True

		num_pages = 0
		for r in self.records:
			self.CreateRecord(r)
			num_pages = num_pages + int(r.pages)

		my_range = doc.Range(doc.Content.End-1, doc.Content.End)
		doc.Tables.Add(my_range, 1, 4)
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 1).Range.Text = 'Total Number of Pages:'
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 2).Range.Text = str(num_pages)
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 3).Range.Text = 'Number of Hours Spent:'

		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 1).Range.Bold = True
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 3).Range.Bold = True
	def CreateRecord(self, record):
		doc = self.global_doc

		my_range = doc.Range(doc.Content.End-1, doc.Content.End)
		doc.Tables.Add(my_range, 1, 4)
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 1).Range.Text = record.source
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 2).Range.Text = record.type_source
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 3).Range.Text = record.date
		doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 4).Range.Text = record.pages

		if record.comment:
			my_range = doc.Range(doc.Content.End-1, doc.Content.End)
			doc.Tables.Add(my_range, 1, 1)
			doc.Tables(1).Cell(doc.Tables(1).Rows.Count, 1).Range.Text = record.comment

