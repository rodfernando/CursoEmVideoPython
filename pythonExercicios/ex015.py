k = float(input('Quantos kilometros o carro percorreu? '))
d = int(input('Quantos dias foram contratados? '))

# 60 reais a díaria
# 0,15 por km rodado

calc = (d * 60) + (k * 0.15)
print('-' * 20)
print('Total a pagar')
print('-' * 20)
print('Dias: {}\nKm: {}'.format(d, k))
print('-' * 20)
print('Diária(s): R${:.2f}\n'
      'Combustível: {:.2f} reais\n'
      'Total a pagar: {:.2f} reais'.format(d*60, k*0.15, calc))
print('-' * 20)