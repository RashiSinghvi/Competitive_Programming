def substrCount(s): 'aabxb'
	ans=len(s)
	for i in range(0,len(s)):
		#logic-1["aaaa"]
		rpc=0
		while i+1<len(s) and s[i]==s[i+1]:
			rpc+=1
			i+=1
		ans=ans+(rpc*(rpc+1))//2

		#logic-2['abxba']
		p=1
		while i-p>=0 and i+p<len(s) and s[i+p]==s[i-1] and s[i-p]==s[i-1]:
			ans+=1
			p+=1
	return ans

if __name__ == '__main__':
	s=input('Enter any string:- ')
	print(substrCount(s)