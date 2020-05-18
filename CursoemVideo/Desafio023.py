 # 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
 # (unidae, dezena, centena, milhar)

n = int(input('Digite um número inteiro (0 - 9999): '))
print(f'unidade: {n//1%10}')
print(f'dezena: {n//10%10}')
print(f'centena: {n//100%10}')
print(f'milhar: {n//1000}')


"""outra forma: 
n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('{} milhares.'.format(n2[1]))
print('{} centenas. '.format(n2[2]))
print('{} dezenas. '.format(n2[3]))
print('{} unidades.'.format(n2[4]))"""