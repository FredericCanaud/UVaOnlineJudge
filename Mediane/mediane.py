import sys

nombres = []

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

del lines[0]
for line in lines:
    line = line.split()
    if len(line) < 2:
        print("Vide")
        break
    for i in range(1,int(line[0])+1):
        nombres.append(float(line[i]))
    nombres.sort()
    if len(nombres) % 2 == 1:
        print(nombres[int((len(nombres)-1)/2)])
    else:
        print( round((nombres[int((len(nombres)/2))] + nombres[int((len(nombres)/2-1))])/2, 2) )
    nombres.clear()