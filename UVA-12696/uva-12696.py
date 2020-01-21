import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

somme = 0
for line in lines:
    tab = list(map(float,line.strip().split()))
    if len(tab) == 4:
        if (tab[0] + tab[1] + tab[2] <= 125.00) or (tab[0] <= 56.00 and tab[1] <= 45.00 and tab[2] <= 25.00):
            if tab[3] <= 7.00:
                print("1")
                somme = somme + 1
            else:
                print("0")
        else:
            print("0")                  
    
print(somme)