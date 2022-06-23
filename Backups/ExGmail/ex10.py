# Escreva um programa em Python que lê um número inteiro positivo e
# calcula o número obtido do número lido que apenas contém os seus dígitos
# impares.
if __name__ == '__main__':

    x = 0
    impar = ""

    n1 = list(input("Escreva um número: "))

    for x in n1[x]:
        if n1[x] % 2 != 0:
            impar = impar + n1
            x = x + 1
        else:
            x = x + 1

    print(f'Resultado: {impar}')
