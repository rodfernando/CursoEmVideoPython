'''Crie um programa que vai lre vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista'''
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if resposta in 'N':
        break
print('-='*30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores na ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 está contido na lista.')
else:
    print('O valor 5 não está contido na lista.')

