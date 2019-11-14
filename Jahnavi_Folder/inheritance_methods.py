class Ltts:
    def fun(self):
        print("Devops")
class Ltts1(Ltts):
    def fun1(self):
        print("Smart Products")
class Ltts2(Ltts1):
    def fun2(self):
        print("APE")
l = Ltts2()
l.fun()
l.fun1()
l.fun2()
