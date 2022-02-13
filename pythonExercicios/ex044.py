# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
# de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão:preço normal
# - 3x ou mais no cartão:20% de juros

preço = float(input('Digite o preço do produto: '))
print('''Escolha a forma de pagamento:
[ 1 ] À vista
[ 2 ] Dividido''')
pagamento = int(input('Sua opção: '))

if pagamento == 1:
    print('''Escolha o tipo de pagamento 
    [ 1 ] Dinheiro
    [ 2 ] Cheque
    [ 3 ] Cartão''')
    opção = int(input('Sua opção: '))
    if opção == 1 or opção == 2:
        valorFinal = preço * 0.9
        print('Você ganhou 10% de desconto')
        print('Valor final: R${:.2f}'.format(valorFinal))
    elif opção == 3:
        valorFinal = preço * 0.95
        print('Você ganhou 5% de desconto')
        print('Valor final: R${:.2f}'.format(valorFinal))
else:
    print('''Escolha a quantidade de parcelas:    
        [ 1 ] 2x
        [ 2 ] 3x ou mais''')
    opção = int(input('Sua opção: '))
    if opção == 1:
        valorFinal = preço
        valorDividido = preço / 2
        print('Preço com valor normal')
        print('Valor final: R${:.2f} em duas parcelas de R${:.2f}.'.format(valorFinal, valorFinal))
    else:
        parcelas = int(input('Digite a quantidade de parcelas: '))
        valorFinal = preço * 1.2
        valorDividido = valorFinal / parcelas
        print('Valor com 20% de juros')
        print('Valor final: R${:.2f} em {} parcelas de R${:.2f}.'.format(valorFinal, parcelas, valorDividido))
