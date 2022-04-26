num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0) # Inserir na posição 2 o número 0
# num.pop(3)
if 8 in num:
    num.remove(8)
else:
    print('Não achei o número 8.')
print(num)
print(f'Essa lista tem {len(num)} elementos.')


valores = list()
# valores.append(9)
# valores.append(5)
# valores.append(3)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
# for v in valores:
#     print(f'{v}...')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}.')

a = [2, 3, 4, 8]
b = a
#para copiar lista de a em b, deve-se fazer b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')