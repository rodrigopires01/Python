"""
O objetivo do exercício é completar o programa de forma a validar datas inseridas no formato DD-MM-YYYY
Para a data ser válida, o ano deverá estar entre 1900 e 2022, o mês entre 1 e 12
e o dia entre 1 e o número máximo de dias para o mês em questão. Quando o ano for
divisível por 4, o mês de Fevereiro tem 29 dias, caso contrário tem apenas 28.
NOTA IMPORTANTE: Não é permitido adicionar ou remover funções nem eliminar qualquer código já existente.
                 Linhas com "# ..." são um aindicação dos locais possíveis que deve preencher, mas não é obrigatório.

"""


def separar_data(data):
    """
    Separa as componentes da data

    :param data: data que irá ser decomposta em dia, mês, ano
    :return: dia, mes, ano
    """
    dia, mes, ano = data.split('-')

    return dia, mes, ano


def ultimo_dia_do_mes(mes, ano):
    """
    Retorna o número de dias no mês
    :param mes: Mês
    :return: Número de dias no mês
    """
    if int(mes) in (4, 6, 9, 11):
        ultimo = 30
    elif int(mes) == 2:
        if int(ano) % 4 == 0:
            ultimo = 29
        else:
            ultimo = 28
    else:
        ultimo = 31

    return ultimo


def formato_correto(data):
    """
    Verifica se o formato da data inserida está de acordo com DD-MM-YYYY. Por correto entenda-se dois digitos seguidos
    de um traço, seguido de dois digitos, seguido de um traço, seguido de 4 digitos.

    :param data: data alvo da verificação
    :return: True ou False para indicar se o formato está correto ou não
    """
    var = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if data[0] in var and data[1] in var and data[2] == "-" and data[3] in var and data[4] in var and data[5] == "-" and \
            data[6] in var and data[7] in var and data[8] in var and data[9] in var:
        correto = True
    else:
        correto = False

    return correto


def validar_data(data):
    """
    Recebe a data e verifica se a data é válida. Se a data for válida retorna True, caso contrário
    apresenta uma das 3 mensagens de erro e retorna False.

    :param data: data alvo da verificação
    :return: True or False em função da data ser válida or inválida
    """

    valida = None

    if formato_correto(data):
        dia, mes, ano = separar_data(data)
        msg1 = f'O ano "{ano}" deverá ser entre 1900 e 2022.'
        msg2 = f'O mês "{mes}" deverá ser entre 1 e 12.'
        msg3 = f'O dia "{dia}" deverá ser entre 1 e {ultimo_dia_do_mes(mes, ano)}'

        if int(dia) < 1 or int(dia) > int(ultimo_dia_do_mes(mes, ano)):
            print(msg3)
            valida = False
        elif int(mes) < 1 or int(mes) > 12:
            print(msg2)
            valida = False
        elif int(ano) < 1900 or int(ano) > 2022:
            print(msg1)
            valida = False
        else:
            valida = True

    else:
        print(f'"{data}" não está no formato DD-MM-YYYY')

    return valida


if __name__ == '__main__':
    """
    O programa deverá continuamente pedir ao utilizador para inserir uma data. Após validar a data, o programa 
    deverá perguntar se o utilizador quer verificar mais alguma data. Se o utilizador disser que sim (s) deverá
    voltar a pedir uma data e assim sucessivamente.
    """

    while True:
        data = input('Insira uma data no formato DD-MM-YYYY [Exemplo: 31-01-2022]: ')
        if data == '0':
            exit()
        if validar_data(data):
            print(f'A data "{data}" é válida!')
        else:
            print(f'A data "{data}" é inválida!')
        if input(f'Deseja continuar? s/n') != 's':
            break
