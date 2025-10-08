from math import*
print ('Forneça os coeficientes da equação: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a!= 0:
    if b**2 - 4*a*c >= 0:
        x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
        print ('raizes da equação:', x1, 'e', x2)
    else:
        print ('A equação não tem raizes reais')