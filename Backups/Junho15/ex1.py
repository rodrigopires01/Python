nome = 'Rodrigo Teles Pires'
nomeInv = ''

if __name__ == '__main__':
    for x in range(1, len(nome)-1 * -1):
        nomeInv += nome[-x]

print(nomeInv)
