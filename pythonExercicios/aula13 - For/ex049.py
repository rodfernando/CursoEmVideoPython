# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, utilizando o laço for

n = int(input('Digite um número para ver a tabuada: '))

print('-' * 12)
c = 1
for i in range(1, 11):
    resultado = n * c
    print('{} x {:2} = {}'.format(n, c, resultado))
    c += 1
print('-' * 12)
