def notas(*n, situação=False):
    """
    --> Função para analisar notas e a situação de vários alunos de uma turma.
    :param n: notas dos alunos (aceita várias)
    :param situação: situação da média da turma (opcional)
    :return: um dicionário com a várias informações da turma.
    """
    dados = {'total': 0, 'maior': 0, 'menor': 0, 'media': 0}
    for c in n:
        dados['total'] += 1
        if dados['total'] == 1:  # PRIMEIRA NOTA
            dados['maior'] = c
            dados['menor'] = c
            dados['media'] = c
        else:
            if c > dados['maior']:
                dados['maior'] = c
            elif c < dados['menor']:
                dados['menor'] = c
            dados['media'] += c

    dados['media'] = dados['media']/dados['total']  # MEDIA TOTAL (SOMA DAS NOTAS DIVIDO PELA QUANTIDADE DE NOTAS)
    if situação:
        dados['situação'] = ''
        if dados['media'] > 7:
            dados['situação'] = 'BOA'
        elif 6 <= dados['media'] <= 7:
            dados['situação'] = 'RASOAVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


print(notas(5.5, 2.5, 1.5))

''' FORMA MAIS FÁCIL E RÁPIDA UTILIZANDO PROPRIEDADES DE DICIONÁRIOS.
dados['total'] = len(n)
dados['maior'] = max(n)
dados['menor'] = min(n)
dados['media'] = sum(n)/len(n)'''
