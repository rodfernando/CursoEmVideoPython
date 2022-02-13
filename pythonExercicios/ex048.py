# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que
# se encontram no intervalo entre 1 até 500

soma = 0 # acumulador
cont = 0 # contador de números
for c in range(1, 501, 2):
    print(c, end=' ') # end para colocar lado à lado
    if c % 3 == 0:
        soma += c
        cont += 1
print('\nA soma de todos os valores é {}'.format(soma))
print('A quantidade de números divisíveis por 3 foram {}.'.format(cont))
