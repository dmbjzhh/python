from Tkinter import *
import socket

def write():
	textVar.set("")
	text.delete("0.0", "end")
	label.config(text = "write diary mode")
	listBox.pack_forget()
	entry.pack()
	text.pack()

def save():
	title = textVar.get() + ".txt"
	content = text.get("0.0", "end")

	if title == '':
		label.config(text = "please enter the title")
	else:
		s = socket.socket()
		s.connect(('127.0.0.1', 1234))
		print s.recv(1024)
		dict = {'title': title, 'content': str(content)}
		s.send(str(dict))
		data = s.recv(1024)
		s.close()
		label.config(text = data)

def read():
	listBox.delete(0,END)
	showText = "read diary mode"

	s = socket.socket()
	s.connect(('127.0.0.1', 1234))
	print s.recv(1024)
	s.send("read")
	data = s.recv(2048)
	dict = eval(data)
	s.close()

	if len(dict) == 0:
		showText += " (empty list)"
	label.config(text = showText)

	for item in dict.values():
		string = str(item['id']) + ': ' + item['title']
		listBox.insert(0, string)

	listBox.bind('<Double-Button-1>', showDiary)

	entry.pack_forget()
	text.pack_forget()
	listBox.pack()

def showDiary(event):
	title = listBox.get(listBox.curselection())
	textVar.set(title)

	id = title.split(':')[0]
	data = 'show' + id

	s = socket.socket()
	s.connect(('127.0.0.1', 1234))
	print s.recv(1024)
	s.send(data)
	data = s.recv(1024)
	content = eval(data)['content']
	s.close()

	text.delete("0.0", "end")
	text.insert("end", content)
	listBox.pack_forget()
	entry.pack()
	text.pack()



root = Tk()
root.geometry('500x400')
root.title("For Sweetie")


saveBtn = Button(root, text = "Save", command = save)
saveBtn.pack(side = LEFT, anchor='sw')

quitBtn = Button(root, text = "quit", command =quit)
quitBtn.pack(side = RIGHT, anchor = 'se')

writeBtn = Button(root, text = "write diary", command = write)
writeBtn.pack(side=BOTTOM, anchor = 's')

readBtn = Button(root, text = "read diary", command = read)
readBtn.pack(side=BOTTOM, anchor = 's')

textVar = StringVar()
entry = Entry(root, textvariable = textVar)
text = Text(root)
listBox = Listbox(root, height = 300)

label = Label(root)
label.pack()

root.mainloop()
