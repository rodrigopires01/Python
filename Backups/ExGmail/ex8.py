# Escreva um programa em Python que pede ao utilizador que lhe forneça
# uma sucessão de inteiros correspondentes a valores em segundos e que
# calcula o número de dias correspondentes a cada um desses inteiros. O
# programa termina quando o utilizador fornece um número negativo. O
# seu programa deve possibilitar a seguinte interação:
if __name__ == '__main__':

    x = 0

    while x < 1:
        n1 = int(input("Escreva um número em segundos: "))

        if n1 >= 0:
            dias = n1 / 84600
            print(f'Dias: {dias:.5f}')
        else:
            print(f'Escreveu um número negativo...')
            break
