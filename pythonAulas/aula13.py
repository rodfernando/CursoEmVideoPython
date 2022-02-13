# Estrutura de repetição (iteração)

# for c in range(1,10):

# for c in range(1,10):
# Laço de variável de controle
#     if moeda:
#         pega
#     anda
#     pega
# pega
# anda

for c in range(1, 6):
    print(c)
print('='*30)

for c in range(1, 6):
    print('Oi')
print('='*30)

for c in range(6, 0, -1):
    print(c)
print('=' * 30)

n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('='*30)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('Fim')
print('='*30)

for c in range(0, 3):
    n = int(input('Digite um número: '))
print('Fim')
print('='*30)

s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n
print('O somatório final é {}.'.format(s))
