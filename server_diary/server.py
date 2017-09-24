import socket
import database
import re

s = socket.socket()
s.bind(('127.0.0.1', 1234))

s.listen(5)
while True:
	c, addr = s.accept()
	print u'connecting address is : ', addr
	c.send('connecting to the server successfully...')

	data = c.recv(1024)
	if data:
		tableName = 'diary'
		database.DB().initTable(tableName)
		database.DB().showAllData(tableName)

		if data == 'read':
			print 'read diary: '
			c.send(database.DB().getDataDict(tableName))

		elif data[0:4] == 'show':
			id = re.sub(r'\D', '', data)
			print 'search diary: ', id
			c.send(database.DB().searchData(tableName,id))

		else:
			dict = eval(data)
			print dict
			tup = (dict['title'], dict['content'])
			print tup
			c.send(database.DB().insertData(tableName, tup))

		database.DB().close()

	c.close()