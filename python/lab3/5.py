def fact(k):
    if k==1 or k==0:
        return 1
    else:
        s=k*fact(k-1)
    return s
x=input()
z=fact(x)
print z
