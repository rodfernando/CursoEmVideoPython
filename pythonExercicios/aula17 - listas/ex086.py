'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # adiciona-se 0 para não precisar usar o append neste exercício
#
# # for para alimentação da matriz
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = (int(input(f'Digite um número para a posição {[l, c]}: ')))
#     print()
# # for para formatação da matriz
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end=' ')
#     print()

matriz = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor na posição [{l}, {c}]: '))) # para o append, basta adicionar somente a linha em que deseja ser adicionada
    print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
