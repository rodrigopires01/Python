def checkMarital(status, s, m, d):
    if status == '"single"':
        s += 1
    elif status == '"married"':
        m += 1
    elif status == '"divorced"':
        d += 1
    else:
        print(f'Erro')
    return s, m, d


def ler(ficheiro):
    valores = []
    info = [[0, 0, 0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    with open(ficheiro, encoding='utf-8') as file:
        for num, line in enumerate(file, 1):
            if num == 1:
                continue
            else:
                valores.append(line.rstrip().split(','))

    for value in valores:
        if int(value[0]) <= 20:
            info[0][0] += 1
            info[1][0], info[1][1], info[1][2] = checkMarital(value[2], info[1][0], info[1][1], info[1][2])
        elif int(value[0]) <= 40:
            info[0][1] += 1
            info[2][0], info[2][1], info[2][2] = checkMarital(value[2], info[2][0], info[2][1], info[2][2])
        elif int(value[0]) <= 60:
            info[0][2] += 1
            info[3][0], info[3][1], info[3][2] = checkMarital(value[2], info[3][0], info[3][1], info[3][2])
        elif int(value[0]) <= 80:
            info[0][3] += 1
            info[4][0], info[4][1], info[4][2] = checkMarital(value[2], info[4][0], info[4][1], info[4][2])
        elif int(value[0]) <= 100:
            info[0][4] += 1
            info[5][0], info[5][1], info[5][2] = checkMarital(value[2], info[5][0], info[5][1], info[5][2])
        else:
            print(f'Algum erro aconteceu')

    print(f'Entre 0 e 20   = {info[0][0]}    ||||| {info[1][0]} divorciados, {info[1][1]}, casados e {info[1][2]} solteiros.')
    print(f'Entre 21 e 40  = {info[0][1]} ||||| {info[2][0]} divorciados, {info[2][1]}, casados e {info[2][2]} solteiros.')
    print(f'Entre 41 e 60  = {info[0][2]} ||||| {info[3][0]} divorciados, {info[3][1]}, casados e {info[3][2]} solteiros.')
    print(f'Entre 61 e 80  = {info[0][3]}  ||||| {info[4][0]} divorciados, {info[4][1]}, casados e {info[4][2]} solteiros.')
    print(f'Entre 81 e 100 = {info[0][4]}    ||||| {info[5][0]} divorciados, {info[5][1]}, casados e {info[5][2]} solteiros.')


if __name__ == '__main__':
    ler("bank.csv")
