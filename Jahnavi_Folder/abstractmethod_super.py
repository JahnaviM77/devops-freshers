from abc import ABC, abstractmethod
class Ltts(ABC):
    def method(jahnavi):
       print("SPS")
    
class Ltts1(Ltts):
    def method(jahnavi):
        super().method()
        print("DevOps")
        
class Ltts2(Ltts1):
    def method(jahnavi):
        super().method()
        print("APE")
        

x = Ltts2()
x.method()

