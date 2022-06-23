import os
import main


def menuP():
    menu = ['Inserir', 'Modificar', 'Eliminar', 'Listar']
    print(f'------------------')
    print(f'| MENU Clientes |')
    print(f'------------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]} Clientes')
    print(f'5. Limpar Ecrã')
    print(f'0. Voltar')


def menuClientes():
    limparEcra()
    menuP()

    while True:
        escolha = int(input("Escolhe uma opção válida: "))

        if escolha == 0:
            main.mainMenu()
        elif escolha == 1:
            print()
            inserir()
            print()
        elif escolha == 2:
            print()
            modificar()
            print()
        elif escolha == 3:
            print()
            eliminar()
            print()
        elif escolha == 4:
            print()
            listar()
            print()
        elif escolha == 5:
            limparEcra()
            menuP()
        else:
            continue


def limparEcra():
    os.system("clear")


def updateClientes():
    clientes = []
    file = open("clientes.csv", encoding='utf-8')
    for num, line in enumerate(file, 1):
        clientes.append(line.rstrip().split(','))

    return clientes


def inserir():
    idx = 0
    clientes = updateClientes()
    for cli in clientes:
        idx = cli[0]

    while True:
        nomeCli = str(input("Nome: "))
        print()
        moradaCli = str(input("Morada: "))
        print()
        codpostalCli = str(input("Codigo Postal: "))
        print()
        localidadeCli = str(input("Localidade: "))
        print()
        telefoneCli = str(input("Nº Telefone: "))
        print()
        print(f'Cliente Adicionado com sucesso.')

        fileW = open("clientes.csv", "a", encoding='utf-8')
        fileW.write(
            f'{int(idx) + 1}, "{nomeCli}", "{moradaCli}", "{codpostalCli}", "{localidadeCli}", {telefoneCli}\n')

        if input(f'Continuar? (s/n)') is not 's':
            limparEcra()
            menuP()
            break


def modificar():
    limparEcra()
    listar()
    print()
    idx = 0
    clientes = updateClientes()
    fileR = open("clientes.csv", "r")
    linhas = fileR.readlines()

    while True:
        for prod in clientes:
            idx = prod[0]
        print(f'0. Voltar')
        print()
        while True:
            choice = int(input("Escolhe o ID para alterar: "))
            if choice < 0 or choice > int(idx):
                print(f'Escolhe um ID válido!')
            elif choice == 0:
                menuClientes()
            else:
                break

        while True:
            print(f'1 - Nome  |  2 - Morada  | 3 - Cod Postal  | 4 - Localidade  |  5 - Nº Telefone')
            alterar = int(input("O que é que quer alterar?: "))
            if alterar < 1 or alterar > 5:
                print(f'Escolhe um ID válido!')
            else:
                break

        if alterar == 1:
            novoNome = str(input("Novo Nome: "))
            print(f'O Nome foi alterado com sucesso!')
            print(f'Nome Antigo:{clientes[choice][alterar]} | Nome Atual: {novoNome}')
            linhas[
                choice] = f'{choice}, "{novoNome}",{clientes[choice][2]},{clientes[choice][3]},{clientes[choice][4]},{clientes[choice][5]}\n'

        elif alterar == 2:
            novaMorada = str(input("Nova Morada: "))
            print(f'A Morada foi alterada com sucesso!')
            print(f'Morada Antigo:{clientes[choice][alterar]} | Morada Atual: {novaMorada}')
            linhas[
                choice] = f'{choice},{clientes[choice][1]}, "{novaMorada}",{clientes[choice][3]},{clientes[choice][4]},{clientes[choice][5]}\n'
        elif alterar == 3:
            novoCodPostal = str(input("Novo Codigo Postal: "))
            print(f'O Codigo Postal foi alterado com sucesso!')
            print(f'Codigo Postal Antigo:{clientes[choice][alterar]} | Codigo Postal Atual: {novoCodPostal}')
            linhas[
                choice] = f'{choice},{clientes[choice][1]},{clientes[choice][2]}, "{novoCodPostal}",{clientes[choice][4]},{clientes[choice][5]}\n'
        elif alterar == 4:
            novoLocalidade = str(input("Nova Localidade: "))
            print(f'A Localidade foi alterada com sucesso!')
            print(f'Localidade Antiga:{clientes[choice][alterar]} | Encomendas Atuais: {novoLocalidade}')
            linhas[
                choice] = f'{choice},{clientes[choice][1]},{clientes[choice][2]},{clientes[choice][3]}, "{novoLocalidade}",{clientes[choice][5]}\n'
        elif alterar == 5:
            novoTelefone = str(input("Novo Nº Telefone: "))
            print(f'O Nº Telefone foi alterado com sucesso!')
            print(f'Nº Telefone Antigo:{clientes[choice][alterar]} | Nº Telefone Atual: {novoTelefone}')
            linhas[
                choice] = f'{choice},{clientes[choice][1]},{clientes[choice][2]},{clientes[choice][3]},{clientes[choice][4]}, {novoTelefone}\n'
        else:
            print(f'Algum erro aconteceu!')

        fileW = open("clientes.csv", "w")
        fileW.writelines(linhas)
        fileW.close()

        if input(f'Continuar? (s/n)') is not 's':
            limparEcra()
            menuP()
            break


def eliminar():
    limparEcra()
    listar()
    print()
    idx = 0
    clientes = updateClientes()
    clientesAt = []

    for cli in clientes:
        idx = cli[0]
    print(f'0. Voltar')
    print()

    while True:
        choice = int(input("Escolhe o ID para apagar: "))
        if choice < 0 or choice > int(idx):
            print(f'Escolhe um ID válido!')
        elif choice == 0:
            menuClientes()
        else:
            limparEcra()
            menuP()
            break

    fileR = open("clientes.csv", "r")
    for row in fileR:
        if str(row[0]) == str(choice):
            print()
        else:
            clientesAt.append(row)

    fileW = open("clientes.csv", "w")
    for prod in clientesAt:
        fileW.write(prod)


def listar():
    clientes = updateClientes()
    for cli in clientes:
        print(f'{cli[0]: <4} {cli[1]: <25} {cli[2]: <20} {cli[3]: <15} {cli[4]: <20} {cli[5]: <10}')
