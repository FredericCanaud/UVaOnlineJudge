import sys


def estUnAnagramme(premierMot,deuxiemeMot):
    if(sorted(premierMot.lower()) == sorted(deuxiemeMot.lower())):
        return True
    else:
        return False 
    
dictionnaire = set()
pasAnagramme = set()
iterateur = 0

while True:
    line = sys.stdin.readline().strip().split()
    if line[0] == '#':
        break
    else:
        for mot1 in line:
            if iterateur == 0:
                dictionnaire.add(mot1)
            else:
                for mot2 in list(dictionnaire):
                    if not estUnAnagramme(mot1,mot2) and iterateur != 0:
                        dictionnaire.add(mot1)
                    else:
                        pasAnagramme.add(mot1)
                        pasAnagramme.add(mot2)
                        dictionnaire.remove(mot2)
    iterateur = iterateur +1
dictionnaire = sorted(dictionnaire)
for mot in dictionnaire:
    if mot in dictionnaire:
        print(mot)