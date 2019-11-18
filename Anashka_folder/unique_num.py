
def unique(list1):
	unique = []
	for i in list1:
		if i not in unique:
			unique.append(i)

	print("Original list is {}".format(list1))
	print("Unique list is {}".format(unique))

list2 = [4,2,3,3,6,6,9,5]	
unique(list2)