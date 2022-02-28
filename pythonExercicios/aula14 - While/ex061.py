'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while.'''

print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)
a1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

termo = a1
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
