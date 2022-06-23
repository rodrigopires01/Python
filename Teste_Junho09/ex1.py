# Ex1: programa que quando corre ele diz que se é a primeira vez que ja correste o programa, se não for diz quando foi a primeira vez que correu o programa.
import pickle
from datetime import datetime
from pathlib import Path


def guardar():
    hora = datetime.now()
    file = open("hora.dat", "wb")
    pickle.dump(hora, file)


if __name__ == '__main__':
    file = Path("hora.dat")
    if file.is_file():
        file = open("hora.dat", "rb")
        horas = pickle.load(file)
        print(f'Já tinha corrido este programa pela primeira vez em {horas}')
    else:
        print(f'Acabou de correr o programa pela primeira vez!')
        guardar()
