x=input('amount')
c=x/100
if c>0:
	print 'the number of hundred notes=',c
	x=x%100
c=x/50
if c>0:
	print 'the number of fifty notes=',c
	x=x%50
c=x/10
if c>0:
	print 'the number of ten notes=',c
