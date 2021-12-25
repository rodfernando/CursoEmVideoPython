# --Padrão ANSI--
# \033 [0(style);33(text);44(back) m
# Style: 0 -> none; 1 -> bold, 4 -> underline; 7 -> negative
# Text: cores de 30 - 37
# Back: cores de fundo de 40 - 47

print('\033[1;32;41mOlá Mundo!\033[m') # cort o final

#letra branca
print('\033[7;30mOlá Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[1;31m{}\033[m.'.format(a, b))

# nome = 'Fernando'
# print('Olá, {}{}{}'.format('\033[32m', nome,'\033[m'))

nome = 'Rodrigo'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m'}
print('Olá, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))