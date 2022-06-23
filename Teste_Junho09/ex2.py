# Ex2: ficheiro CSV com informações do cliente. Tem que pedir ao utilizador o ID e dizer se o cliente existe, se não existe, e se existir mostrar as informações do cliente.

def listClients():
    clients = []
    file = open("clientes.csv", encoding='utf-8')
    for num, line in enumerate(file, 1):
        clients.append(line.rstrip().split(','))

    return clients


if __name__ == '__main__':
    clientes = listClients()

    for cli in clientes:
        idx = cli[0]

    while True:
        choice = int(input("Escolhe o ID de cliente: "))
        if choice < 1 or choice > int(idx):
            print(f'Não existe nenhum cliente com este ID!')
        else:
            print(f'Cliente Encontrado!')
            break

    print(clientes[choice])
