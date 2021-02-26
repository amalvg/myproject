from tkinter import *
root=Tk()
class demo:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        Button(frame,text='hai amal',command=self.printmsg).pack()
        Button(frame,text='exit',command=frame.quit).pack()
    def printmsg(self):
        print('hello am amal')
obj=demo(root)
root.mainloop()
