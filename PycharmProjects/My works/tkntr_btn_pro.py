from tkinter import *
root=Tk()
f=Frame(root).pack()
def log():
    print('hai amal')
def cancel():
    print('its cancelled')
Button(f,text='login',bg='red',command=log).pack()
Button(f,text='cancel',bg='cyan',command=cancel).pack()
root.mainloop()
