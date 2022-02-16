# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos.

idadeMax = 0
idadeMin = 0
idadeAnterior = 0
somatorioIdade = 0
nomeVelho = ''
contMulher = 0
for i in range(0, 2):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i + 1)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i + 1)))
    sexo = str(input('Digite o sexo da {}ª pessoa (M/F): '.format(i + 1)))
    somatorioIdade += idade
    if idade > idadeAnterior and sexo == 'M' or sexo == 'm':
        idadeMax = idade
        nomeVelho = nome
    elif idade < 20 and sexo == 'F' or sexo == 'f':
        contMulher += 1
    idadeAnterior = idade

# média de idade do grupo:
media = float(somatorioIdade / i)
print('A média de idade das pessoas é {:.1f}Kg'.format(media))

# nome do mais velho
print('O nome do mais velho é {}.'.format(nomeVelho))

# Quantas mulheres têm menos de 20 anos
print('Temos {} mulher(es) com menos de 20 anos'.format(contMulher))
