# Escreva um programa em Python que lê três números e que diz qual o
# maior dos números lidos.

if __name__ == '__main__':

    x = 0
    maior = 0
    lista = []

    while x < 3:
        n1 = int(input("Escreva um número: "))
        lista.append(n1)
        x = x + 1
    x = 0
    while x < 3:
        if lista[x] > maior:
            maior = lista[x]
        x = x + 1

    print(f'Maior número é: {maior}')
