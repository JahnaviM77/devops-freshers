a=input("Enter number1 : ")
b=input("Enter number2 : ")
c=input("Enter number3 : ")

if (a>b) and (a>c):
    print("{} is bigger".format(a))
elif (b>a) and (b>c):
    print("{} is bigger".format(b))
else:
    print("{} is bigger".format(c)) 
    