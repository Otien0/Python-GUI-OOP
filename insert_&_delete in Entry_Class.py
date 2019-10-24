from tkinter import *
def mentry():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
a = Tk()
Label(a,text='First name').grid(row=0)
Label(a,text ="Last name").grid(row=1)
Label(a,text ="E-mail").grid(row=2)
Label(a,text ="Country").grid(row=3)

e1= Entry(a)
e1.grid(row=0,column=1)
e1.insert(0,"mourice")
e2= Entry(a)
e2.grid(row=1,column=1)
e2.insert(0,"Otieno")
e3= Entry(a)
e3.grid(row=2,column=1)
v1 = "morrisotieno@gmail.com"
e3.insert(0,v1)
e4= Entry(a)
e4.grid(row=3,column=1)
v2 = "Kenya"
e4.insert(0,v2)

Button(a,text="new entries",command=mentry).grid(row=4,column=1)




a.mainloop()
