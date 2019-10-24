from tkinter import *

def mcal():
    var2 = var1.get()
    var3 = var2 * 3.785
    e2.insert(0,var3)
def mclear():
    e1.delete(0,END)
    e2.delete(0,END)

a = Tk()
a.title("Unit Converter")
var1 = IntVar()
n = "arial",14,"bold"

Label(a,text="Gallons",padx=25,font=(n)).grid(row=0,sticky=W)
e1 = Entry(a,width=25,textvariable=var1)
e1.grid(row=0,column=1)
Label(a,text="Litres",padx=25,font=(n)).grid(row=1,sticky=W)
e2 = Entry(a,width=25)
e2.grid(row=1,column=1)

Button(a,text="calculate",command=mcal,font=(n),width=25).grid(row=2,column=1)
Button(a,text="Clear",command=mclear,font=(n),width=25).grid(row=2,column=0)
Button(a,text="EXIT",font=(n),command=a.destroy,width=25).grid(row=3,column=0)


a.mainloop()
