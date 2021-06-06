def getmax(li,a):
	count = 0
	result = 0
	for i in range(0,a):
		if li[i]==0:
			count = 0
		else:
			count+=1
			result = max(result,count)
	return result

li=[0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
a=len(li)
print(getmax(li,a))