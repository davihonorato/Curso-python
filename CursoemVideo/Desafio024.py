# 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

#cidade = str(input('Digite o nome de uma cidade: ')).strip()
#print('Começa com santo: ', 'SANTO' in cidade.upper())

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == "SANTO")