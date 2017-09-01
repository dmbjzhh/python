from Tkinter import *
import os

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

	if title != ".txt":
		fileObj = open(title,"wb")
		fileObj.write(content);
		fileObj.close()
		label.config(text = "saved")
	else:
		label.config(text = "Please enter the title")

def read():
	listBox.delete(0,END)
	dir = os.getcwd()
	list = os.listdir(dir)

	showText = "read diary mode"
	if len(list) == 0:
		showText += " (empty list)"
	label.config(text = showText)

	for item in list:
		listBox.insert(0, item)

	listBox.bind('<Double-Button-1>', showDiary)

	entry.pack_forget()
	text.pack_forget()
	listBox.pack()

def showDiary():
	title = listBox.get(listBox.curselection())
	showTitle = title[:-4]
	textVar.set(showTitle)

	fileObj = open(title, "r+")
	content = fileObj.read();
	text.delete("0.0", "end")
	text.insert("end", content)
	fileObj.close()

	listBox.pack_forget()
	entry.pack()
	text.pack()

def initDiary():
	dir = os.getcwd()
	list = os.listdir(dir)
	haveDiary = False
	for item in list:
		if item == "diary":
			haveDiary = True
	if haveDiary == False:
		os.mkdir("diary")

	os.chdir("./diary")

initDiary()


root = Tk()
root.geometry('500x400')
root.title("For Sweetie")


saveBtn = Button(root, text = "Save", command = save)
saveBtn.pack(side = LEFT, anchor='sw')

quitBtn = Button(root, text = "quit")
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

