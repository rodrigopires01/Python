combustivel = [5000, 4000, 2000]
combustivel2d = [[3000, 1000, 1500], [2000, 3000, 500]]
combustivel3d = [[1000, 200, 500], [500, 1000, 130], [750, 300, 300], [400, 700, 120], [250, 400, 400], [300, 300, 200], [1000, 100, 300], [800, 1000, 50]]
grupos = ['Oriental', 'Central', 'Ocidental']
estacoes = ['Verão', 'Outono', 'Inverno', 'Primavera']

# 1 Dimensão
for grupo in grupos:
    print(f'{grupo} ', end='')
print()
for comb in combustivel:
    print(f'{comb}      ', end='')
print()

# 2 Dimensões
print(f'------------------------------------------------------------------------------------------------------------------------')
for grupo in grupos:
    print(f'{grupo} ', end='')
print()
for comb in combustivel2d[0]:
    print(f'{comb}      ', end='')
print()
for comb in combustivel2d[1]:
    print(f'{comb}      ', end='')
print()

# 3 Dimensões
print(f'------------------------------------------------------------------------------------------------------------------------')
for estacao in estacoes:
    print(f'           {estacao}             ', end='')
print()
print(f'Oriental Central Ocidental | Oriental Central Ocidental |  Oriental Central Ocidental  |   Oriental Central Ocidental  | ')
for comb in combustivel3d[0]:
    print(f'{comb}     ', end='')
print(f'|   ', end='')
for comb in combustivel3d[2]:
    print(f'{comb}      ', end='')
print(f'|   ', end='')
for comb in combustivel3d[4]:
    print(f'{comb}      ', end='')
print(f'|     ', end='')
for comb in combustivel3d[6]:
    print(f'{comb}      ', end='')
print()
for comb in combustivel3d[1]:
    print(f'{comb}     ', end='')
print(f'|   ', end='')
for comb in combustivel3d[3]:
    print(f'{comb}      ', end='')
print(f'|   ', end='')
for comb in combustivel3d[5]:
    print(f'{comb}      ', end='')
print(f'|     ', end='')
for comb in combustivel3d[7]:
    print(f'{comb}      ', end='')
print()
print(f'------------------------------------------------------------------------------------------------------------------------')

x = 0
total = 0
while x < len(combustivel3d):
    y = 0
    while y < len(combustivel3d[x]):
        total += combustivel3d[x][y]
        y += 1
    x += 1

print(f'Total de vendas: {total}')

x = 0
totalgasolina = 0
while x < len(combustivel3d):
    y = 0
    while y < len(combustivel3d[x]):
        totalgasolina += combustivel3d[x][y]
        y += 1
    x += 2

print(f'Total de vendas de gasolina: {totalgasolina}')

x = 1
totalgasoleo = 0
while x < len(combustivel3d):
    y = 0
    while y < len(combustivel3d[x]):
        totalgasoleo += combustivel3d[x][y]
        y += 1
    x += 2

print(f'Total de vendas de gasoleo: {totalgasoleo}')

x = 0
totaloriental = 0
while x < len(combustivel3d):
    totaloriental += combustivel3d[x][0]
    x += 1

print(f'Total de vendas no grupo oriental: {totaloriental}')

x = 0
totalcentral = 0
while x < len(combustivel3d):
    totalcentral += combustivel3d[x][1]
    x += 1

print(f'Total de vendas no grupo central: {totalcentral}')

x = 0
totalocidental = 0
while x < len(combustivel3d):
    totalocidental += combustivel3d[x][2]
    x += 1

print(f'Total de vendas no grupo ocidental: {totalocidental}')

x = 0
totalgasolinaoriental = 0
while x < len(combustivel3d):
    totalgasolinaoriental += combustivel3d[x][0]
    x += 2

print(f'Total de vendas de gasolina no grupo oriental: {totalgasolinaoriental}')

x = 0
totalgasolinacentral = 0
while x < len(combustivel3d):
    totalgasolinacentral += combustivel3d[x][1]
    x += 2

print(f'Total de vendas de gasolina no grupo central: {totalgasolinacentral}')

x = 0
totalgasolinaocidental = 0
while x < len(combustivel3d):
    totalgasolinaocidental += combustivel3d[x][2]
    x += 2

print(f'Total de vendas de gasolina no grupo central: {totalgasolinaocidental}')

x = 1
totalgasoleooriental = 0
while x < len(combustivel3d):
    totalgasoleooriental += combustivel3d[x][0]
    x += 2

print(f'Total de vendas de gasoleo no grupo oriental: {totalgasoleooriental}')

x = 1
totalgasoleocentral = 0
while x < len(combustivel3d):
    totalgasoleocentral += combustivel3d[x][1]
    x += 2

print(f'Total de vendas de gasoleo no grupo central: {totalgasoleocentral}')

x = 1
totalgasoleoocidental = 0
while x < len(combustivel3d):
    totalgasoleoocidental += combustivel3d[x][2]
    x += 2

print(f'Total de vendas de gasoleo no grupo central: {totalgasoleoocidental}')

print(f'------------------------------------------------------------------------------------------------------------------------')

if totalgasolina > totalgasoleo:
    print(f'Combustivel que vendeu mais foi a Gasolina com {totalgasolina} vendas.')
elif totalgasoleo > totalgasolina:
    print(f'Combustivel que vendeu mais foi o Gasoleo com {totalgasoleo} vendas.')
else:
    print(f'Ambos os combustiveis venderam o mesmo. Gasolina: {totalgasolina}, Gasoleo: {totalgasoleo}')

if totaloriental > totalcentral and totaloriental > totalocidental:
    print(f'O grupo que vendeu mais foi o grupo Oriental com {totaloriental} vendas.')
elif totalcentral > totaloriental and totalcentral > totalocidental:
    print(f'O grupo que vendeu mais foi o grupo Central com {totalcentral} vendas.')
else:
    print(f'O grupo que vendeu mais foi o grupo Ocidental com {totalocidental} vendas.')

if totalgasolinaoriental > totalgasolinacentral and totalgasolinaoriental > totalgasolinaocidental:
    print(f'O grupo que vendeu mais gasolina foi o grupo Oriental com {totalgasolinaoriental} vendas.')
elif totalgasolinacentral > totalgasolinaoriental and totalgasolinacentral > totalgasolinaocidental:
    print(f'O grupo que vendeu mais gasolina foi o grupo Central com {totalgasolinacentral} vendas.')
else:
    print(f'O grupo que vendeu mais gasolina foi o grupo Ocidental com {totalgasolinaocidental} vendas.')

if totalgasoleooriental > totalgasoleocentral and totalgasoleooriental > totalgasoleoocidental:
    print(f'O grupo que vendeu mais gasoleo foi o grupo Oriental com {totalgasoleooriental} vendas.')
elif totalgasoleocentral > totalgasoleooriental and totalgasoleocentral > totalgasoleoocidental:
    print(f'O grupo que vendeu mais gasoleo foi o grupo Central com {totalgasoleocentral} vendas.')
else:
    print(f'O grupo que vendeu mais gasoleo foi o grupo Ocidental com {totalgasoleoocidental} vendas.')
