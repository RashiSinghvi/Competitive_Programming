def moreThanNdK(arr,size,k):
	map={4=3,5=1,6=1,7=1,8=1}
	count=size//k
	for e in arr:
		if e in map:
			map[e]+=1
		else:
			map[e]=1

	for key in map:
		if map[key]>count:
			print(key)

if __name__ == '__main__':
	print("First Test\n")
	arr1= [4, 5, 6, 7, 8, 4, 4]
	size = len(arr1)
	k = 3;
	moreThanNdK(arr1, size, k)