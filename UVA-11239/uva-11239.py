import sys
import heapq

utilisateurs = {}
systemes = {}
heap = []

while True:
    line = sys.stdin.readline().strip()
    if len(line) != 0:
        if line[0] == "0":
            break
        elif line[0] == "1":
            for key in systemes.keys():
                for user in utilisateurs.keys():
                    if user in systemes[key] and utilisateurs[user] > 1:
                        systemes[key].remove(user)
                heapq.heappush(heap, (-len(systemes[key]),key))
            heap.sort()
            for i in range(0,len(heap)):
                print(heap[i][1],-heap[i][0])
            heap.clear()
            systemes.clear()
            utilisateurs.clear()
        else:  
            if line.isupper():
                systemeActuel = line
                systemes[systemeActuel] = set()
            elif line.islower():
                if line in utilisateurs.keys() and line not in systemes[systemeActuel]:
                    utilisateurs[line] = utilisateurs[line] + 1
                else:
                    utilisateurs[line] = 1
                systemes[systemeActuel].add(line)