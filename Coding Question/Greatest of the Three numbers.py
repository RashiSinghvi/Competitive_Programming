n1=int(input("Enter a 1st number : "))
n2=int(input("Enter a 2nd number : "))
n3=int(input("Enter a 3rd number : "))
if n1>n2 and n1>n3:
	print(n1,"is a greatest no.")
elif n2>n3:
	print(n2,"is greatest no.")
else:
	print(n3,"is greatest no.")