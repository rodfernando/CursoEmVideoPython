'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela'''
lista = []

for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição: '))
    if c == 0 or n > lista[len(lista)-1]:# para pegar o último elemento ou "lista[-1]"
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]: #vai verificar se o valor que quero inserir é menor ou igual a ele
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os Valores digitados em ordem foram {lista}.')