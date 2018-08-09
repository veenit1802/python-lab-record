x=input()
y=input()
while y>0:
	if x%y==0:
		print y
		break
	else:
		temp=x%y
		x=y
		y=temp
