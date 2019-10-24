from tkinter import *

a = Tk()
var1 = IntVar()
Checkbutton(a,text="checkbutton1",variable=var1).grid(row=0,sticky=W)
var2 = IntVar()
Checkbutton(a,text="checkbutton2",variable=var2).grid(row=1,sticky=W)
var3 = IntVar()
Checkbutton(a,text="checkbutton3",variable=var3).grid(row=2,sticky=W)
var4 = IntVar()
Checkbutton(a,text="checkbutton4",variable=var4).grid(row=3,sticky=W)


a.mainloop()
