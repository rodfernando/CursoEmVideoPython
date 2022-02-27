'''Faça um programa que leia o sexo das pessoas, mas que só aceite os valores de 'M' ou 'F'. Caso esteja errado
peça o valor novamente até ter o correto'''

sexo = str(input('Digite um sexo: [M/F]: ')).strip().upper()[0] # Validações para tirar espaço e aumentar a letra pegando somente a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Você digitou uma opção inválida. Digite novamente um sexo: [M/F]: ')).strip().upper()[0]
print('O sexo {} foi cadastrado com sucesso!'.format(sexo))
