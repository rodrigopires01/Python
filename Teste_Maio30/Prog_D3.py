def checkParImpar(num, listaP, listaI):
    if num % 2 == 0:
        listaP.append(num)
        return 'par.'

    else:
        listaI.append(num)
        return 'impar.'


def checkPrimo(num, lista):
    if num <= 1:
        return 'não dá, números primos têm que ser maior que 1.'
    elif numero == 2:
        lista.append(numero)
        return 'primo'

    for x in range(2, num):
        if num % x == 0:
            return 'não primo.'
        else:
            lista.append(numero)
            return 'primo.'


def checkRepetido(num, listaNum):
    x, flag = 0, False
    while x < len(listaNum):
        if num == listaNum[x]:
            flag = True
        x += 1
    if flag:
        return True
    else:
        return False


def checkContinuar():
    check = input(f'Quer continuar ?(sim, s, yes, y) ')
    if check == 'sim' or check == 's' or check == 'yes' or check == 'y':
        return True
    else:
        return False


def checkMaiorMenor(num, listaNum):
    maior = listaNum[0]
    menor = listaNum[0]
    x = 0

    while x < len(listaNum):
        if listaNum[x] < menor:
            menor = listaNum[x]

        if listaNum[x] > maior:
            maior = listaNum[x]
        x = x + 1

    if num == maior:
        return 'o maior até agora.'
    elif num == menor:
        return 'o menor até agora.'
    else:
        return 'um numero normal.'


if __name__ == '__main__':
    repetir, repetido = True, False
    numeros, numerosPares, numerosImpares, numerosPrimos = [], [], [], []

    while repetir:
        numero = int(input(f'Insira números: '))

        if checkRepetido(numero, numeros):
            print(f'Já inseriu este número...')

            repetir = checkContinuar()
        else:
            numeros.append(numero)

            print(f'{numero} é {checkParImpar(numero, numerosPares, numerosImpares)}')
            print(f'{numero} é {checkPrimo(numero, numerosPrimos)}')
            print(f'{numero} é {checkMaiorMenor(numero, numeros)}')

            repetir = checkContinuar()
    print(f'Números Inseridos: {numeros}')
    print(f'Números Pares Inseridos: {numerosPares}')
    print(f'Números Impares Inseridos: {numerosImpares}')
    print(f'Números Primos Inseridos: {numerosPrimos}')
