p=input('principal amount')
r=input('rate')
t=input('time')
s=p*r*t
print 'simple interest=',s
c=p*((r+1)**t-1)
print 'compund interest=',c
