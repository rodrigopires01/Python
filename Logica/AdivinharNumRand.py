import os
import pickle
from random import randrange
from pathlib import Path


def relatorio(mostrar=False):
    if mostrar:
        print(f'Numero Sorteado: {rand}')
    print(f'Tentativas: {tentativas}')
    print(f'Números Inseridos: {nums}')


def restaurar():
    file = Path("adivinha.dat")
    if file.is_file():
        with open("adivinha.dat", "rb") as infile:
            tentativas, nums, rand = pickle.load(infile)
    else:
        tentativas = 0
        nums = []
        rand = randrange(100) + 1
    return tentativas, nums, rand


def guardar(tentativas, nums, rand):
    with open("adivinha.dat", "wb") as output:
        pickle.dump([tentativas, nums, rand], output)


if __name__ == '__main__':
    tentativas, nums, rand = restaurar()

    while True:
        num = int(input('Numero: '))
        if num == 0:
            guardar(tentativas, nums, rand)
            relatorio()
            exit()
        if num > 100:
            tentativas += 1
            relatorio()
            continue
        if num in nums:
            print(f'Já tentaste este...')
            continue
        if num == rand:
            print(f'Acertaste no Nº')
            file = Path("adivinha.dat")
            if file.is_file():
                os.remove("adivinha.dat")
            break
        else:
            tentativas += 1
            nums.append(num)
            diff = abs(rand - num)
            if diff <= 10:
                print(f'Muito Quente!')
            elif 11 <= diff <= 20:
                print(f'Quente!')
            elif 21 <= diff <= 30:
                print(f'Frio!')
            elif 31 <= diff <= 40:
                print(f'Muito Frio!')
            elif diff <= 41:
                print(f'Gelado!')
            else:
                print(f'Congelado!')
    relatorio(True)
