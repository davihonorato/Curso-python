# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')

def leiaInt(msg):
    ok = False
    num = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if ok:
            break
    return num

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')