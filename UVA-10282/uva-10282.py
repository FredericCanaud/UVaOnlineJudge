import sys

dictionnaire = {}

while True:
    line = sys.stdin.readline().strip()
    if line == '\n':
        break
    try:
        traduction, mot = line.split()
        dictionnaire[mot] = traduction
    except:
        break
for line in sys.stdin:
    try:
        mot = line.strip()
    except:
        break
    try:
        print(dictionnaire[mot])
    except:
        print('eh')
