import random
from time import sleep

numeroSorteio = random.randint(0, 5)

numeroDaSorte = int(input('Digite um valor entre 0 e 5: '))

print('PROCESSANDO...')
sleep(3)

print('O número sorteado é {}.'.format(numeroSorteio))
if numeroDaSorte == numeroSorteio:
    print('Parabéns! Você acertou!')
else:
    print('Não foi dessa vez!')