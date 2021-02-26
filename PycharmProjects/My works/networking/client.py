import socket
from tkinter import *

def send(listbox,entry):
    m_client=entry.get()
    listbox.insert('end','Client:'+m_client)
    entry.delete(0,END)
    s.send(bytes(m_client, 'utf-8'))

def receive(listbox):
    m_server = s.recv(50)
    listbox.insert('end','Server:'+m_server.decode('utf-8'))

root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text='Send',command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)
rbutton=Button(root,text='Receive',command=lambda :receive(listbox))
rbutton.pack(side=BOTTOM)
root.title('Client')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12346
s.connect((HOST_NAME,PORT))

root.mainloop()
