'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('='*40)
print('{:^40}'.format('BANCO DEV'))
print('='*40)

n = int(input('Que valor você quer sacar? R$'))

cedula50 = n // 50
moda50 = n // 1 % 50

cedula20 = moda50 // 20
moda20 = moda50 // 1 % 20

cedula10 = moda20 // 10
moda10 = moda20 // 1 % 10

cedula1 = moda10 // 1
moda1 = moda10 // 1 % 1

print(f'Total de {cedula50} cédula(s) de R$50,00')
print(f'Total de {cedula20} cédula(s) de R$20,00')
print(f'Total de {cedula10} cédula(s) de R$10,00')
print(f'Total de {cedula1} cédula(s) de R$1,00')
print('='*40)
print('Volte sempre ao Banco CEV. Tenha um bom dia!')
