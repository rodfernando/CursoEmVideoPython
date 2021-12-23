nome = str(input('Digite seu nome completo: ')).split()

primeiroNome = nome

print('Prazer em te conhecer, {}!'.format(nome))
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu segundo nome é {}.'.format(nome[len(nome)-1])) # eu quero que mostre o nome na posição do comprimento do nome - 1
