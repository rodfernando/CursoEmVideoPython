#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sará formado:
#-Equilátero: todos os lados iguais
#-Isóscelas: dois lados iguais
#-Escalano: todos os lados diferentes

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Temos um Triângulo')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não temos um Triângulo')