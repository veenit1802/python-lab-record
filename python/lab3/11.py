def ffun(n):
    while n>0:
        for i in range(0,2):
            print '+ ',
            for j in range(0,4):
                print ' -',
            for k in range(0,2):
                for j in range(0,4):
                    print '|',
                    print('         |'),
n=input()
ffun(n)
