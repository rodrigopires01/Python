"""
O ficheiro salarios.csv contem a informação salarial dos colaboradores da empresa. Para além do salário e dos
descontos para a segurança social, contem ainda as ilhas nas quais o colaborador prestou serviços.

Escreva uma programa que permite ao utilizador interagir com o ficheiro.



print(f'* * * *   M E N U   * * * *')
print(f'10 - Mostrar/guardar tabelas de salários')
print(f'11 - Inserir registo')
print(f'12 - Modificar registo por ID')
print(f'13 - Eliminar registo por ID')
print(f'14 - Pesquisar por ID')
print(f'15 - Pesquisar por nome')
print(f'16 - Pesquisar por código postal')
print(f'17 - Mostrar a tabela por ordem decrescente de XXXXX')
print(f'18 - Mostrar/guardar regito(s) do colaborador com o salário bruto mais elevado')
print(f'19 - Mostrar o total dos salários brutos')
print(f'20 - Mostrar o total dos descontos para a segurança social')
print(f'21 - Mostrar o total dos descontos para o seguro')
print(f'22 - Mostrar os IDs e nomes dos colaboradores que trabalharam numa determinada ilha')
print(f'23 - Mostrar quantos colaboradores há em cada código postal')
print(f'24 - Listagem de registos personalizada')
print(f'99 - Sair')

Em todos os casos de "Mostrar/guardar" deverá sempre perguntar se o utilizador pretende guardar os resultados. Se assim
for, o nome do ficheiro de output é semre TesteL3a_XX.csv em que XX é o número da opção.
"""
import os


def escreverFicheiro(info, num):
    file = open(f'TesteL3a_{num}.csv', "a", encoding='utf-8')
    file.write(f'{info}\n')
    file.close()


def lerFicheiro():
    info = []
    file = open("salarios.csv", encoding='utf-8')
    for num, line in enumerate(file, 1):
        info.append(line.rstrip().split(','))
    file.close()
    return info


def run10():
    salarios = lerFicheiro()

    for sal in salarios:
        print(sal)

    if input(f'Deseja guardar esta tabela num ficheiro? s/n') == 's':
        for sal in salarios:
            escreverFicheiro(sal, 10)
        print(f'Tabela guardada com sucesso!')

    input("Press Enter to continue...")
    os.system("clear")


def run11():
    idx = 0
    salarios = lerFicheiro()
    for sal in salarios:
        idx = sal[0]

    nomeColab = str(input("Nome do Colaborador: "))
    codPostal = str(input("Codigo Postal: "))
    salBruto = str(input("Salario Bruto: "))
    degSocial = str(input("Deg Social: "))
    seguro = str(input("Seguro: "))
    ilhas = str(input("Ilhas: "))
    print(f'Colaborador adicionado com sucesso.')

    fileW = open("salarios.csv", "a", encoding='utf-8')
    fileW.write(f'\n{int(idx) + 1},{nomeColab},{codPostal},{salBruto},{degSocial},{seguro},"{ilhas}"')

    input("Press Enter to continue...")
    os.system("clear")


def run12():
    idx = 0
    salarios = lerFicheiro()

    fileR = open("salarios.csv", "r")
    linhas = fileR.readlines()
    for sal in salarios:
        print(sal)

    while True:
        for sal in salarios:
            idx = sal[0]
            
        while True:
            choice = int(input("Escolhe o ID para alterar: "))
            if choice < 0 or choice > int(idx):
                print(f'Escolhe um ID válido!')
            elif choice == 0:
                exit()
            else:
                break

        while True:
            print(f'1 - Nome  |  2 - Cod Postal  | 3 - Salario Bruto  | 4 - Deg Social  |  5 - Seguro | 6 - Ilhas')
            alterar = int(input("O que é que quer alterar?: "))
            if alterar < 1 or alterar > 6:
                print(f'Escolhe um ID válido!')
            else:
                break

        if alterar == 1:
            novoNome = str(input("Novo Nome: "))
            print(f'O Nome foi alterado com sucesso!')
            print(f'Nome Antigo:{salarios[choice][alterar]} | Nome Atual: {novoNome}')
            linhas[
                choice] = f'{choice}, "{novoNome}",{salarios[choice][2]},{salarios[choice][3]},{salarios[choice][4]},{salarios[choice][5]}\n'

        elif alterar == 2:
            novoCodPostal = str(input("Novo Cod Postal: "))
            print(f'O Cod Postal foi alterado com sucesso!')
            print(f'Cod Postal Antigo:{salarios[choice][alterar]} | Cod Postal Atual: {novoCodPostal}')
            linhas[
                choice] = f'{choice},{salarios[choice][1]}, "{novoCodPostal}",{salarios[choice][3]},{salarios[choice][4]},{salarios[choice][5]}\n'
        elif alterar == 3:
            novoSalario = str(input("Novo Salario: "))
            print(f'O Salario foi alterado com sucesso!')
            print(f'Salario Antigo:{salarios[choice][alterar]} | Salario Atual: {novoSalario}')
            linhas[
                choice] = f'{choice},{salarios[choice][1]},{salarios[choice][2]}, {novoSalario},{salarios[choice][4]},{salarios[choice][5]}\n'
        elif alterar == 4:
            novoDeg = str(input("Novo Deg Social: "))
            print(f'O Deg Social foi alterado com sucesso!')
            print(f'Deg Social Antigo:{salarios[choice][alterar]} | Deg Social Atual: {novoDeg}')
            linhas[
                choice] = f'{choice},{salarios[choice][1]},{salarios[choice][2]},{salarios[choice][3]}, {novoDeg},{salarios[choice][5]}\n'
        elif alterar == 5:
            novoSeguro = str(input("Novo Seguro: "))
            print(f'O Seguro foi alterado com sucesso!')
            print(f'Seguro Antigo:{salarios[choice][alterar]} | Seguro Atual: {novoSeguro}')
            linhas[
                choice] = f'{choice},{salarios[choice][1]},{salarios[choice][2]},{salarios[choice][3]},{salarios[choice][4]}, {novoSeguro}\n'
        elif alterar == 6:
            novasIlhas = str(input("Novas Ilhas: "))
            print(f'As Ilhas foram alteradas com sucesso!')
            print(f'Minimo Antigo:{salarios[choice][alterar]} | Minimo Atual: {novasIlhas}')
            linhas[
                choice] = f'{choice},{salarios[choice][1]},{salarios[choice][2]},{salarios[choice][3]},{salarios[choice][4]}, {novasIlhas}\n'
        else:
            print(f'Algum erro aconteceu!')

        fileW = open("salarios.csv", "w")
        fileW.writelines(linhas)
        fileW.close()

    input("Press Enter to continue...")
    os.system("clear")


def run13():
    print('run13')
    # ...
    # ...
    input("Press Enter to continue...")


def run14():
    print('run14')
    # ...
    # ...
    input("Press Enter to continue...")


def run15():
    print('run15')
    # ...
    # ...
    input("Press Enter to continue...")


def run16():
    print('run16')
    # ...
    # ...
    input("Press Enter to continue...")


def run17():
    print('run17')
    # ...
    # ...
    input("Press Enter to continue...")


def run18():
    print('run18')
    # ...
    # ...
    input("Press Enter to continue...")


def run19():
    print('run19')
    # ...
    # ...
    input("Press Enter to continue...")


def run20():
    print('run20')
    # ...
    # ...
    input("Press Enter to continue...")


def run21():
    print('run21')
    # ...
    # ...
    input("Press Enter to continue...")


def run22():
    print('run22')
    # ...
    # ...
    input("Press Enter to continue...")


def run23():
    print('run23')
    # ...
    # ...
    input("Press Enter to continue...")


def run24():
    print('run24')
    # ...
    # ...
    input("Press Enter to continue...")


def main_menu():
    opcoes = {
        '0': 'print()',
        '10': 'run10()',
        '11': 'run11()',
        '12': 'run12()',
        '13': 'run13()',
        '14': 'run14()',
        '15': 'run15()',
        '16': 'run16()',
        '17': 'run17()',
        '18': 'run18()',
        '19': 'run19()',
        '20': 'run20()',
        '21': 'run21()',
        '22': 'run22()',
        '23': 'run23()',
        '24': 'run24()'
    }
    while True:
        os.system('clear')
        print(f'* * * *   M E N U   * * * *')
        print(f'10 - Mostrar/guardar tabelas de salários')
        print(f'11 - Inserir registo')
        print(f'12 - Modificar registo por ID')
        print(f'13 - Eliminar registo por ID')
        print(f'14 - Pesquisar por ID')
        print(f'15 - Pesquisar por nome')
        print(f'16 - Pesquisar por código postal')
        print(f'17 - Mostrar a tabela por ordem decrescente de salário bruto')
        print(f'18 - Mostrar/guardar regito(s) do colaborador com o salário bruto mais elevado')
        print(f'19 - Mostrar o total dos salários brutos')
        print(f'20 - Mostrar o total dos descontos para a segurança social')
        print(f'21 - Mostrar o total dos descontos para o seguro')
        print(f'22 - Mostrar os IDs e nomes dos colaboradores que trabalharam numa determinada ilha')
        print(f'23 - Mostrar quantos colaboradores há em cada código postal')
        print(f'24 - Listagem de registos personalizada')
        print(f'0 - Sair')
        print()
        while True:
            opcao = int(input('Insira uma opção válida: '))
            if opcao == 0 or 0 <= opcao <= 99:
                eval(opcoes.get(str(opcao)))
                break
        if opcao == 0:
            break


if __name__ == '__main__':
    main_menu()
