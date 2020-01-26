import sys
import time

requetes = {}

def getFactors(n):
    factors=[]

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

while True:
    line = sys.stdin.readline().strip()
    if line == '#':
        break
    try:
        ordre, numero, quantum = line.split()
        ordre.lower()
        if ordre == "Register":
            if quantum not in requetes:
                requetes[int(quantum)] = int(numero)
    except:
        break
nombreRequetes = int(sys.stdin.readline().strip())
quantumMax = int(max(requetes.keys()))
while nombreRequetes > 1:
    for i in range(1,quantumMax+1):
        print(getFactors(i))
        if nombreRequetes > 0:
            for j in requetes.keys():
                if j in getFactors(i):
                    nombreRequetes = nombreRequetes - 1
                    print(requetes.get(j))
        else:
            break