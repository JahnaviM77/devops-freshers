class Employee:
	#salary = 0
	def __init__(self,name,department,designation,salary):
		self.name = name
		self.department = department
		self.designation = designation
		self.salary = salary

	def display(self):
		print("Employee Name : " + self.name)
		print("Employee Department : " + self.department)
		print("Employee designation : " + self.designation)
		print("Employee salary :"+ str(self.salary))
		
	
	def pf(abc):
		pf = abc.salary * 5/100
		print("Employee salary : "+ str(pf))
		


emp = Employee('Akash','APx','System Engineer',70000)
emp.display()
emp.pf()
		
		
		
