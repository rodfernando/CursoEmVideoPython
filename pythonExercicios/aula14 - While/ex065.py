'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''

resposta = 'S'
maior = menor = soma = quant = 0

while resposta in 'Ss': #forma de dizer quais as strings que desejo; uma espécie do do-while
    n = int(input('Digite um número: '))
    quant += 1
    soma += n

    #Maior e menor
    if quant == 1: # A quantidade de número é 1, ou seja, ele tanto é o maior quanto o menor
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]

#Média
media = soma / quant
print('O maior número foi {} e o menor foi {}, a média foi {:.2f}.'.format(maior, menor, media))
