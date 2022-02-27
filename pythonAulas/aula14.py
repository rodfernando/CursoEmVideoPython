# Estrutura de repetição com teste lógico

'''for i in range(1,10):
    print(i)
print('fim')'''

'''i = 1
while i < 10:
    print(i)
    i += 1
print('fim')'''

#Obs: Sabendo o limite, podemos usar tanto o for como o while. Não sabendo o limite, usamos somente o while

# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('Você digitou zero!')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Deseja continuar? [S/N]')).upper()
# print('Finalizado!')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Temos {} número(s) pares e {} número(s) ímpares'.format(par, impar))


