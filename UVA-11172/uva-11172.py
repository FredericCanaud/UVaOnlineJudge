import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    tab = list(map(int,line.strip().split()))
    if len(tab) == 2:
        if tab[0] < tab[1]:
            print("<")
        else:
            if tab[0] > tab[1]:
                print(">")
            else:
                print("=")
    
