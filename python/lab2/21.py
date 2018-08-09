x=input()
y=input()
a=x
b=y
while y>0:
	if x%y==0:
		break
	else:
		temp=x%y
		x=y
		y=temp
print (a*b)/y
