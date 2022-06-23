import os
import main


def menuEncomendas():
    menu = ['Manter', 'Manter Detalhe da']
    os.system("clear")
    print(f'------------------')
    print(f'| MENU Encomendas |')
    print(f'------------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]} Encomenda')
    print(f'0. Voltar')

    while True:
        escolha = int(input("Escolhe uma opção válida: "))

        if escolha == 0:
            main.mainMenu()
        elif escolha == 1:
            manterEncomenda()
        elif escolha == 2:
            manterDetalhe()
        else:
            continue


def manterEncomenda():
    menu = ['Inserir', 'Modificar', 'Eliminar', 'Listar']
    os.system("clear")
    print(f'------------------')
    print(f'| MENU Encomenda |')
    print(f'------------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]} Encomenda')
    print(f'0. Voltar')

    while True:
        escolha = int(input("Escolhe uma opção válida: "))

        if escolha == 0:
            menuEncomendas()
        elif escolha == 1:
            inserirE()
        elif escolha == 2:
            modificarE()
        elif escolha == 3:
            eliminarE()
        elif escolha == 4:
            listarE()
        else:
            continue


def manterDetalhe():
    menu = ['Inserir', 'Modificar', 'Eliminar', 'Listar']
    os.system("clear")
    print(f'------------------')
    print(f'| MENU Detalhe Encomenda |')
    print(f'------------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]} Detalhe da Encomenda')
    print(f'0. Voltar')

    while True:
        escolha = int(input("Escolhe uma opção válida: "))

        if escolha == 0:
            menuEncomendas()
        elif escolha == 1:
            inserirD()
        elif escolha == 2:
            modificarD()
        elif escolha == 3:
            eliminarD()
        elif escolha == 4:
            listarD()
        else:
            continue


def inserirE():
    print(f'hello-1')


def modificarE():
    print(f'hello1')


def eliminarE():
    print(f'hello3')


def listarE():
    print(f'hello5')


def inserirD():
    print(f'hello-1')


def modificarD():
    print(f'hello1')


def eliminarD():
    print(f'hello3')


def listarD():
    print(f'hello5')