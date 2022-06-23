def escrever(output, line, control):
    with open(output, control, encoding='utf-8') as file:
        file.write(line)


def ler(input):
    grupo1, grupo2, grupo3, grupo4, grupo5 = 0, 0, 0, 0, 0
    with open(input, encoding='utf-8') as file:
        for num, line in enumerate(file, 1):
            if num == 1:
                escrever("bank1.csv", line, 'w')
                escrever("bank2.csv", line, 'w')
                escrever("bank3.csv", line, 'w')
                escrever("bank4.csv", line, 'w')
                escrever("bank5.csv", line, 'w')
            else:
                valores = line.rstrip().split(',')

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


if __name__ == '__main__':
    ler("bank.csv")
