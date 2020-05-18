# Crie um algorítimo que leia um número e mostre o seu dobro, o seu triplo e sua raíz quadrada.

a = int(input('Digite um número: '))
dobro = 2*a
triplo = 3*a
raiz = a**(1/2) # pow(a, (1/2))

print(f'Dobro: {dobro} \nTriplo: {triplo} \nRaiz: {raiz:.2f}')
