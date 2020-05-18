# Faça um programa que leia o comprimento do cateto adjacente e do cateto oposto de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa. (a² = b² + c²)

adjacente = float(input('CATETO ADJACENTE: '))
oposto = float(input('CATETO OPOSTO: '))

hipotenusa = (adjacente**2 + oposto**2)**(1/2)

print(f'HIPOTENUSA: {hipotenusa:.2f} ')

 # OU

from math import hypot
print(f'HIPOTENUSA: {hypot(adjacente, oposto):.2f}')