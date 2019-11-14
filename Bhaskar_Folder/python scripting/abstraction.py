class Object_Count:  
    __count = 0;  
    def __init__(self):  
        Object_Count.__count = Object_Count.__count+1  
    def display(self):  
        print("The number of objects created for this class:",Object_Count.__count)  
ob1 = Object_Count()  
ob2 = Object_Count()  
ob1.display()  
