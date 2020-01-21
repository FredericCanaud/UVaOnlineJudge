import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    tab = list(map(int,line.strip().split()))
    print(abs(tab[1] - tab[0]))
    
