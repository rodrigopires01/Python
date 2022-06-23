def escrever(output, line, control):
    with open(output, control, encoding='utf-8') as file:
        file.write(line)


def ler(ficheiro, output):
    passageiros = []
    totalS, totalR, totalT = 0, 0, 0
    with open(ficheiro, encoding='utf-8') as file:
        for num, line in enumerate(file, 1):
            passageiros.append(line.rstrip().split(','))

    x = 1
    while x < len(passageiros):
        total = int(passageiros[x][1]) + int(passageiros[x][2]) + int(passageiros[x][3])
        escrever(output, f'Total {passageiros[x][0]}: {total}\n', 'a')
        print(f'Total {passageiros[x][0]}: {int(passageiros[x][1]) + int(passageiros[x][2]) + int(passageiros[x][3])}')
        x += 1
    print(f'----------------')
    x = 1
    while x < 12:
        totalS += int(passageiros[x][1])
        x += 1
    x = 1
    while x < 12:
        totalR += int(passageiros[x][2])
        x += 1
    x = 1
    while x < 12:
        totalT += int(passageiros[x][3])
        x += 1

    escrever(output, f'---------------------------\n', 'a')
    escrever(output, f'Total {passageiros[0][1]}: {totalS}\n', 'a')
    escrever(output, f'Total {passageiros[0][2]}: {totalR}\n', 'a')
    escrever(output, f'Total {passageiros[0][3]}: {totalT}\n', 'a')


if __name__ == '__main__':
    print(ler("passageiros.csv", "resultado.txt"))
