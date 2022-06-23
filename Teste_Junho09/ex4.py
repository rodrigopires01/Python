# Ex4: Ficheiro CSV para calcular e inquirir as dividas do cliente. Fazer calculos do maior, menor, soma, media.

def listClients():
    clients = []
    file = open("vendas.csv", encoding='utf-8')
    for num, line in enumerate(file, 1):
        clients.append(line.rstrip().split(','))

    return clients


def clientQuantity():
    clientes = listClients()
    for cli in clientes:
        idx = cli[0]
    return idx


def biggestName():
    clients = listClients()
    big = None
    biggest = []

    for cli in clients:
        if big is None:
            big = cli[1]
        else:
            if len(cli[1]) > len(big):
                big = cli[1]

    for cli in clients:
        if len(cli[1]) == len(big):
            biggest.append(cli)

    return biggest


def moreWords():
    clients = listClients()
    words = None

    for cli in clients:
        if words is None:
            words = cli[1]
        else:
            if len(cli[1].split()) > len(words.split()):
                words = cli[1]

    return words


def debtAsc():
    clients = listClients()
    check = None
    debt = []
    x = 0
    troquei = True

    for cli in clients:
        idx = cli[0]
        if check is None:
            check = 1
        else:
            debt.append(cli[4])

    while troquei:
        troquei = False
        for x in range(len(clients)):
            if x < int(idx) - 1:
                if float(debt[x]) > float(debt[x + 1]):
                    troquei = True
                    temp = debt[x]
                    debt[x] = debt[x + 1]
                    debt[x + 1] = temp
                x += 1

    return debt


if __name__ == '__main__':
    print(f'Existem {clientQuantity()} clientes!')

    print(f'Cliente com maior nome: {biggestName()}')

    print(f'Cliente com mais palavras no nome: {moreWords()}')

    print(f'Ordem Crescente do montante em divida: {debtAsc()}')











