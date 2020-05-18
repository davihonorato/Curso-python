# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

t = int(input('Digite uma distância (em metros): '))

print(f'Em quilômetros: {t/1000}km ')
print(f'Em hectômetros: {t/100}hm ')
print(f'Em decâmetros: {t/10}dam ')
print(f'Em decímetros: {t*10}dm ')
print(f'Em centímetros: {t*100}cm ')
print(f'Em milímetros: {t*1000}mm ')