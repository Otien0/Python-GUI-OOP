from tkinter import *
from tkinter import colorchooser
a = Tk()

def mcolor():
    color = colorchooser.askcolor()
    label = Label(text='your chosen color',bg=color[1]).pack()
button = Button(text="choose color",width = 30,command= mcolor).pack()
a.mainloop()
  
