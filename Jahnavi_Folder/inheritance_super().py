class Ltts:
    def __init__(jahnavi, stream, team):
        jahnavi.stream = stream
        jahnavi.team = team
    def func(jahnavi):
        print(jahnavi.stream, jahnavi.team)
        
class Ltts1(Ltts):
    def __init__(jahnavi, stream, team, psnumber):
        jahnavi.number = psnumber
        
l=Ltts1("APE", "Devops", 40007348)
l.func()
