'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os numa tupla.
No final, mostre:
A)Quantas vezes apareceu o valor 9
B)Em que posição foi digitado o número 3
C)Quais foram os números pares.'''

tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print('')
print('='*40)
print(f'Você digitou os valores {tupla}')
print(f'Quantidade(s) de nove: {tupla.count(9)}.')
print(f'O número 3 está na posição {tupla.index(3)+1}')
print(f'O(s) valore(s) pares foi(ram)>', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')


