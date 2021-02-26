# class student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def getdata(self):
#         self.name=input('enter your name')
#         self.mark=input('enter your mark')
#     def putdata(self):
#         print(self.name,'\n',self.mark)
# obj=student('','')
# obj.getdata()
# obj.putdata()

class Employee:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount+=1
    def dispcount(self):
        print('total employee %d',Employee.empcount)
    def dispEmployee(self):
        print('Name:',self.name,',Salary:',self.salary)
emp1=Employee("ABC",2000)
emp2=Employee('XYZ',5000)
emp1.dispEmployee()
emp2.dispEmployee()
print('Total employee:',Employee.empcount)