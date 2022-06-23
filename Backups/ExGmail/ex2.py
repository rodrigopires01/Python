# Escreva um programa em Python que lê valores correspondentes a uma
# distância percorrida (em Km) e o tempo necessário para a percorrer (em
# minutos), e calcula a velocidade média em:

def velmed(x, y):
    x = x * 1000
    y = y * 60
    total = x / y

    return total


if __name__ == '__main__':
    n1 = int(input("Escreva a distancia percorrida em KM: "))

    n2 = int(input("Escreva o tempo necessário para percorer em MINUTOS: "))

    print(f'A velocidade média em Km/h é: {(velmed(int(n1), int(n2)))*3.6} KM/h')

    print(f'A velocidade média em m/s é: {velmed(int(n1), int(n2)):.2f} m/s')
