texto = 'O homem de 66 anos não era visto desde domingo e esta manhã foi dado alerta para o seu desaparecimento à GNR.'


def localizar(param, text):
    vezes = 0
    for x in range(len(text)-1):
        if text[x] == param[0] and text[x+1] == param[1]:
            vezes += 1
    return vezes


if __name__ == '__main__':
    print(localizar("de", texto))
