'''Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra;
b) Quantos produtos custam mais de R$1000,00;
c) Qual é o nome do produto mais barato.'''

outdoor = 'LOJA SUPER BARATÃO'
print('-'*40)
print(f'{outdoor:^40}')
print('-'*40)
total = totMil = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1

# Verificação
    total += preço
    if preço > 1000:
       totMil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    if resposta == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {totMil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}.')