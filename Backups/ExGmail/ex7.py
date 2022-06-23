# Escreva um programa em Python que lê o número de horas, que um em-
# pregado trabalhou numa dada semana e o seu salário/hora e calcula o
# ordenado semanal tendo em conta as horas extraordinárias. O salário é
# calculado do seguinte modo: se o número de horas fôr menor que 40 então
# salário é dado pelo produto do número de horas pelo salário hora, em caso
# contrário recebe horas extraordinárias as quais são pagas a dobrar.

if __name__ == '__main__':

    total = 0
    horas_extra = 0
    n1 = int(input("Número de horas trabalhadas: "))
    n2 = int(input("Salário por hora: "))

    if n1 < 40:
        total = n1 * n2
    else:
        horas_extra = n1 - 40
        total = (n1 * n2) + (horas_extra * (n2*2))

    print(f'Seu salário é: {total}')
