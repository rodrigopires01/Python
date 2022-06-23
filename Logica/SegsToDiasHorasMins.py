# Escreva um programa que lê um número inteiro correspondente a um
# certo número de segundos e que escreve o número de dias, horas, minutos
# e segundos correspondentes a esse número.

if __name__ == '__main__':

    n1 = float(input("Escreva um número em segundos: "))
    dia = n1 // (24 * 3600)
    n1 = n1 % (24 * 3600)
    hora = n1 // 3600
    n1 %= 3600
    minutos = n1 // 60
    n1 %= 60
    segundos = n1

    print(f'Dias: {int(dia)}')
    print(f'Horas: {int(hora)}')
    print(f'Minutos: {int(minutos)}')
    print(f'Segundos: {int(segundos)}')
