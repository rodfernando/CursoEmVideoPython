import random

# Rodrigo = 1
# José = 2
# Maria = 3
# João = 4
#
# sorteio = random.randint(1,4)
#
# print('O sorteado(a) foi {}!'.format(sorteio))

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}!'.format(escolhido))