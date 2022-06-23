def sum(num1, num2):
    total = int(num1) + int(num2)
    return total


if __name__ == '__main__':
    print('Insere um Nº')
    num1 = input()
    print('Insere outro Nº')
    num2 = input()
    print(f'{num1} + {num2} = {sum(num1, num2)}')
