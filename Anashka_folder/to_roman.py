class IntToRoman:
	def __init__(self,num):
		self.num=num
	def roman_Convert(self):
		
		to_roman_dict = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                2000: 'MM', 3000: 'MMM'}
		
		li = to_roman_dict.values()
		lis = to_roman_dict.keys()
		#print(lis)
		#print(li)
		
		for key in lis:
			if key== self.num:
				print("The Roman numeral is : ",to_roman_dict[key])
			


num = int(input("Enter nuumber :"))
ob=IntToRoman(num)
ob.roman_Convert()
				





	