from CursoemVideo.Desafio115.lib.arquivo import *
from CursoemVideo.Desafio115.lib.interface import *
from time import sleep

arquivo = 'file.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    item = [' ', 'PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO MENU']
    escolha_usuario = menu(item)
    if escolha_usuario == 1:
        cabeçalho(item[1])
        lerArquivo(arquivo)
    elif escolha_usuario == 2:
        cabeçalho(item[2])
        nome = str(input('NOME: ')).upper().strip()
        idade = leiaInt('IDADE: ')
        cadastrar(arquivo, nome, idade)
    elif escolha_usuario == 3:
        cabeçalho('SAINDO DO SISTEMA...')
        break
    else:
        print('\033[31mOPÇÃO INVÁLIDA! DIGITE NOVAMENTE. \033[m')
    sleep(2)
