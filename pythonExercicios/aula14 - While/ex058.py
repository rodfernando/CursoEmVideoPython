'''Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

import random
from time import sleep

cont = 0
numeroDaSorte = int(input('Digite um valor entre 0 e 10: '))
numeroSorteio = random.randint(0, 10)
print('PROCESSANDO...')
sleep(1)

while numeroDaSorte != numeroSorteio:
    print('O número sorteado é {}.'.format(numeroSorteio))
    print('Você não foi sorteado! =/')
    cont += 1
    numeroDaSorte = int(input('Digite um valor entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(1)
    numeroSorteio = random.randint(0, 10)
if numeroDaSorte == numeroSorteio:
    print('O número sorteado é {}.'.format(numeroSorteio))
    print('Parabéns! Você acertou!')
    cont += 1

print('Nº de tentativa(s): {} vezes.'.format(cont))
print('Programa finalizado com sucesso!')
