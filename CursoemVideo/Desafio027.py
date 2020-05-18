# 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip().title()
print(f'Primeiro nome: {nome.split()[0]}')
ultimo = len(nome.split())
print(f'Último nome: {nome.split()[ultimo-1]}')

# Você pode declar a entrada como outra incógnita e depois usar o split declarando uma nova incógnita (fica menor):
#n = str(input('Digite o seu nome completo: ')).strip().title()
#nome = n.split()
#print(f'Primeiro nome: {nome[0]}')
#print(f'Último nome: {nome[len(nome)-1]}')

