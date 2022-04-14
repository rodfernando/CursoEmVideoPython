'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o maior e o menor valor que
estão na tupla'''

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram:')
for n in tupla:
    print(f'{n}', end=' ')

print(f'\nO maior valor dentro da tupla é {max(tupla)}')
print(f'O menor valor dentro da tupla é {min(tupla)}')
