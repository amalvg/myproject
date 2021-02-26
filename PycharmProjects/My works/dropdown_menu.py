from tkinter import *
root=Tk()

def fun():
    print('this is function')

mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)

mymenu.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Save',command=fun)
submenu.add_separator()
submenu.add_command(label='Exit',command=root.quit)

submenu2=Menu(mymenu)

mymenu.add_cascade(label='Edit',menu=submenu2)
submenu2.add_command(label='Undo',command=fun)
submenu2.add_command(label='Redo',command=fun)

submenu3=Menu(mymenu)
subsub=Menu(submenu3)

mymenu.add_cascade(label='Run',menu=submenu3)
submenu3.add_cascade(label='Test',menu=subsub)
subsub.add_command(label='Bug',command=fun)

root.mainloop()