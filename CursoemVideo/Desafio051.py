# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d = a + (10 - 1) * r  # Utiliza-se essa fórmula (matemática) para encontrar até o décimo termo. Se quisermos achar até o vigésimo, basta trocar o '10' pelo '20'

for c in range(a, d + r, r):  # soma-se d+r para poder encontrar o último número da PA, visto que o python não mostra o exatamente o décimo (d)
    print(c)
print('FIM')
