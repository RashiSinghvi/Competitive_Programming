num=int(input("Enter a no. "))
Sum=0
while(num>0):
	rem=num%10
	Sum+=rem
	num=num//10
print("Sum of digits is : ",Sum)