# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

h = float(input('Qual é a altura (em metros)? '))
b = float(input('Qual é a largura (em metros)? '))
A = b*h
qt = A/2
print(f'Área da parede: {A}m²')
print(f'A quantidade de tinta que será necessária: {qt:.2f} litros ')