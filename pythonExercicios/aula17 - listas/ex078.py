'''Faça um programa que leia cinco valores numéricos e guarde-os em uma lista.
No final, mostre qual o maior e o menor valor digitado e as suas respectivas posições na lista.'''
maior = menor = 0

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        else:
            menor = lista[c]

print('-='*20)
print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}', end='')
print()
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}', end='')
print()
print('-='*20)