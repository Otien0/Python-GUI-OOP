from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

a = Tk()

def mcolor():
    color = colorchooser.askcolor()
    label = Label(text='your chosen color',bg=color[1]).pack()
def mfileopen():
    file1 = filedialog.askopenfile()
    file2 = file1.name
    f = open(file2)
    label2 = Label(text=f.read(),font=('aerial',24,'italic')).pack()
    
button = Button(text="choose color",width = 30,command= mcolor).pack()
button = Button(text="open file",width = 30,command= mfileopen).pack()
a.mainloop()
  
