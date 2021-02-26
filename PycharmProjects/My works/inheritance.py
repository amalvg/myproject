# class student:
#     def __init__(self,name):
#         self.name=name
#     def getdata(self):
#         self.name=input('enter your name')
# class hod(student):
#     def __init__(self,hodname):
#         self.hodname=hodname
#     def getdata2(self):
#         self.hodname=input('enter hod name')
#     def display(self):
#         print('student name is',self.name)
#         print('hod name is',self.hodname)
# # obj=hod('')
# # obj.getdata()
# # obj.getdata2()
# # obj.display()
#
# class C(hod):
#     def fun3(self):
#         print('this is class C')
# class D(C):
#     def fun4(self):
#         print('this is class D')
# obj=D('')
# obj.getdata()
# obj.getdata2()
# obj.display()
# obj.fun3()
# obj.fun4()

class A:
    def get1(self):
        print('an A class')
class B:
    def get2(self):
        print('a B class')
class C(A,B):
    def put(self):
        print('yes am an inherited A & B')
obj=C()
obj.get1()
obj.get2()
obj.put()