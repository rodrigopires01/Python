# Escreva um programa em Python que pede ao utilizador que lhe forneça
# dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).

def calculo(x, y):
    total = (x + 3 * y) * (x - y)
    return total


if __name__ == '__main__':
    n1 = int(input("Escreva o primeiro número: "))
    n2 = int(input("Escreva o segundo número: "))

    print(f'O valor de (x + 3 * y) * (x - y) é: {calculo(int(n1), int(n2))}')
