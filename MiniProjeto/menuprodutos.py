import os
import main


def menuP():
    menu = ['Inserir', 'Modificar', 'Eliminar', 'Listar']
    print(f'-----------------')
    print(f'| MENU Produtos |')
    print(f'-----------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]} Produtos')
    print(f'5. Limpar Ecrã')
    print(f'0. Voltar')


def menuProdutos():
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


def updateProdutos():
    produtos = []
    file = open("produtos.csv", encoding='utf-8')
    for num, line in enumerate(file, 1):
        produtos.append(line.rstrip().split(','))

    return produtos


def inserir():
    idx = 0
    produtos = updateProdutos()
    for prod in produtos:
        idx = prod[0]

    while True:
        nomeProd = str(input("Nome do Produto: "))
        print()
        precoProd = str(input("Preço do Produto: "))
        print()
        stockProd = str(input("Stock do Produto: "))
        print()
        encomendasProd = str(input("Encomendas do Produto: "))
        print()
        minimoProd = str(input("Minimo do Produto: "))
        print()
        print(f'Produto Adicionado com sucesso.')

        fileW = open("produtos.csv", "a", encoding='utf-8')
        fileW.write(
            f'{int(idx) + 1}, "{nomeProd}", "{precoProd}", {stockProd}, {encomendasProd}, {minimoProd}\n')

        if input(f'Continuar? (s/n)') is not 's':
            limparEcra()
            menuP()
            break


def modificar():
    limparEcra()
    listar()
    print()
    idx = 0
    produtos = updateProdutos()
    fileR = open("produtos.csv", "r")
    linhas = fileR.readlines()

    while True:
        for prod in produtos:
            idx = prod[0]
        print(f'0. Voltar')
        print()
        while True:
            choice = int(input("Escolhe o ID para alterar: "))
            if choice < 0 or choice > int(idx):
                print(f'Escolhe um ID válido!')
            elif choice == 0:
                menuProdutos()
            else:
                break

        while True:
            print(f'1 - Nome  |  2 - Preço  | 3 - Stock  | 4 - Encomendas  |  5 - Minimo')
            alterar = int(input("O que é que quer alterar?: "))
            if alterar < 1 or alterar > 5:
                print(f'Escolhe um ID válido!')
            else:
                break

        if alterar == 1:
            novoNome = str(input("Novo Nome: "))
            print(f'O Nome foi alterado com sucesso!')
            print(f'Nome Antigo:{produtos[choice][alterar]} | Nome Atual: {novoNome}')
            linhas[
                choice] = f'{choice}, "{novoNome}",{produtos[choice][2]},{produtos[choice][3]},{produtos[choice][4]},{produtos[choice][5]}\n'

        elif alterar == 2:
            novoPreco = str(input("Novo Preço: "))
            print(f'O Preço foi alterado com sucesso!')
            print(f'Preço Antigo:{produtos[choice][alterar]} | Preço Atual: {novoPreco}')
            linhas[
                choice] = f'{choice},{produtos[choice][1]}, "{novoPreco}",{produtos[choice][3]},{produtos[choice][4]},{produtos[choice][5]}\n'
        elif alterar == 3:
            novoStock = str(input("Novo Stock: "))
            print(f'O Stock foi alterado com sucesso!')
            print(f'Stock Antigo:{produtos[choice][alterar]} | Stock Atual: {novoStock}')
            linhas[
                choice] = f'{choice},{produtos[choice][1]},{produtos[choice][2]}, {novoStock},{produtos[choice][4]},{produtos[choice][5]}\n'
        elif alterar == 4:
            novoEncomendas = str(input("Novas Encomendas: "))
            print(f'As Encomendas foram alteradas com sucesso!')
            print(f'Encomendas Antigas:{produtos[choice][alterar]} | Encomendas Atuais: {novoEncomendas}')
            linhas[
                choice] = f'{choice},{produtos[choice][1]},{produtos[choice][2]},{produtos[choice][3]}, {novoEncomendas},{produtos[choice][5]}\n'
        elif alterar == 5:
            novoMinimo = str(input("Novo Minimo: "))
            print(f'O Minimo foi alterado com sucesso!')
            print(f'Minimo Antigo:{produtos[choice][alterar]} | Minimo Atual: {novoMinimo}')
            linhas[
                choice] = f'{choice},{produtos[choice][1]},{produtos[choice][2]},{produtos[choice][3]},{produtos[choice][4]}, {novoMinimo}\n'
        else:
            print(f'Algum erro aconteceu!')

        fileW = open("produtos.csv", "w")
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
    produtos = updateProdutos()
    produtosAt = []

    for prod in produtos:
        idx = prod[0]
    print(f'0. Voltar')
    print()

    while True:
        choice = int(input("Escolhe o ID para apagar: "))
        if choice < 0 or choice > int(idx):
            print(f'Escolhe um ID válido!')
        elif choice == 0:
            menuProdutos()
        else:
            limparEcra()
            menuP()
            break

    fileR = open("produtos.csv", "r")
    for row in fileR:
        if str(row[0]) == str(choice):
            print()
        else:
            produtosAt.append(row)

    fileW = open("produtos.csv", "w")
    for prod in produtosAt:
        fileW.write(prod)


def listar():
    produtos = updateProdutos()
    for prod in produtos:
        print(f'{prod[0]: <4} {prod[1]: <15} {prod[2]: <10} {prod[3]: <10} {prod[4]: <15} {prod[5]: <10}')
