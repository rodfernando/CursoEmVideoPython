# Desenvolva um programa que leia o Primeiro termo e a Razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão

print('=' * 30)
print('     10 TERMOS DE UMA PA')
print('=' * 30)
a1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

# décimo termo de uma pa
décimo = a1 + ((10-1) * razão)

for i in range(a1, décimo + razão, razão):
    print('{}  '.format(i), end='→ ') # alt + 26 = →
print('Acabou')
