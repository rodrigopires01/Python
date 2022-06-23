import os

import menuclientes
import menuprodutos
import menutransportes
import menuencomendas
import menurelatorios


def mainMenu():
    menu = ['Clientes', 'Produtos', 'Transportes', 'Encomendas', 'Relatórios']
    os.system("clear")
    print(f'------------------')
    print(f'| MENU PRINCIPAL |')
    print(f'------------------')
    for x in range(len(menu)):
        print(f'{x + 1}. {menu[x]}')
    print(f'0. Sair')

    while True:
        escolha = int(input("Escolhe uma opção válida: "))

        if escolha == 0:
            exit()
        elif escolha == 1:
            menuclientes.menuClientes()
        elif escolha == 2:
            menuprodutos.menuProdutos()
        elif escolha == 3:
            menutransportes.menuTransportes()
        elif escolha == 4:
            menuencomendas.menuEncomendas()
        elif escolha == 5:
            menurelatorios.menuRelatorios()
        else:
            continue


if __name__ == '__main__':
    mainMenu()
