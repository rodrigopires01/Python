"""
Peça ao utilizador para inserir contínuamente datas no formato DD-MM-YYYY
Apresente uma - e apenas uma - das seguintes mensagens, sempre que se aplique:

'A data inserida não tem 10 caracteres'
'A data inserida não tem dois traços'
'A data inserida não tem dois caracteres antes do primeiro traço'
'A data inserida não tem dois caracteres entre o primeiro traço e o segundo traço'
'A data inserida não tem quatro caracteres depois do segundo traço'
'O mês é inválido'
'O dia é inválido'

Quando o programa terminar, deverá apresentar o seguinte sumário:
print(f'Número de datas válidas inseridos: {inseridas}')
print(f'Número de mensagens de erro apresentadas : {erros}')

NOTA: Para a quantidade de datas inseridos só conta datas válidas
"""


def validar_data(date):
    errorMsg1 = 'A data inserida não tem 10 caracteres'
    errorMsg2 = 'A data inserida não tem dois traços'
    errorMsg3 = 'A data inserida não tem dois caracteres antes do primeiro traço'
    errorMsg4 = 'A data inserida não tem dois caracteres entre o primeiro traço e o segundo traço'
    errorMsg5 = 'A data inserida não tem quatro caracteres depois do segundo traço'
    errorMsg6 = 'O mês é inválido'
    errorMsg7 = 'O dia é inválido'
    var = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    checkHifen = 0
    dia, mes, ano = data.split('-')

    if int(len(date)) < 10:
        print(errorMsg1)
        return False

    for car in date:
        if car == '-':
            checkHifen += 1

    if int(checkHifen) != 2:
        print(errorMsg2)
        return False

    if data[0] not in var or data[1] not in var and data[2] == "-":
        print(errorMsg3)
        return False

    if data[2] == "-" and data[3] not in var or data[4] not in var and data[5] == "-":
        print(errorMsg4)
        return False

    if data[5] == "-" and data[6] not in var or data[7] not in var or data[8] not in var or data[9] not in var:
        print(errorMsg5)
        return False

    if int(mes) < 1 or int(mes) > 12:
        print(errorMsg6)
        return False

    if int(mes) == 2:
        if int(ano) % 4 != 0 and int(dia) > 28 or int(dia) < 1:
            print(errorMsg7)
            return False
        elif int(ano) % 4 == 0 and int(dia) > 29 or int(dia) < 1:
            print(errorMsg7)
            return False

    elif int(mes) in (4, 6, 9, 11) and int(dia) > 30 or int(dia) < 1:
        print(errorMsg7)
        return False

    elif int(mes) in (1, 3, 5, 7, 8, 10, 12) and int(dia) > 31 or int(dia) < 1:
        print(errorMsg7)
        return False

    return True


if __name__ == '__main__':
    print('Programa: TesteL1c.py')

    inseridas, erros = 0, 0

    while True:
        data = input('Insira datas válidas [Exemplo: 31-01-2022]: ')
        if validar_data(data):
            print(f'A data "{data}" é válida!')
            inseridas += 1
        else:
            print(f'A data "{data}" é inválida!')
            erros += 1
        if input(f'Deseja continuar? s/n') != 's':
            break

    print(f'Número de datas válidas inseridos: {inseridas}')
    print(f'Número de mensagens de erro apresentadas : {erros}')
