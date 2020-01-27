import sys


def isCorrect(line):
    tab = list(line)
    pileElementOpenned =[]
    for car in tab:
        if car=="(":
            pileElementOpenned.append("(")
        elif car=="[":
            pileElementOpenned.append("[")
        elif car==")":
            if len(pileElementOpenned)==0 or pileElementOpenned.pop() != "(":
                return False
        elif car=="]":
            if len(pileElementOpenned)==0 or pileElementOpenned.pop() != "[":
                return False
    
    return len(pileElementOpenned) == 0



lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

numberOfLines = list(map(int,lines[0].split()))[0]

for i in range(1,numberOfLines+1):
    line = lines[i]
    if isCorrect(line):
        print("Yes")
    else:
        print("No")