'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada (flag). No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando a flag)'''

n = s = cont = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram lido(s) {cont} números e a soma total foi de {s}.')
