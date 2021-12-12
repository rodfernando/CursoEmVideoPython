salario = float(input('Digite o salário a ser aumentado: '))
aumento = salario + (salario * (5/100))
print('O salário era R${:.2f} reais e com 5% de aumento, foi para R${:.2f} reais.'.format(salario, aumento))