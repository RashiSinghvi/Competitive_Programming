def makePalindrome(str):
	for i in range(0,len(str)):
		if isPalindrome(str+str[0:i][::-1]):
			print("Min-New palindrome String:- "+str+str[0:i][::-1])
			return
		elif isPalindrome(str[::-1][0:i]+str):
			print("Min-New palindrome String:- "+str[::-1][0:i]+str)
			return

def isPalindrome(str):
	return str==str[::-1]


if __name__ == '__main__':
	str=input('Enter any string:- ')
	if isPalindrome(str):
		print("Given String "+str+" is palindrome")
	else:
		makePalindrome(str)