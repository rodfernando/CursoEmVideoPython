nome = str(input('Digite seu nome completo: \n')).strip().upper()

print('A letra A aparece {} vezes'.format(nome.count('A')))
print('O primeiro "A" encontra-se na posição {}.'.format(nome.find('A') + 1))
print('O último "A" encontra-se na posição {}.'.format(nome.rfind('A') + 1))