class Details:
	def __init__(self,name,age,mark,tutor):                # class definition
		self.name = name
		self.age = age
		self.mark = mark
		self.tutor = tutor


ob = Details('Aan',18,90,'Deepa')                                  # Object creation

print(ob.name)
print(ob.age)
print(ob.mark)
print(ob.tutor)