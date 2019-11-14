class Parent1(object): #Parent Class
    def __init__(self): 
        self.str1 = "Bhaskar"
        print("Parent1 class")
class Parent2(object): #Parent Class
    def __init__(self): 
        self.str2 = "Ganesh"        
        print("Parent2 class")  
class Derived(Parent1,Parent2): #Child Class
    def __init__(self): 
        Parent1.__init__(self) 
        Parent2.__init__(self) 
        print("Derived class")
          
    def printStrs(self): 
        print(self.str1, self.str2)
ob = Derived() 
ob.printStrs()
