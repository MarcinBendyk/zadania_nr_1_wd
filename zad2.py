import random
import math
import sys
from typing import List

#lista = [random.randint(1, 100) for x in range(10)]
#lista2 = [x for x in lista if x % 2 == 0]
#print(lista)
#print(lista2)

#lista = {'maslo':'g','woda':'l','szynka':'kg'}
#lista2 = {k for (k, v) in lista.items() if v == 'g'}
#print(lista2)

#def check (a,b,c):
#    if a**2+b**2==c**2:
#        return 'jest '
#    else:
#        return 'nie jest'
#print(check(1,2,3))

#def pt(a = 2,b = 4,h = 2):
#   return ((a+b)*h)/2
#print (pt())

#def function(a,b,c):
#    lista = [a * b * i for i in range(c)]
#    return lista
#print(function(5,5,5))


liczba = int(input('\n'))

try:
        sqrt_liczba = math.sqrt(liczba)
except Exception:
        print('Liczba ujemna!!!')
else:
        print(sqrt_liczba)