def conversor(f):
    c = (f - 32) / 1.8
    return c


if __name__ == '__main__':
    graus = 0

    graus = float(input(f'Temperatura em ºF: '))

    print(f'Temperatura em ºC: {conversor(graus)}')
