nome = str(input('Digite seu nome completo: '))

print('-' * 40)
# Maiúsculo
print(nome.upper())
print('-' * 40)

# Minúsculo
print(nome.lower())
print('-' * 40)

# Quant. sem espaço
nomeStrip = nome.strip() # o strip tira os espaços fora da letra.
print(len(nomeStrip) - nomeStrip.count(' ')) # nome sem os espaços
print('-' * 40)

# Quant. letras no primeiro nome
nomeDividido = nome.split()
primeiroNome = nomeDividido[0]
print('O primeiro nome é {} e tem {} letras.'.format(primeiroNome, len(primeiroNome)))