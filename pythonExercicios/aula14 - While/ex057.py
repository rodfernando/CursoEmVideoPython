'''Faça um programa que leia o sexo das pessoas, mas que só aceite os valores de 'M' ou 'F'. Caso esteja errado
peça o valor novamente até ter o correto'''

n = 1
masc = fem = 0
sexo = ''
while n != 'S':
    while sexo != 'M' or sexo != 'F':
        sexo = str(input('Digite um sexo: [M/F]: '))
        if sexo != 'M' or sexo != 'F':
            sexo = str(input('Você digitou uma opção inválida. Digite novamente um sexo: [M/F]: '))
        if sexo == 'M':
            masc += 1
        else:
            fem += 1
    n = str(input('Deseja encerrar a execução? [S/N]')).upper()
print('Temos {} homem(ns) e {} mulher(es)'.format(masc, fem))

