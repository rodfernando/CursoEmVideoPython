'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre;
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves
Obs: 50 kg -> pessoa leve
100 kg -> pessoa pesada'''

listagem = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(listagem) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    listagem.append(dados[:])
    dados.clear()
    resposta = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if resposta in 'nN':
        break
print('-='*40)
print(f'{len(listagem)} pessoas foram analisadas.')
print(f'O maior peso foi de {maior}. Pessoa(s):', end='')
for p in listagem:
    if p[1] == maior:
        print(f' {p[0]}', end=' - ')
print(f'\nO menor peso foi de {menor}. Pessoa(s):', end='')
for p in listagem:
    if p[1] == menor:
        print(f' {p[0]}', end=' - ')


