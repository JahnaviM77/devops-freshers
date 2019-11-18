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
        
print(issubclass(Ltts2, Ltts))
print(issubclass(Ltts2, Ltts1))
print(issubclass(Ltts1, Ltts))
print(issubclass(Ltts, Ltts2))
print(isinstance(Ltts2(), Ltts))
print(isinstance(Ltts2(), Ltts1))
print(isinstance(Ltts1(), Ltts))
print(isinstance(Ltts(), Ltts1))