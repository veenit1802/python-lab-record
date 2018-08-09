a=[]
k=0
i=0
while i<10:
	j=input()
	if j%2==1:
		a.append(j)
		k=k+1
	i=i+1
a.sort()
print a[k-1]
