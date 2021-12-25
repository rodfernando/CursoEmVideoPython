salario = float(input('Digite o salário: R$ '))

if salario > 1250:
    print('Seu salário de R$ {:.2f} foi aumentado para R$ {:.2f}'.format(salario, salario * 1.1))
else:
    print('Seu salário de R$ {:.2f} foi aumentado para R$ {:.2f}'.format(salario, salario * 1.15))
print('--FIM--')
