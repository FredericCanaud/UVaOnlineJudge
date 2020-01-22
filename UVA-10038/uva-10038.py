import sys

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    tab = list(map(int,line.strip().split()))
    jolly = True
    taille = tab[0]
    nombres = set()
    nombresAttendus = set()
    for i in range(1,len(tab)-1):
        if(abs(tab[i]-tab[i+1]) < 1 or abs(tab[i]-tab[i+1]) > taille-1):
            jolly = False
            nombres.add(abs(tab[i]-tab[i+1]))
            nombresAttendus.add(i)
    if jolly:
        if(nombres == nombresAttendus):
            print("Jolly")
        else:
            print("Not Jolly")
    else:
        print("Not jolly")