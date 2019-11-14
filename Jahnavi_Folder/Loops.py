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
x = Ltts(2, 3)
x.func() 
