'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores impares e os valores pares digitados, respectivamente.
Ao final, mostre o conteúdo das 3 listas geradas'''
lista = []
listaPar = []
listaImpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    if resposta in 'N':
        break
listaCopiada = lista[:]
for c in listaCopiada:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)
print('-='*30)
print(f'Lista geral: {lista}')
print(f'Lista par: {listaPar}')
print(f'Lista impar: {listaImpar}')
