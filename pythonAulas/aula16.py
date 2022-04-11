lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) # Transforma a tupla em lista, adicionando []
print(lanche)

print('-' * 40)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(4))
print(c.index(8))
print(c.index(5, 1))

print('-' * 40)

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

