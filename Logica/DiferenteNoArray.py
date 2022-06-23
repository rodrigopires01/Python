def checkNumber(lista1, lista2):
    if len(lista1) > len(lista2):
        maior = lista1
        menor = lista2
    else:
        maior = lista2
        menor = lista1

    for x in range(len(maior)):
        if maior[x] not in menor:
            return maior[x]


if __name__ == '__main__':
    array1 = [3, 4, 7, 11, -3, 1]
    array2 = [1, 4, 11, 3, 7, -3, 150]

    print(f'O número que é diferente nas duas listas é o: {checkNumber(array1, array2)}')
