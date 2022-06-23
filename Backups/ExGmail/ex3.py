# Escreva um programa em Python que pede ao utilizador que lhe forneça
# um inteiro correspondente a um número de segundos e que calcula o nú-
# mero de dias correspondentes a esse número de segundos. O seu programa
# deve permitir a interação:

def sectodays(x):
    x = x / 86400

    return x


if __name__ == '__main__':
    n1 = int(input("Escreva um número de segundos: "))

    print(f'O número de dias correspondentes é: {sectodays(int(n1))}')
