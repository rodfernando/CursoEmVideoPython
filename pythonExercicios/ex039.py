from datetime import datetime

# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:
# - se ele ainda vai se alistar ao serviço militar;
# - se é a hora de se alistar;
# - se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


dataDeHoje = datetime.today().year # Método para chamar o ano
anoNascimento = int(input('Digite o ano de nascimento: '))
idade = dataDeHoje - anoNascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(anoNascimento, idade, dataDeHoje))

if idade == 18:
    print('Chegou a hora de se alistar, jovem!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda tem {} anos. Falta(m) {} ano(s) para o alistamento militar.'.format(idade, saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} ano(s).'.format(saldo))
