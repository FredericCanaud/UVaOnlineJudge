import sys


lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for line in lines:
    line = line.split()
    for i in line:
        i = line[i].rstrip(',').rstrip('.')
    print(line)