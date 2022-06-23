if __name__ == '__main__':
    empresa = ['SATA', 'TAP', 'RYANAIR']
    local = ['AÇORES', 'MADEIRA']
    passageiros = [[], [], []]
    x = 0

    while x < 3:
        y = 0
        while y < 2:
            numero = int(input(f'Insira passageiros para a {empresa[x]} em {local[y]}: '))
            passageiros[x].append(numero)
            y += 1
        x += 1

    x = 0
    while x < 3:
        print(f'Total relativo para a {empresa[x]}: {passageiros[x][0]+passageiros[x][1]}')
        x += 1
        
    x = 0
    while x < 2:
        print(f'Total relativo para {local[x]}: {passageiros[0][x]+passageiros[1][x]+passageiros[2][x]}')
        x += 1
