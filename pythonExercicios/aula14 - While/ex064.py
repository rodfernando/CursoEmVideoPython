'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles.
(desconsiderar o flag(999), ele não vale como dado.'''

cont = -1
total = 0
n = 0
while n != 999:
    n = int(input('Digite um número a ser somado: '))
    cont += 1
    if n == 999:
        total -= 999
    total += n
print('=' * 50)
print('Números digitados: {}\nTotal da soma: {}'.format(cont, total))
print('=' * 50)
