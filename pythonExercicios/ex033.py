n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior.',format(n1))
    if n2 > n3:
        print('{} é o menor.'.format(n3))
    else:
        print('{} é o menor.'.format((n2)))
elif n2 > n1 and n2 > n3:
    print('{} é o maior.'.format(n2))
    if n1 > n3:
        print('{} é o menor.'.format(n3))
    else:
        print('{} é o menor.'.format(n1))
else:
    print('{} é o maior.'.format(n3))
    if n1 > n2:
        print('{} é o menor.'.format(n2))
    else:
        print('{} é o menor.'.format(n1))