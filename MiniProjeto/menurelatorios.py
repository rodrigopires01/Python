import os
import main


def menuRelatorios():
    menu = ['Inserir', 'Modificar', 'Eliminar', 'Listar']
    os.system("clear")
    print(f'------------------')
    print(f'| MENU Relatórios |')
    print(f'------------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]} Relatórios')
    print(f'0. Voltar')

    while True:
        escolha = int(input("Escolhe uma opção válida: "))

        if escolha == 0:
            main.mainMenu()
        elif escolha == 1:
            inserir()
        elif escolha == 2:
            modificar()
        elif escolha == 3:
            eliminar()
        elif escolha == 4:
            listar()
        else:
            continue


def inserir():
    print(f'hello-1')


def modificar():
    print(f'hello1')


def eliminar():
    print(f'hello3')


def listar():
    print(f'hello5')
