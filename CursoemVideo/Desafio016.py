# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira. (math)
# Digita um número 6.67; esse número tem a parte inteira 6.

import math
n = float(input('Digite um número real: '))
print(f'O número digitado foi {n} e sua porção inteira é {math.trunc(n)}')

n = float(input('Digite um número real: '))
print(f'O número digitado é {n} e tem como parte inteira {int(n)}')

n = float(input('Digite um número real: '))
print(f'O número digitado foi {n} e sua porção inteira é {n:.0f}')

 # Três formas de resolver esse problema.
