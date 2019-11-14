class Employee:  #Parent Class
    def get_ps(self):  
        return 0;  
class Bhaskar(Employee):  #Child Class
    def get_ps(self):  
        return 4000;  
class Ganesh(Employee):  #Child Class
    def get_ps(self):  
        return 4000;  
e1 = Employee()  
e2 = Bhaskar()  
e3 = Ganesh()  

print("Employee Ps_Number",e1.get_ps());  
print("Bhaskar Ps_Number",e2.get_ps());  
print("Ganesh Ps_Number",e3.get_ps());  
