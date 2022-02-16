# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Ex: apos a sopa, a sacada da casa, a torre da derrota, o lobo ama bolo, anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #dividiu a frase para gerar uma lista
juntarPalavras = ''.join(palavras) # juntou as palavras da lista com um espaço vazio numa String só
inverso = '' # uma variável vazia

# inverso = juntarPalavras[::-1] # uma forma de fazer sem utilizar o FOR

for letra in range(len(juntarPalavras) -1, -1, -1): # como é regressivo, a palavra acabará com -1, e não + 1. O intervalo não é 0, e sim -1. (Ao invés de ser do 0 ao 20, será do -19 ao -1.
    # print(juntarPalavras[letra])
    inverso += juntarPalavras[letra] # lembrar que letra é uma string aqui. Para contagem, temos que adicionar juntarPalavras[letras]

if juntarPalavras == inverso:
    print('Temos um palíndromo.')
    print('{} = {}'.format(juntarPalavras, inverso))
else:
    print('Não temos um palíndromo')
