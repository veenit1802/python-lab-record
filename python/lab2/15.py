x=int(input('enter the number'))
i=0
s=0
while x>0:
	c=x%10
	s=s+((c+1)%10)*10**i
	i=i+1
	x=x/10
print s
	
