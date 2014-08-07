from Record import Record
from RecordWindow import RecordWindow
from RecordCreate import RecordCreate
import csv

class RecordController:
	def __init__(self):
		self.record_list = []
		self.record_window = RecordWindow(self)
		self.record_create = RecordCreate(self.record_list)

	def AddRecord(self, source, type_source, report_date, pages, comment):
		self.record_list.append(Record(source, type_source, report_date, pages, comment))
		self.record_window.list_ctrl.SetObjects(self.record_list)

	def DeleteRecord(self, index):
		self.record_list.pop(index)
		self.record_window.list_ctrl.SetObjects(self.record_list)

	def CreateRecordReport(self):
		self.record_create.CreateTable()

	def SaveRecordReport(self):
		source = []
		type_source = []
		date = []
		pages = []
		comment = []

		for record in self.record_list:
			source.append(record.source)
			type_source.append(record.type_source)
			date.append(record.date)
			pages.append(record.pages)
			comment.append(record.comment)

		save_file = open('record report.txt', 'wb')
		writer = csv.writer(save_file)
		writer.writerow(source)
		writer.writerow(type_source)
		writer.writerow(date)
		writer.writerow(pages)
		writer.writerow(comment)