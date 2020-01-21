import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    avg = 0
    somme = 0
    tab = list(map(int,line.strip().split()))

    if tab[0] == len(tab)-1:
        for i in range(1,len(tab)):
            avg = avg + tab[i]
        avg = float(avg/tab[0])

    for i in range(1,len(tab)):
        if tab[i] >= avg:
            somme = somme + 1                
    print("{:.3%}".format(somme/tab[0]))