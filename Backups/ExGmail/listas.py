from random import *

if __name__ == '__main__':
    x = 50
    lista = [randrange(x), randrange(x), randrange(x), randrange(x), randrange(x)]
    x = 0
    y = 0
    soma = 0
    numMaior = lista[x]
    numMenor = lista[x]

    while x < len(lista):
        print(lista[x])
        soma = soma + (lista[x])
        if lista[x] < numMenor:
            numMenor = lista[x]

        if  lista[x] > numMaior:
            numMaior = lista[x]

        x = x + 1

    print(f'Soma: {soma}')
    print(f'Maior: {numMaior}')
    print(f'Menor: {numMenor}')
