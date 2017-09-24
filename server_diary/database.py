import sqlite3

class DB:
	def __init__(self):
		self.connect = sqlite3.connect("test.db")
		self.cursor = self.connect.cursor()

	def searchTable(self, tableName):
		flag = False
		self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
		for item in self.cursor.fetchall():
			if item[0] == tableName:
				flag = True
				break
		return flag

	def initTable(self, tableName):
		if self.searchTable(tableName) == False:
			sql = "CREATE TABLE " + tableName + " (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)"
			self.cursor.execute(sql)
			print u"create table successfully"
		else:
			print u"This table is already exist"

	def insertData(self, tableName, data):
		sql = "INSERT INTO " + tableName + "(title, content) VALUES (?, ?)"
		self.cursor.execute(sql, data)
		self.connect.commit()
		return "saved !"

	def deleteData(self, tableName, id):
		sql = "DELETE FROM " + tableName + "WHERE id = " + str(id)
		self.cursor.execute(sql)
		self.connect.commit()
		return "deleted !"

	def updataData(self, tableName, id, data):
		sql = "UPDATE " + tableName + " SET title = '" + data[0] + "', content = '" + data[1] + "' WHRER id = " + str(id)
		self.cursor.execute(sql)
		self.connect.commit()
		return "updated !"

	def searchData(self, tableName, id):
		sql = "SELECT * FROM " + tableName + " WHERE id = " + str(id)
		self.cursor.execute(sql)
		tup = self.cursor.fetchone()
		dict = {'title': tup[1], 'content': tup[2]}
		return str(dict)

	def showAllData(self, tableName):
		sql = "SELECT * FROM " + tableName
		for row in self.cursor.execute(sql):
			print row

	def getDataDict(self, tableName):
		dict = {}
		i = 0
		sql = "SELECT * FROM " + tableName
		for row in self.cursor.execute(sql):
			item = {'id': row[0],'title': row[1]}
			dict[str(i)] = item
			i += 1
		return str(dict)

	def dropTable(self, tableName):
		sql = 'DROP TABLE IF EXISTS ' + tableName
		self.cursor.execute(sql)
		self.connect.commit()
		return "this table is deleted or not exist"

	def clearTable(self, tableName):
		sql = "DELETE FROM " + tableName
		reset = "UPDATE sqlite_sequence SET seq = 0 WHERE name = '" + tableName + "'"
		self.cursor.execute(sql)
		self.cursor.execute(reset)
		self.connect.commit()
		return "table is clean"

	def close(self):
		self.cursor.close()
		self.connect.close()
			