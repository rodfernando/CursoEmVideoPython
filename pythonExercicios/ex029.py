v = int(input('Digite a velocidade do carro: '))

if v > 80:
    print('MULTADO')
    multa = (v - 80) * 7
    print('Valor a pagar: \n'
          'R$ {:.2f}'.format(multa))
print('--FIM--')