'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

boletim = []

while True:
    nome = str(input('Digite o nome do aluno(a): '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])

    resposta = str(input(('Deseja continuar? [S/N] '))).upper().split()[0]
    if resposta in 'Nn':
        break

print('-=' * 30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'* 30)
for i, a in enumerate(boletim):
    print(f'{i:<4}  {a[0]:<10} {a[2]:>8.1f}') # Para mostrar o dado, só seguir o exemplo

while True:
    print('-' * 30)
    nome_pesquisa = int(input('Deseja mostrar nota de que aluno? [999 para finalizar] '))
    if nome_pesquisa == 999:
        print('FINALIZANDO...')
        break
    if nome_pesquisa <= len(boletim) - 1:
        print(f'Notas de {boletim[nome_pesquisa][0]} são {boletim[nome_pesquisa][1]}.')
print('<<< VOLTE SEMPRE >>>')

