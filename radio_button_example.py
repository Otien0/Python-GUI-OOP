from tkinter import *
root = Tk()

def mmm():
    a = v.get()
    if(a == 1):
        a1 = Tk()
        a1.title('Python')
        l1=Label(a1,text='welcome to Python programming',font=('aerial',20,'italic'))
        l1.pack()
    elif(a == 2):
        a1 = Tk()
        a1.title('Java')
        l1=Label(a1,text='welcome to Java programming',font=('aerial',20,'italic'))
        l1.pack()
    elif(a == 3):
        a1 = Tk()
        a1.title('Objective C')
        l1=Label(a1,text='welcome to Objective C programming',font=('aerial',20,'italic'))
        l1.pack()
    else:
        (a == 4)
        a1 = Tk()
        a1.title('Node.Js')
        l1=Label(a1,text='welcome to Node.Js programming',font=('aerial',20,'italic'))
        l1.pack()

root.title('radio buttons')
v = IntVar()
v.set(1)
Languages = [("Python",1),("Java",2),("Objective C",3),("Node.Js",4)]
Label(root,text="Choose a Programming \nLanguage",padx=25,justify=LEFT).pack(anchor=W)

for txt, val in Languages:
    Radiobutton(root,text=txt,padx=25,variable=v,value=val,command=mmm).pack(anchor=W)




root.mainloop()
