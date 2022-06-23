# Escreva um programa em Python que lê cinco números reais e calcula a
# sua média e o seu desvio padrão.
from statistics import pstdev

if __name__ == '__main__':

    x = 0
    soma = 0
    lista = []

    while x < 5:
        n1 = int(input("Escreva um número: "))
        lista.append(n1)
        soma = soma + n1
        x = x + 1

    print(f'Média: {soma/5:.2f}')
    print(f'Desvio Padrão: {pstdev(lista):.2f}')
