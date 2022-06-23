def conversor(f):
    c = (f - 32) / 1.8
    return c


def checkContinuar():
    check = input(f'Quer continuar ?(sim, s, yes, y) ')
    if check == 'sim' or check == 's' or check == 'yes' or check == 'y':
        return True
    else:
        return False


if __name__ == '__main__':
    graus, repetir = 0, True

    while repetir:
        graus = 0

        graus = float(input(f'Temperatura em ºF: '))

        print(f'Temperatura em ºC: {conversor(graus)}')

        repetir = checkContinuar()
