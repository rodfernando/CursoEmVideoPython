'''Faça um programa que leia um número qualquer e mostre o seu fatorial'''

n = int(input('Digite um número para saber o seu fatorial: '))
x = n # variável para armazenar o valor inicial
f = 1 # pra deixar a multiplicação iniciando por 1
print('Calculando {}! = '.format(n), end='')
while x > 0:
    print('{}'.format(x), end='') # formatação
    print(' x ' if x > 1 else ' = ', end='') # formatação
    f *= x
    x -= 1
print(f)
