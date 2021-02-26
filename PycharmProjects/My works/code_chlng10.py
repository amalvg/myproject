class Computer:
    def __init__(self,compname):
        self.compname=compname
    def get1(self):
        self.compname=input('enter computer name')
class Desktop(Computer):
    def __init__(self,deskname):
        self.deskname=deskname
    def get2(self):
        self.deskname=input('enter desktop name')
class Laptop(Desktop):
    def __init__(self,lapname):
        self.lapname=lapname
    def get3(self):
        self.lapname=input('enter laptop name')
    def display(self):
        print('computer name is',self.compname)
        print('desktop name is',self.deskname)
        print('laptop name is',self.lapname)
obj=Laptop(' ')
obj.get1()
obj.get2()
obj.get3()
obj.display()