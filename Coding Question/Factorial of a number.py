def factorial(n):
	Sum=1
	for i in range(1,n+1):
		Sum=Sum*i
	print(Sum)

n=int(input("Enter a number : "))
factorial(n)