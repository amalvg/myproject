from tkinter import *
root=Tk()
f=Frame(root).grid()
Label(f,text='username').grid(row=0,column=0)
Label(f,text='password').grid(row=1,column=0)
Entry(f).grid(row=0,column=1)
Entry(f).grid(row=1,column=1)
Button(f,text='login').grid()
root.mainloop()