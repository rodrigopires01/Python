def ordenar(island, order):
    a = 0

    while a < len(island[0]):
        b = a + 1
        while b < len(island[0]):
            if island[1][a] * order > island[1][b] * order:
                temp = island[1][a]
                temp1 = island[0][a]
                island[1][a] = island[1][b]
                island[0][a] = island[0][b]
                island[1][b] = temp
                island[0][b] = temp1
            b += 1
        a += 1

    if order == -1:
        for sales in island:
            print(f'Ordem Decrescente: {sales}')
    elif order == 1:
        for sales in island:
            print(f'Ordem Crescente: {sales}')
    else:
        print(f'Erro!')


if __name__ == '__main__':

    ilhas = [["São Jorge", "Terceira", "Graciosa", "Pico", "Faial"], []]

    for ilha in ilhas[0]:
        ilhas[1].append(int(input(f'Insere o número de vendas para a ilha {ilha}: ')))

    maior = ilhas[1][0]
    menor = ilhas[1][0]
    x, y, z, soma = 0, 0, 0, 0

    for vendas in ilhas[1]:
        soma = soma + vendas

        if vendas > maior:
            maior = vendas
            y = x

        if vendas < menor:
            menor = vendas
            z = x
        x += 1

    print(f'--------------------------------------------------------------------------')
    print(f'Maior venda: {ilhas[0][y]} com {maior} vendas')
    print(f'Menor venda: {ilhas[0][z]} com {menor} vendas')
    print(f'Média de vendas: {soma / 5}')
    print(f'--------------------------------------------------------------------------')

    for ilha in ilhas:
        print(f'Ordem Normal: {ilha}')

    print(f'--------------------------------------------------------------------------')
    ordenar(ilhas, 1)
    print(f'--------------------------------------------------------------------------')
    ordenar(ilhas, -1)
    print(f'--------------------------------------------------------------------------')

