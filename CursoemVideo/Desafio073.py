# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
# Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em
# ordem alfabética. d) Em que posição está o time da Chapecoense.
c = 0
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico-PR', 'Sao Paulo', 'Internacional', 'Corinthians',
          'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atletico-MG', 'Fluminense', 'Botafogo', 'Ceará SC',
          'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('- - - PRIMEIRO COLOCADOS - - - ')
for c in range(0, 5):  # Cinco primeiro colocados
    print(f'[{c+1}] {tabela[c]}')
print('- - - ÚLTIMOS COLOCADOS - - - ')
for c in range(16, 20):  # Quatro últimos colocados
    print(f'[{c+1}] {tabela[c]}')
print('- - - ORDEM ALFABÉTICA - - - ')
print(sorted(tabela))  # Ordem alfabética
print('- - - COLOCAÇÃO DA CHAPECOENSE - - - ')
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª colocação')