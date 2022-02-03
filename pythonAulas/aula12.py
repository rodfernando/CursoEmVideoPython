# Estrutura condicional aninhada simples
# Posso ter diversos elif, ou nenhum else.

nome = str(input('Qual o seu nome? '))
if nome == 'Rodrigo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Josefa':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana': # verificação em lista
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))