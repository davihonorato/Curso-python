# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
# lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0 or valor > valores[len(valores)-1]:  # Essa fórmula é para pegar o ultimo da lista. pode-se utilizar apenas lista[-1]
        valores.append(valor)
        print('Valor adicionado ao final da lista.')
    else:
        for pos, x in enumerate(valores):
            if valor <= x:
                valores.insert(pos, valor)
                print(f'Valor adicionado na posição {pos}')
                break
print(valores)
