class Ltts:
    def __init__(jahnavi, a, b):
        jahnavi.a = a
        jahnavi.b = b
    def func(jahnavi):
        if jahnavi.a > jahnavi.b:
            print("a is greater")
        else:
            jahnavi.a < jahnavi.b
            print("b is greater")
            
class Ltts1(Ltts):
    def __init__(jahnavi, a, b, c):
        jahnavi.c = c       
    def func1(jahnavi):
        y = jahnavi.a+jahnavi.b+jahnavi.c
        print(y)
x = Ltts1(2, 3, 5)
x.func1()
