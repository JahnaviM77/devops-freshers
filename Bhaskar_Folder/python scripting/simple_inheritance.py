class Person(object): #Parent Class
    def __init__(self, name): 
        self.name = name 
   
    def getName(self): 
        return self.name 
 
    def isEmployee(self): 
        return False
   
class Employee(Person):#Child Class 

    def isEmployee(self): 
        return True

emp1= Person("Bhaskar")
print (emp1. getName (), emp1. isEmployee ()) 
   
emp2 = Employee("Ganesh")
print (emp2.getName(), emp2.isEmployee())
