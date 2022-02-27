# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos

pesoAnterior = 0
pesoMax = 0
pesoMin = 0
for i in range(0 ,5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i + 1)))
    if peso > pesoAnterior:
        pesoMax = peso
    elif peso < pesoAnterior:
        pesoMin = peso
    pesoAnterior = peso
print('O maior peso foi {}Kg.'.format(pesoMax))
print('O menor peso foi {}Kg.'.format(pesoMin))
