def pattern(t,n):
    if n == 1:
        for i in range(t):
            for j in range(i):
                print('_',end='')
            print()
    if n == 2:
        for y in range(t):
            for j in range(y,t):
                print("_",end='')
            print()
    if n == 3:
        for f in range(t):
            for j in range(f,t):
                print(' ',end='')
            for j in range(f):
                print('_',end='')
            print()
    if n == 4:
        for g in range(t):
            for j in range(g):
                print(' ',end = '')
            for j in range(g,t):
                print('_',end='')
            print()
    if n == 5:
        for x in range(t):
            for j in range(x,t):
                print(' ',end='')
            for j in range(x):
                print('_',end='')
            for j in range(x):
                print('_',end='')
            print()
    if n == 6:
        for u in range(t):
            for j in range(u):
                print(' ',end='')
            for j in range(u,t):
                print('_',end='')
            for j in range(u,t):
                print('_',end='')
            print()
    if n == 7:
        for a in range(t):
            for j in range(a,t):
                print(' ',end='')
            for j in range(a):
                print('_',end='')
            for j in range(a):
                print('_',end='')
            print()
    for a in range(t):
            for j in range(a):
                print(' ',end='')
            for j in range(a,t):
                print('_',end='')
            for j in range(a,t):
                print('_',end='')
            print()

pattern(10,1)

print(1)