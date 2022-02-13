#Fazer um jogo de Jokenpô
import random

lista = ['pedra', 'papel', 'tesoura']
print('JOKENPÔ')
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
eu = int(input('Digite um número: '))
pc = random.randint(0, 2)

print('x' * 30)
print('O jogador escolheu {}.'.format(lista[eu]))
print('O computador escolheu {}.'.format(lista[pc])) # Dentro da lista, quero a posição que o pc escolheu
print('x' * 30)

# Pedra
if eu == 0 and pc == 1:
    print('Perdi!!!')
elif eu == 0 and pc == 2:
    print('Ganhei!!!')
elif eu == 0 and pc == 0:
    print('Empatou!!!')

# Papel
if eu == 1 and pc == 0:
    print('Ganhei!!!')
elif eu == 1 and pc == 2:
    print('Perdi!!!')
elif eu == 1 and pc == 1:
    print('Empatou!!!')

# Tesoura
if eu == 2 and pc == 0:
    print('Perdi!!!')
elif eu == 2 and pc == 1:
    print('Ganhei!!!')
elif eu == 2 and pc == 2:
    print('Empatou!!!')