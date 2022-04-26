'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[], []]

for c in range(0, 7):
    n = (int(input(f'Digite o {c+1}º número: ')))

    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(lista)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'Todos os valores: {lista}')
print(f'Todos os valores pares: {lista[0]}')
print(f'Todos os valores ímpares: {lista[1]}')