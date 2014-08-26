from Record import Record
from RecordWindow import RecordWindow
from RecordCreate import RecordCreate
from send2trash import send2trash
import csv
import os

class RecordController:
	def __init__(self):
		self.record_list = []
		self.record_window = RecordWindow(self)
		self.record_create = RecordCreate(self, self.record_list)
		self.LoadRecordReport()


	def AddRecord(self, source, type_source, report_date, pages, comment):
		self.record_list.append(Record(source, type_source, report_date, pages, comment))
		self.record_window.list_ctrl.SetObjects(self.record_list)
		self.SaveRecordReport()

	def DeleteRecord(self, index):
		self.record_list.pop(index)
		self.record_window.list_ctrl.SetObjects(self.record_list)
		self.SaveRecordReport()

	def CreateRecordReport(self):
		self.record_create.CreateTable()

	def ClearAllRecords(self):
		if os.path.isfile('record_report_save_file.txt'):
			#os.remove('record_report_save_file.txt')
			send2trash('record_report_save_file.txt')
		del self.record_list[:]
		self.record_window.list_ctrl.SetObjects(self.record_list)

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

		save_file = open('record_report_save_file.txt', 'wb')

		writer = csv.writer(save_file)
		writer.writerow(source)
		writer.writerow(type_source)
		writer.writerow(date)
		writer.writerow(pages)
		writer.writerow(comment)

	def LoadRecordReport(self):
		try:
			save_file = open('record_report_save_file.txt', 'r')
			reader = csv.reader(save_file)

			source = reader.next()
			type_source = reader.next()
			date = reader.next()
			pages = reader.next()
			comment = reader.next()

			for index in range(len(source)):
				self.record_list.append(Record(source[index], type_source[index], date[index],
					pages[index], comment[index]))

			self.record_window.list_ctrl.SetObjects(self.record_list)
		except (StopIteration, IOError) as e:
			pass

