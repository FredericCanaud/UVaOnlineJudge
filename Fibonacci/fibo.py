def fibonacci1(number):
    if (number <= 0):
        return 0
    elif (number == 1):
        return 1
    else:
        return fibonacci1(number-1) + fibonacci1(number-2)

def fibonacci2(number):
    tab = [None]*(number+1)
    tab[0] = 0
    tab[1] = 1
    for i in range (2, number+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[number]

def fibonacci3(number):
    nombre1 = 0
    nombre2 = 1
    for i in range (2, number+1):
        nombre3 = nombre2 + nombre1
        nombre1 = nombre2
        nombre2 = nombre3
    return nombre3

while True:
    nombre = input("Entrez un nombre à calculer : ")
    print(fibonacci3(int(nombre)))
