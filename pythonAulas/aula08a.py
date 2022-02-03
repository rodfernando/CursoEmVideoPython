# import math
from math import sqrt, floor
# A partir deste tipo de import, o método já é trazido para a classe sem a necessidade de referenciar.

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {}.'.format(num, floor(raiz))) # math.ceil arredonda para cima --- floor arredonda para baixo
