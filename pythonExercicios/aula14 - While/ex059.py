'''Crie um programa que leia os valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = ''
while opção != 5:
    print('''Digite uma opção: 
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa''')
    opção = int(input(''))
    if opção == 1:
        print('Soma: {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('Multiplicação: {} * {} = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é o maior número.'.format(n1))
        else:
            print('{} é o maior número.'.format(n2))
    elif opção == 4:
        print('Informe novamente os números: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa!')
