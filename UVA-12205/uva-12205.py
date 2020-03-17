import sys

dureeAppel = {}

increment = 0
while True:
    line = sys.stdin.readline().strip().split()
    if int(line[0]) == 0 and int(line[1]) == 0:
        break
    else:
        for i in range(1,int(line[0])+1):
            line2 = sys.stdin.readline().strip().split()
            dureeAppel[int(line2[2])] = int(int(line2[2]) + int(line2[3]))
            print(int(line2[2]),dureeAppel[int(line2[2])])
        for i in range(1,int(line[1])+1):
            line2 = sys.stdin.readline().strip().split()
            print(line2)
            for debut, fin in dureeAppel.items():
                if (int(line2[0]) >= fin) and (int(line2[0]) + int(line2[1]) <= fin):
                    increment = increment +1
                elif (int(line2[0]) <= debut) and (int(line2[0]) + int(line2[1]) >= debut):
                    increment = increment +1
                elif (int(line2[0]) <= debut) and (int(line2[0]) + int(line2[1]) >= fin):
                    increment = increment +1
                print(increment)
            increment = 0
        dureeAppel.clear()