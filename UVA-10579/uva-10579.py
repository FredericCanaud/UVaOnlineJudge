import sys
def fibo3(n):
    n1 = 0
    n2 = 1
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    for i in range (2, n+1):
        n3 = n2 + n1
        n1 = n2
        n2 = n3
    return n3
lines = sys.stdin.readlines()
for l in lines:
    print(fibo3(int(l)))