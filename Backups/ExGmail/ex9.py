# Escreva um programa em Python que lê uma sequência de dígitos, sendo
# cada um dos dígitos fornecido numa linha separada, e calcula o número
# inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a
# sequência de dígitos é fornecido ao programa o inteiro 1. O seu programa
# deve permitir a interação:
if __name__ == '__main__':

    x = 0
    num = ""

    while x < 1:
        n1 = input("Escreva um número: ")

        if n1 == "-1":
            print(f'O número é: {num}')
            break
        else:
            num = num + n1
