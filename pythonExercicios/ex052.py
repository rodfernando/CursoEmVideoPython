# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Um número primo é divisível por 1 e por ele mesmo

n = int(input('Digite um número: '))
cont = 0
for i in range(1, n + 1, 1):
    if n % i == 0:
        cont += 1
        print('{}  '.format(i), end='→ ')
if cont == 2:
    print('Este número é primo')
else:
    print('Este número tem {} divisores, portanto não é primo.'.format(cont))
