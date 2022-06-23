def escrever(output, line, control):
    with open(output, control, encoding='utf-8') as file:
        file.write(line)


def ler(ficheiro):
    a, b = 0, 0
    valores = []

    with open(ficheiro, encoding='utf-8') as file:
        for num, line in enumerate(file, 1):
            if num == 1:
                escrever("bankBalance.csv", line, 'w')
            else:
                dados = line.rstrip().split(',')
                if int(dados[0]) <= 20:
                    valores.append(line.rstrip().split(','))

    for linha in valores:
        print(linha)
    print('---------------------')
    while a < len(valores[0]) - 1:
        b = a + 1
        while b < len(valores[0]) - 1:
            if valores[a][5] > valores[b][5]:
                temp = valores[a][5]
                valores[a][5] = valores[b][5]
                valores[b][5] = temp
            b += 1
        a += 1

    for linha in valores:
        print(linha)


if __name__ == '__main__':
    ler("bank.csv")
