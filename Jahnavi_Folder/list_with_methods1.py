list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list)
print(len(list))

list.append(9)
print(list)

list.remove(3)
print(list)

list.pop()
print(list)

list.insert(3, "three")
print(list)

list1= [11, 12, 13, 14, 15, 16, 17, 18]
list3 = list + list1
print(list3)

list4 = list.copy()
print(list4)
print(list4.count(3))

list.clear()
print(list)
