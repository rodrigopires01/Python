def escrever(output, line, control):
    with open(output, control, encoding='utf-8') as file:
        file.write(line)


def ler(input, output):
    valores = []
    with open(input, encoding='utf-8') as file:
        for num, line in enumerate(file, 1):
            if num == 1:
                control = 'w'
            else:
                control = 'a'
                valores.append(line.rstrip().split(','))
            escrever(output, line, control)


if __name__ == '__main__':
    ler("bank.csv", "bank2.csv")
