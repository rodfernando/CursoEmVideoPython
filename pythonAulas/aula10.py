# Exemplo de estruturas condicionais compostas (simples são as que tem somente if)

tempo = int(input('Quantos anos tem o seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# Exemplo de estruturas condicionais simplificada/ternária

tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

# Exemplo de média usando condição simplificada

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(media))
print('Aprovado' if media <= 6 else 'Reprovado')

