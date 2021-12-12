a = input('Digite algo: ')
print('O valor primitivo deste dado é ', type(a))
print('Só tem espaços? ', a.isspace())
# print('É um número? ', a.isnumeric())
print('É um número? {}'.format(a.isnumeric()))
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower())
print('Está capitalizada? ', a.istitle())


