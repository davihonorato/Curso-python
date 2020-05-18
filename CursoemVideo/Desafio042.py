# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILATERO: todos os lados iguais; ISÓSCELES: dois lados iguais; ESCALENO: todos os lados diferentes.

l1 = int(input('Digite o lado do primeiro triângulo: '))
l2 = int(input('Digite o lado do segundo triângulo: '))
l3 = int(input('Digite o lado do terceiro triângulo: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print(f'É POSSÍVEL FORMAR UM TRIÂNGULO', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('ISÓSCELES')
    else:  # Caso fosse colocado no elif, a condição poderia ficar dessa forma: elif l1 != l2 != l3 != l1
        print('ESCALENO')
else:
    print('NÃO É POSSÍVEL FORMAR O TRIÂNGULO')
