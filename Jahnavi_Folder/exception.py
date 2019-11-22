class Ltts:
    def __init__(jahnavi, a, b):
        jahnavi.a = a
        jahnavi.b = b
    
    def exception(jahnavi):
        try:
            result = jahnavi.a / jahnavi.b
        except ZeroDivisionError:
            print("divide by zero")
        else:
            print(result)
        finally:
            print("Executed")
            
x = Ltts(2, 0)
x.exception()