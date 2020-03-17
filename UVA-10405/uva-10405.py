import sys

def LongestCommonSubsequence(sequence1, sequence2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif sequence1[i-1] == sequence2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    plusLongueSousSequence = [""] * (index+1)
    plusLongueSousSequence[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if sequence1[i-1] == sequence2[j-1]:
            plusLongueSousSequence[index-1] = sequence1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    return len(plusLongueSousSequence)-2

lines = sys.stdin.readlines()
while lines[-1] == '\n':
    del lines[-1]

for i in range(0,len(lines),2):
    line1 = lines[i]
    line2 = lines[i+1]
    print(LongestCommonSubsequence(line1,line2, len(line1), len(line2)))