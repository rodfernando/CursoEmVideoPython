# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para haxadecimal

numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('A conversão do número {} para binário é {:2}'.format(numero, bin(numero)[2:])) # não quero os dois primeiros dígitos, ou seja, começo da posição 2 e vou até o final
elif opcao == 2:
    print('A conversão do número {} para octal é {}'.format(numero, oct(numero)[2:]))
else:
    print('A conversão do número {} para hexadecimal é {:2}'.format(numero, hex(numero)[2:]))