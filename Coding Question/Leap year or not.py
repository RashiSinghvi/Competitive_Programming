year= int(input("Enter a year "))
if year%4==0:
	print("It is a leap Year")
elif year%100==0:
	print("It is not a leap Year")
elif year%400==0:
	print("It is a leap Year")
else:
	print("It is not a leap Year")