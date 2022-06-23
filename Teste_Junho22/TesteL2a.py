"""
Pergunte ao utilizador quantos números deseja, mas só aceite a resposta se o número for ímpar.
Sorteie essa quantidade de números e insira-os na lista nums, tendo o cuidado de não inserir números que já estão lá.
Os números sorteados deverão estar entre 1 e 100 inclusive.

Apresente:
A lista de números sorteada
[12, 1, 4, 16, 23, 9, 2]
A lista de números sorteada ordenada de forma crescente
[1, 2, 4, 9, 12, 16, 23]
A lista de números sorteada ordenada de forma decrescente
[23, 16, 12, 9, 4, 2, 1]
A lista de números sorteada com a primeira metade ordenada de forma crescente e a segunda metade de forma decrescente
[1, 2, 4, 9, 23, 16, 12]
A lista de números sorteada com a primeira metade ordenada de forma decrescente e a segunda metade de forma crescente
[23, 16, 12, 9, 4, 2, 1]
print(f'Quantidade de números sorteados: {inseridos}')
Quantidade de números sorteados: 7
print(f'O maior número inserido: {maior}')
O maior número inserido: 23
print(f'O menor número inserido: {menor}')
O menor número inserido: 1
print(f'A soma dos números inseridos: {soma}')
A soma dos números inseridos: 67

if __name__ == '__main__':
    print('Programa: TesteL2a.py')
    nums = []
"""
from random import randrange


def ordernar(lista, ordem):
    troquei = True

    while troquei:
        troquei = False
        for x in range(len(lista) - 1):
            if lista[x] * ordem > lista[x + 1] * ordem:
                troquei = True
                temp = lista[x]
                lista[x] = lista[x + 1]
                lista[x + 1] = temp

    return lista


def ordenarCreDec(lista):
    listaMetade = []
    a = 0
    while a < (len(lista) / 2):
        listaMetade.append(lista[a])
        a = a + 1

    b = len(lista) - 1
    while b >= (len(lista) / 2):
        listaMetade.append(lista[b])
        b = b - 1

    return listaMetade


def ordenarDecCre(lista):
    listaMetade = []
    a = 0

    b = len(lista) - 1
    while b >= (len(lista) / 2):
        listaMetade.append(lista[b])
        b = b - 1

    while a < (len(lista) / 2):
        listaMetade.append(lista[a])
        a = a + 1

    return listaMetade


if __name__ == '__main__':
    print('Programa: TesteL2a.py')
    nums = []
    soma = 0

    while True:
        quantidade = input('Quantos Números Deseja? ')
        if int(quantidade) % 2 != 0:
            break
        else:
            print(f'Tenta outra vez...')

    for x in range(int(quantidade)):
        nums.append(randrange(100))

    maior = nums[0]
    menor = nums[0]

    for x in nums:
        soma = soma + x

        if x > maior:
            maior = x
            y = x

        if x < menor:
            menor = x
            z = x
        x += 1

    print(f'A lista de números sorteada: {nums}')
    print(f'A lista de números sorteada ordenada de forma crescente: {ordernar(nums, 1)}')
    print(f'A lista de números sorteada ordenada de forma decrescente: {ordernar(nums, -1)}')
    print(f'A lista de números sorteada com a primeira metade ordenada de forma crescente e a segunda metade de forma decrescente: {ordenarCreDec(ordernar(nums, 1))}')
    print(f'A lista de números sorteada com a primeira metade ordenada de forma decrescente e a segunda metade de forma crescente: {ordenarDecCre(ordernar(nums, 1))}')
    print(f'Quantidade de números sorteados: {quantidade}')
    print(f'O maior número inserido: {maior}')
    print(f'O menor número inserido: {menor}')
    print(f'A soma dos números inseridos: {soma}')
