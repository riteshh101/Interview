def max_score(d1,d2):
	d3={}
	maximum = max(d2,key=d2.get)
	d3[maximum]=d2[maximum]
	return d3
		

n=int(input("Enter number of user want to create..:"))
d1={}
d2={}
for x in range(1,n+1):
	name = input("Enter username:-")
	score = int(input("Enter user Score:-"))
	d1[str(x)]=name
	d2[str(x)]=score

print(max_score(d1,d2))
