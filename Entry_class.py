from tkinter import *
a = Tk()
Label(a,text='First name').grid(row=0)
Label(a,text ="Last name").grid(row=1)
Label(a,text ="E-mail").grid(row=2)
Label(a,text ="Country").grid(row=3)

e1= Entry(a)
e1.grid(row=0,column=1)
e2= Entry(a)
e2.grid(row=1,column=1)
e3= Entry(a)
e3.grid(row=2,column=1)
e4= Entry(a)
e4.grid(row=3,column=1)




a.mainloop()
