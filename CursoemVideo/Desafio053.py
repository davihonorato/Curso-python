# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase qualquer: ')).upper().replace(' ', '')
letras = len(frase)  # Para saber a quantidade de letras na frase
inverso = ''
for c in range(letras, 0, -1):
    inverso += frase[c-1]  # Tiraremos 1 de c pq sempre a primeira letra é zero. tendo 4 letras: 0, 1, 2, 3. A quarta letra é 3 e não 4;
print(f'A frase ao contrário: {inverso}')
if inverso == frase:
    print('ESSA FRASE É UM PALINDROMO.')
else:
    print('ESSA FRASE NÃO É UM PALINDROMO.')
