from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

a = Tk()

def mcolor():
    color = colorchooser.askcolor()
    label = Label(text='your chosen color',bg=color[1]).pack()
def mfileopen():
    file1 = filedialog.askopenfile()
    label = Label(text=file1).pack()
    
button = Button(text="choose color",width = 30,command= mcolor).pack()
button = Button(text="open file",width = 30,command= mfileopen).pack()


a.mainloop()
  
