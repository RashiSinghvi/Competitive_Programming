def minimum_defference(k,arr):
	n=len(arr)
	arr.sort()
	min_def=10000
	i=0
	while (i+k-1)<n:
		min_def=min(min_def,arr[i+k-1]-arr[i])
		i+=1
	return min_def

if __name__ == '__main__':
	k=int(input('Enter size of k:- '))
	n=int(input('Enter size of array:- '))
	arr=list()
	for i in range(0,n):
		arr.append(int(input('Enter arr['+str(i)+']')))
	print(minimum_defference(k,arr))
		