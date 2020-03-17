import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

def winwin(X):
    nombres = set()
    max = 0
    m = len(X)
    for i in range(m):
        max += X[i]
        if mx <0:
            mx=0
        if mx > max:
            max = mx
    return max

pari = -1
bet = []
for line in lines:
    line = list(map(int,line.strip().split()))
    if pari == -1:
        if line != []:
            pari=line[0]
    else:
        for i in range(len(line)):
            bet.append(line[i])
        if len(bet) == pari:
            gan = winwin(bet)
            pari = -1
            bet = []
            if gan <= 0:
                print("Losing streak.")
            else:
                print("The maximum winning streak is "+str(gan)+".")