'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''

num = int(input('Digite um número para saber o seu fatorial: '))
n = num
x = n

while n != 1:
    x = x * (n - 1)
    n -= 1
print('{}! = {}'.format(num, x))
