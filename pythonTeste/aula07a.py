# Ordem de precedências
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

nome = input('Digite seu nome: ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizado

print('='*20)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 * n2
di = n1 * n2
r = n1 % n2
print('Os resultados da soma, multiplicação e divisão são respectivamente {}, {} e {:.2f}.'.format(s, m, d), end=' ') # O end serve para não quebrar a linha
print('A divisão real e moda são {} e {}.'.format(di,r))