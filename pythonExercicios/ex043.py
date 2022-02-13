#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
#status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Paso
# - Entre 18.5 a 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('digite sua altura (metros): '))

imc = peso / (altura**2)
print('Seu imc é {:1f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25.0:
    print('Peso ideal')
elif 25.0 <= imc < 30.0:
    print('Sobrepeso')
elif 30.0 <= imc < 40.0:
    print('Obesidade')
else:
    print('Obesidade mórbida')