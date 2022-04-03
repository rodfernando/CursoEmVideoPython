'''Faça um programa que jogue par ou ímpar com o computador. O jogo será
interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitoria = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total é de {total}.', end=' ')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você ganhou!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!!\nVocê venceu {vitoria} vez(es). ')
