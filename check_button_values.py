from tkinter import *
def mget():
    print(var1.get(),var2.get(),var3.get(),var4.get())

a = Tk()
var1 = IntVar()
Checkbutton(a,text="checkbutton1",variable=var1).grid(row=0,sticky=W)
var2 = IntVar()
Checkbutton(a,text="checkbutton2",variable=var2).grid(row=1,sticky=W)
var3 = IntVar()
Checkbutton(a,text="checkbutton3",variable=var3).grid(row=2,sticky=W)
var4 = IntVar()
Checkbutton(a,text="checkbutton4",variable=var4).grid(row=3,sticky=W)
Button(a,text="get values",command = mget,width=15).grid(row=4,sticky=W)
Button(a,text="quit",command=a.destroy,width=15).grid(row=5,sticky=W)

a.mainloop()
