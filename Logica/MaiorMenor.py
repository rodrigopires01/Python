from random import *

if __name__ == '__main__':
    lista = [randrange(50), randrange(50), randrange(50), randrange(50), randrange(50)]

    soma = 0
    numMaior = lista[0]
    numMenor = lista[0]

    for x in range(len(lista)):
        soma = soma + (lista[x])
        if lista[x] < numMenor:
            numMenor = lista[x]

        if  lista[x] > numMaior:
            numMaior = lista[x]

    print(f'Soma: {soma}')
    print(f'Maior: {numMaior}')
    print(f'Menor: {numMenor}')
