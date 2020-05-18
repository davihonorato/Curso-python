# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. (olhar os modulos)

import math
angulo = int(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'SENO: {seno:.2f} \nCOSSENO: {cosseno:.2f} \nTANGENTE: {tangente:.2f} ')