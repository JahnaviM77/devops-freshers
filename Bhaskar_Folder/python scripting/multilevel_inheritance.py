class Base(object): #Parent Class
    def __init__(self, name): 
        self.name = name 
    def getName(self): 
        return self.name 

class Child(Base): #Child Class for Base and Parent Class for GrandChild
    def __init__(self, name, age): 
        Base.__init__(self, name) 
        self.age = age 
    def getAge(self): 
        return self.age 

class GrandChild(Child): #Child Class
    def __init__(self, name, age, address): 
        Child.__init__(self, name, age) 
        self.address = address 
    

def getAddress(self): 
        return self.address         

g = GrandChild("Bhaskar", 23, "Ap")   
print(g.getName(), g.getAge(), g.getAddress())
