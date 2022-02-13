#Crie um programa que leia duas notas de um aluno a calcule sua média, mostrando uma mensagem no final, da acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 € 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2
print('Média: {}'.format(media))
if media >= 7.0:
    print('APROVADO')
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')