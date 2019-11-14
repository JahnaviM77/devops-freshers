class Ltts:
    def __init__(jahnavi, list):
        jahnavi.list = list        
    def func(jahnavi):
            if len(jahnavi.list) > 1:
                print("Big list")
            else:
                print("Small list")
            print(jahnavi.list)        
class Ltts1(Ltts):
    def __init__(jahnavi, list):
        super().__init__(list)
    def func1(jahnavi):
        print(jahnavi.list)                 
x = Ltts1([1, 1, 'one'])
x.func()
x.func1()
