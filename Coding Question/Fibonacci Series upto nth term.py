n=int(input("Enter a nth no."))
a=0
b=1
print(a,b,end=" ")
for i in range(2,10):
	Sum=a+b
	print(Sum,end=" ")
	a=b
	b=Sum
