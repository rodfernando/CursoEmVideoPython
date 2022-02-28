'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência de Fibonacci
fórmula -> Fn = Fn-1 + Fn-2'''

termo = int(input('Digite a quantidade de termos: '))
f1 = 0
f2 = 1
fn = 1
cont = 1
while cont <= termo:
    print('{}'.format(fn), end='')
    print(' → ' if cont <= 10 else ' ', end='')
    fn = f2 + f1
    f1 = f2
    f2 = fn
    cont += 1
print('FIM')
