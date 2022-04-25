'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado. Não vou adicionar!')
    else:
        lista.append(n)
        print('Valor adicionado com Sucesso...')

    resposta = str(input('Quer continuar? [S/N] ')).upper().split()[0]
    if resposta in 'N':
        break
print('-='*30)
print(f'Você adicionou os valores {lista}.')
