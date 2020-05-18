# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu
# aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a sua expressão: '))
pilha = list()
for c in exp:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(c)
            break
if len(pilha) == 0:
    print('A sua expressão está correta.')
else:
    print('A sua expressão está incorreta.')
