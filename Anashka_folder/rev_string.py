def reverse(str1):
	rev = ''
	length = len(str) 
	print(length)
	for i in range(length-1,-1,-1):
		rev = rev +str[i]
	print(rev)

str = "abcd"
reverse(str)
