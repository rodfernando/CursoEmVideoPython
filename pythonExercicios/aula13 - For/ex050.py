# Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for i in range(0, 6):
    n = int(input('Digite o {}º inteiro: '.format(i + 1)))
    if n % 2 == 0:
        soma += n
print('A soma total é de {}.'.format(soma))