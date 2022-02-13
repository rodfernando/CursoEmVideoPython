# Faça um programa que mostre na tala uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até
# 0, com uma pausa de 1 segundo entre eles.

for c in range(10, 0 - 1, -1):
    print('{}...'.format(c))
print('Fogos estourando!!!')