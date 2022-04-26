'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[], [], []]
maior = menor = soma_terceira = soma = 0

# Alimentação da matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um número na posição [{l}, {c}]: ')))
        # Verificação números pares
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        # Verificação terceira coluna
        if c == 2:
            soma_terceira += matriz[l][2]
        # verificação maior número da 1ª linha
        if l == 1 and matriz[l][c] == '':
            maior = menor = matriz[l][c]
        else:
            if l == 1 and matriz[l][c] > maior:
                maior = matriz[l][c]

# Formatação da matriz
print('-='*30)
print('Matriz:')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*20)

#A)
print(f'A soma dos números pares foi {soma}.')
#B)
print(f'A soma dos números da terceira coluna foi {soma_terceira}.')
#C)
print(f'O maior valor da 1ª linha é {maior}.')
print('-='*20)
