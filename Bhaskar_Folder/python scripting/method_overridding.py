class Employee:  #Parent Class
    def get_ps(self):  
        return 0;  
class Bhaskar(Employee):  #Child Class
    def get_ps(self):  
        return 4000;  
e1 = Employee()  
e2 = Bhaskar()  
 print("Employee Ps_Number",e1.get_ps());  
print("Bhaskar Ps_Number",e2.get_ps());  
