"""
O ficheiro turistas.csv contem dados relativos aos turistas que visitaram os Açores o ano passado.
Escreva um programa que lê o ficheiro e sumariza a informação numa tabela de duas dimensãoes: grupo	e turistas.
Apresente a tabela devidamente formatada.

if __name__ == '__main__':
    print('Programa: TesteL3b.py')
"""


def ler(input):
    titulo = []
    valores = []
    sumario = [['Oriental'], [], ['Central'], [], ['Ocidental'], []]
    x, soma, soma2, soma3 = 0, 0, 0, 0
    file = open(input, encoding='utf-8')

    for num, line in enumerate(file, 1):
        if num == 1:
            titulo.append(line.rstrip().split(','))
        else:
            valores.append(line.rstrip().split(','))

    for valor in valores:
        if valor[0] == 'Oriental':
            soma += int(valor[3])
        if valor[0] == 'Central':
            soma2 += int(valor[3])
        if valor[0] == 'Ocidental':
            soma3 += int(valor[3])

    sumario[1].append(soma)
    sumario[3].append(soma2)
    sumario[5].append(soma3)

    print(titulo[0][0], titulo[0][3])
    while x < len(sumario) - 1:
        print(sumario[x], sumario[x+1])
        x += 2


if __name__ == '__main__':
    print('Programa: TesteL3b.py')
    print()
    ler("turistas.csv")
