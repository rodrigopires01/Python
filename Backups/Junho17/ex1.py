def escrever():
    writeToFile = open("input.csv", "a", encoding='utf-8')
    writeToFile.write("O homem de 66 anos não era visto desde domingo e esta manhã foi dado alerta para o seu desaparecimento à GNR.\n")
    writeToFile.close()


if __name__ == '__main__':
    contador = 1

    readFile = open("input.csv", encoding='utf-8')
    for line in readFile:
        frase = line
        for x in range(len(frase)):
            if frase[x] == ' ':
                contador += 1

    print(f'Palavras: {contador}')
