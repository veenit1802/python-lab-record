def compound(p,n,t):
    s=p*((1+n)**t-1)
    return s
p=input()
n=input()
t=input()
k=compound(p,n,t)
print k
