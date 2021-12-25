# d = int(input('Digite quantos kilometros tem sua viagem: '))
#
# if d <= 200:
#     print('O preço da sua passagem é de R$ {:.2f}.'.format(d * 0.5))
# else:
#     print('O preço da sua passagem é de R$ {:.2f}.'.format(d * 0.45))

# Outra forma com operador ternário

d = int(input('Digite quantos kilometros tem sua viagem: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
print('O preço de sua passagem será de R${:.2f}.'.format(preço))