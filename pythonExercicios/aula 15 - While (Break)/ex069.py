'''Crie um programa que leia a idade e o sexo de várias pessoas. Acada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a)quantas pessoas tem mais de 18 anos
b)quantos homens foram cadastrados
c)quantas mulheres tem menos de 20 anos'''
outdoor = 'CADASTRE UMA PESSOA'
print('-'*40)
print(f'{outdoor:^40}')
print('-'*40)

contIdade = contHomem = contMulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-' * 40)

#Verificação
    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F' and idade <= 20:
        contMulher += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'''Pessoas com idade acima de 18 anos: {contIdade}
Quantidade de homem(ns): {contHomem}
Quantidade de mulher(es) abaixo de 20 anos: {contMulher}''')
print('Programa finalizado')
