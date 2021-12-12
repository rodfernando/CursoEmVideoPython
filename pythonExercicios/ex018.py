import math

angulo = float(input('Digite um ângulo: '))

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print('Os valores de seno e cosseno do ângulo de {}º são:\n'
      'sen = {:.2f}\n'
      'cos = {:.2f}\n'
      'tan = {:.2f}'.format(angulo, sen, cos, tan))