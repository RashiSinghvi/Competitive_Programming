n1=int(input("Enter a 1st no. of range "))
n2=int(input("Enter a 2nd no. of range "))
for num in range(n1,n2+1):
	Sum=0
	n=num
	while(num>0):
		rem=num%10
		Sum+=rem*rem*rem
		num=num//10
	if n==Sum:
		print(n,"is armstrong number")
	