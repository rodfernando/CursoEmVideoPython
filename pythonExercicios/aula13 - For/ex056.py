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
for i in range(1, 6):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa (M/F): '.format(i)))
    somatorioIdade += idade
    if idade > idadeAnterior and (sexo == 'M' or sexo == 'm'):
        idadeMax = idade
        nomeVelho = nome
    if idade < 20 and (sexo == 'F' or sexo == 'f'):
        contMulher += 1
    idadeAnterior = idade
    print('-' * 40)

print('-' * 40)
# média de idade do grupo:
media = float(somatorioIdade / i)
print('A média de idade das pessoas é {:.1f} anos'.format(media))

# nome do mais velho
print('O nome do homem mais velho é {}, com {} anos'.format(nomeVelho, idadeMax))

# Quantas mulheres têm menos de 20 anos
print('Temos {} mulher(es) com menos de 20 anos'.format(contMulher))

print('-' * 40)