def ler(ficheiro):
    valores = []
    with open(ficheiro) as file:
        for num, line in enumerate(file, 1):
            if num == 1:
                titulos = line.rstrip().split(',')
            else:
                if int(valores[0]) <= 20:
                    escrever("bank1.csv", line, 'a')
                    grupo1 += 1
                elif int(valores[0]) <= 40:
                    escrever("bank2.csv", line, 'a')
                    grupo2 += 1
                elif int(valores[0]) <= 60:
                    escrever("bank3.csv", line, 'a')
                    grupo3 += 1
                elif int(valores[0]) <= 80:
                    escrever("bank4.csv", line, 'a')
                    grupo4 += 1
                elif int(valores[0]) <= 100:
                    escrever("bank5.csv", line, 'a')
                    grupo5 += 1
                else:
                    print(f'Algum erro aconteceu')

    soma, media, casados, solteiros, divorciados, outros = 0, 0, 0, 0, 0, 0
    maior = int(valores[0][0])
    menor = int(valores[0][0])

    for valor in valores:
        soma = soma + int(valor[0])
        if int(valor[0]) > maior:
            maior = int(valor[0])
        if int(valor[0]) < menor:
            menor = int(valor[0])

    for estado in valores:
        if estado[2] == '"married"':
            casados += 1
        elif estado[2] == '"divorced"':
            divorciados += 1
        elif estado[2] == '"single"':
            solteiros += 1
        else:
            outros += 1

    print(f'Registos: {num}')
    print(f'-------------------------------')
    print(f'Maior Idade: {maior}')
    print(f'-------------------------------')
    print(f'Menor Idade: {menor}')
    print(f'-------------------------------')
    print(f'Media das Idades: {soma/num:.2f}')
    print(f'-------------------------------')
    print(f'Casados: {casados}')
    print(f'-------------------------------')
    print(f'Solteiros: {solteiros}')
    print(f'-------------------------------')
    print(f'Divorciados: {divorciados}')
    print(f'-------------------------------')
    print(f'Outros: {outros}')


if __name__ == '__main__':
    ler("bank.csv")
