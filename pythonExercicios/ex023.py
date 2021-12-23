numero = int(input('Digite um número de 0 à 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o número {}, temos\n'
      'Unidade = {}\n'
      'Dezena = {}\n'
      'Centena = {}\n'
      'Milhar = {}'.format(numero, u, d, c, m))



