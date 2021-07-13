n=int(input("Enter a no. "))
count=0
for i in range(2,n):
	if n%i==0:
		count+=1
if count>1: 
	print(n,"is not a prime no.")
else:
	print(n, "is a prime no.")