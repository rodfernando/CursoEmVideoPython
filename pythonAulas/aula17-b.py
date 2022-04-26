# teste = list()
# teste.append('Rodrigo')
# teste.append(32)
# galera = []
# galera.append(teste[:])
# print(galera)
# teste[0] = 'Gibimba'
# teste[1] = 12
# galera.append(teste[:])
# print(galera)

print('-='*30)

galera = [['João', 19], ['Maria', 32], ['Rodrigo', 10], ['Cesar', 89]]
print(galera[2][0])
print(galera[0][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-='*30)

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade e tem {p[1]}.')