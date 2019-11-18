def prime_Num(num):
	flag=0
	for i in range(2,int(num/2),1):
		if num % i == 0:
			flag = 1

	if flag==1:
		print("{} is Not Prime".format(num))
	else:
		print("{} is Prime".format(num))


num = int(input("Enter the number:"))
prime_Num(num)