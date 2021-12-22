nome = str(input('Digite seu nome completo: '))

print('-' * 20)
# Maiúsculo
print(nome.upper())
print('-' * 20)

# Minúsculo
print(nome.lower())
print('-' * 20)

# Quant. sem espaço
nomeStrip = nome.strip() # o strip tira os espaços fora da letra.
print(len(nomeStrip) - nomeStrip.count(' ')) # nome sem os espaços
print('-' * 20)

# Quant. letras no primeiro nome
nomeDividido = nome.split()
primeiroNome = nomeDividido[0]
print('O primeiro nome é {}'.format(primeiroNome))