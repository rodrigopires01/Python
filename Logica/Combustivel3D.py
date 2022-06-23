from random import randint


if __name__ == '__main__':

    vendas = [
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ]

    somaGasolina = 0
    somaGasoleo = 0

    somaGasolinaOcidental = 0
    somaGasolinaCentral = 0
    somaGasolinaOriental = 0

    somaGasoleoOcidental = 0
    somaGasoleoCentral = 0
    somaGasoleoOriental = 0

    somaGasolinaHomem = 0
    somaGasolinaMulher = 0
    somaGasolinaCriancas = 0
    somaGasolinaOutros = 0

    somaGasoleoHomem = 0
    somaGasoleoMulher = 0
    somaGasoleoCriancas = 0
    somaGasoleoOutros = 0

    for x in range(0, 2):
        for y in range(0, 4):
            for z in range(0, 3):
                vendas[x][y][z] = randint(10, 99)
                if x == 0:
                    somaGasolina += vendas[x][y][z]
                if x == 1:
                    somaGasoleo += vendas[x][y][z]
                if x == 0 and z == 0:
                    somaGasolinaOcidental += vendas[x][y][z]
                if x == 0 and z == 1:
                    somaGasolinaCentral += vendas[x][y][z]
                if x == 0 and z == 2:
                    somaGasolinaOriental += vendas[x][y][z]
                if x == 1 and z == 0:
                    somaGasoleoOcidental += vendas[x][y][z]
                if x == 1 and z == 1:
                    somaGasoleoCentral += vendas[x][y][z]
                if x == 1 and z == 2:
                    somaGasoleoOriental += vendas[x][y][z]

    print(f'Total gasolina: {somaGasolina}')
    print(f'Total gasoleo: {somaGasoleo}')

    print(f'Total Gasolina Grupo Ocidental: {somaGasolinaOcidental}')
    print(f'Total Gasolina Grupo Central: {somaGasolinaCentral}')
    print(f'Total Gasolina Grupo Oriental: {somaGasolinaOriental}')

    print(f'Total Gasoleo Grupo Ocidental: {somaGasoleoOcidental}')
    print(f'Total Gasoleo Grupo Central: {somaGasoleoCentral}')
    print(f'Total Gasoleo Grupo Oriental: {somaGasoleoOriental}')

    print(f'Total Gasolina Homens: {somaGasolinaHomem}')
    print(f'Total Gasolina Mulheres: {somaGasolinaMulher}')
    print(f'Total Gasolina Crianças: {somaGasolinaCriancas}')
    print(f'Total Gasolina Outros: {somaGasolinaOutros}')

    print(f'Total Gasoleo Homens: {somaGasoleoHomem}')
    print(f'Total Gasoleo Mulheres: {somaGasoleoMulher}')
    print(f'Total Gasoleo Crianças: {somaGasoleoCriancas}')
    print(f'Total Gasoleo Outros: {somaGasoleoOutros}')

