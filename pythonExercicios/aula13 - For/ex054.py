# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

contMenor = 0
contMaior = 0
for i in range(0, 7):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i + 1)))
    if idade < 18:
        contMenor += 1
    else:
        contMaior += 1
print('Temos {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade.'.format(contMaior, contMenor))

