def min_jump(c):
	size=len(c)
	count=-1;
	i=0
	while i<size:
		if i+2<size and c[i+2]==0:
			i+=1
		i+=1
		count+=1
	return count

if __name__ == '__main__':
	n=int(input("Enter number of cloud:- "))
	c=list()
	for i in range(0,n):
		c.append(int(input("Enter c["+str(i)+"]:- ")))
	min_count=min_jump(c)
	print("Answer:- "+str(min_count))