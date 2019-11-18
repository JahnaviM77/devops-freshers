class Ltts:
    def __init__(jahnavi, a, b, c):
        jahnavi.a = a
        jahnavi.b = b
        jahnavi.c = c

list = []
list.append(Ltts("Sunil", "IS", "Bangalore"))
list.append(Ltts("Swapna", "Mentor", "Bangalore"))
list.append(Ltts("Jahnavi", "Trainee", "Mysore"))
for x in list:
    print(x.a, x.b, x.c)
print(list[0].a)
print(list[1].a)
print(list[2].a)
