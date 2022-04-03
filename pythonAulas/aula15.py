# n = s = 0
# while n != 999: # Dizemos que temos uma flag (ponto de parada)
#     n = int(input("Digite um número: "))
#     if n == 999:
#         break
#     s += n
# print("A soma dos valores foi {}".format(s))

# n = s = 0
# while True: # Ao invés de colocar uma flag, dizemos que é true e entra num loop infinito
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print(f'A soma dos valores foi {s:.2f}.')

nome = 'José'
idade = 22
salario = 985.20
print(f'{nome:=^20} tem {idade} e ganha R${salario:.2f}.')
print(f'{nome:=>20} tem {idade} e ganha R${salario:.2f}.')
print(f'{nome:=<20} tem {idade} e ganha R${salario:.2f}.')