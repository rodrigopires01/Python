def compare(num1, num2):
    if num1 > num2:
        res = 'é maior que'
    elif num2 > num1:
        res = 'é menor que'
    else:
        res = 'é igual a'
    return res


if __name__ == '__main__':
    print('Insere um Nº')
    num1 = input()
    print('Insere outro Nº')
    num2 = input()
    print(f'{num1} {compare(int(num1), int(num2))} {num2}')
