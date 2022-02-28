'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar  0 termos'''

print('=' * 30)
print('     N TERMOS DE UMA PA')
print('=' * 30)

a1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja mostrar?  '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
