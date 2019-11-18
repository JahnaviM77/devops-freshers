print("enter a number")
num=int(input())
temp=num
pnum=0
r=0
while temp>0:
    r=temp%10
    pnum=pnum*10+r
    temp=temp//10


if(num==pnum):
    print("the given number "+ str(num) +" is a pallindrome")
else:
    print("the given number "+ str(num) +" is not a pallindrome")   