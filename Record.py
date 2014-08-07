from datetime import datetime as dt

class Record:
	def __init__(self, source, type_source, date, pages, comment):
		self.source = source
		self.type_source = type_source
		self.date = date
		self.pages = pages
		self.comment = comment

	def __str__(self):
		if self.comment == None:
			return self.source + ' ' + self.type_source + ' ' + self.date + ' ' + self.pages
		return self.source + ' ' + self.type_source + ' ' + self.date + ' ' + self.pages + ' ' + self.comment

	def __repr__(self):
		if self.comment == None:
			return self.source + ' ' + self.type_source + ' ' + self.date + ' ' + self.pages
		return self.source + ' ' + self.type_source + ' ' + self.date + ' ' + self.pages + ' ' + self.comment


	@staticmethod
	def Compare(record1, record2):
		date1 = dt.strptime(record1.date, '%m/%d/%y')
		date2 = dt.strptime(record2.date, '%m/%d/%y')
		return int((date1 - date2).total_seconds())
