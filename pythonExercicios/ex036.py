# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal.
# sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos será o pagamento? '))

prestacaoMensal = valorCasa / (anos * 12)
minimo = salario * 0.3

print('-=' * 40)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}.'.format(valorCasa, anos, prestacaoMensal), end='')
print('COMPARANDO --prestação mensal R${:.2f} --mínimo R${:.2f}'.format(prestacaoMensal, minimo))
print('-=' * 40)

if prestacaoMensal > minimo:
    print('Sua parcela é de R${:.2f}. Ela extrapolou o seu limite, que é de R${:.2f}.'.format(prestacaoMensal, minimo))
    print('Seu empréstimo bancário foi negado!')
else:
    print('Sua parcela é de R${:.2f}. Seu limite é de R${:.2f}.'.format(prestacaoMensal, minimo))
    print('Seu empréstimo bancário foi aceito!')
