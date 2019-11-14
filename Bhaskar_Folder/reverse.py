def reverse_type1(str):
    s=""
    l=len(str)-1
    while l>=0:
        s=s+str[l]
        l=l-1
    print("without using slicing "+s)


def reverse_type2(str):
    print("with using slicing "+str[::-1])
    
    
str=input()
reverse_type1(str)
reverse_type2(str)