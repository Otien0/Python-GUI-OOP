from tkinter import *
myGui = Tk()
def hello():
    b = a.get()
    myLabel3 = Label(text=b,fg='red',bg='green',font=14).pack()

def dele():
    myLabel4 = Label(text='Deleted',fg='red',bg='green',font=14).pack()
def newfi():
    myLabel5 = Label(text='Clicked on a new file',font=('roman',16,'italic')).pack()

a = StringVar()

myGui.title("Hello")
myGui.geometry("500x500+200+100")

myLabel1 = Label(text='label one',fg='grey',bg='purple',font=('arial',24,'bold')).pack()
myButton1 = Button(text='Enter',fg='black',bg='yellow',font=('times',22,'italic'),command = hello).pack()
myButton2 = Button(text='Delete',fg='black',bg='blue',font=26,command = dele).pack()
text = Entry(textvariable = a).pack()

mymenu = Menu()
listone = Menu()
listone.add_command(label="New File",command = newfi)
listone.add_command(label="Open File")
listone.add_checkbutton(label="run mode")
listone.add_command(label="Save File")
listone.add_command(label="Edit File")
listone.add_command(label="Delete File")

listtwo = Menu()
listtwo.add_command(label="cut")
listtwo.add_command(label="copy")
listtwo.add_command(label="paste")
listtwo.add_command(label="Select All")

listthree = Menu()
listthree.add_command(label="Indent Region")
listthree.add_command(label="Dendent Region")
listthree.add_command(label="Tabify Region")
listthree.add_command(label="Untabify Region")

listfour = Menu()
listfour.add_command(label="Python Shell")
listfour.add_command(label="Run Module F5")

listfive = Menu()
listfive.add_command(label="Configure IDLE")
listfive.add_command(label="Code Context")


mymenu.add_cascade(label="File",menu=listone)
mymenu.add_cascade(label="Edit",menu=listtwo)
mymenu.add_cascade(label="Format",menu=listthree)
mymenu.add_cascade(label="Run",menu=listfour)
mymenu.add_cascade(label="Options",menu=listfive)

myGui.config(menu=mymenu)

myGui.mainloop()
