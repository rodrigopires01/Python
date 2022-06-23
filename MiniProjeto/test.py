produtos = []
produtosAt = []

fileR = open("teste.csv", "r")
for num, line in enumerate(fileR, 1):
    produtos.append(line.rstrip().split(','))

for prod in produtos:
    print(prod)
    idx = prod[0]


while True:
    choice = int(input("Escolhe o ID para apagar: "))
    if choice < 0 or choice > int(idx):
        print(f'Escolhe um ID válido!')
    else:
        break


fileR = open("teste.csv", "r")
for row in fileR:
    if str(row[0]) == str(choice):
        print(f'{row[0]} foi apagado com sucesso!')
    else:
        produtosAt.append(row)

fileW = open("teste.csv", "w")
for prod in produtosAt:
    fileW.write(prod)
