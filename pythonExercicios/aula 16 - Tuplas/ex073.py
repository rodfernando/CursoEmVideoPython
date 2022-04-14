'''Crie uma tupla preenchida com os primeiros 20 colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre;
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 calocados da tabela.
C) Uma lista de times em ordem alfabética.
D) Em que posição na tabela está o time da Santos'''

tabela = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético-MG', 'Ceará', 'Avaí', 'Cuiabá', 'Flamengo', 'Bragantino',
          'Atlético-GO', 'Juventude', 'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 'America-MG',
          'Botafogo', 'Internacional', 'Goiás', 'Athletico-PR')

print('x'*40)
print('{:^40}'.format('TABELA DO BRASILEIRÃO'))
print('x'*40)

print('G5')
print('='*40)

for i in range(0, 5):
    print(f'{i+1}º - {tabela[i]}')
print('='*40)

for i in range(16, 20):
    print(f'{i + 1}º - {tabela[i]}')
print('='*40)


listaOrdenada = sorted(tabela)
print(listaOrdenada)
print('='*40)

print(f'O Santos está na {tabela.index("Santos")}ª posição.')




# print(f'O time do Santos está na {} posição.')