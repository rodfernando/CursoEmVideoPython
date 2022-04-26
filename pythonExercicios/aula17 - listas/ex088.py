'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep

lista_sorteio = []

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f' SORTEANDO {jogos} JOGOS ', '=-' * 3)
for i in range(0, jogos):
    for n in range(0, 6):
        numero_sorteado = randint(1, 60)
        # Verificação se já existe um número igual na lista
        if numero_sorteado in lista_sorteio:
            numero_sorteado = randint(1, 60)
            lista_sorteio.append(numero_sorteado)
        else:
            lista_sorteio.append(numero_sorteado)
    lista_sorteio.sort()
    print(f'Jogo {i + 1}: {lista_sorteio}')
    sleep(1)
    lista_sorteio.clear()
print('-=' * 5, f'< BOA SORTE >', '=-' * 5)
