# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista DINHEIRO/CHEQUE: 10% de desconto; À VISTA NO CARTÃO: 5% de desconto; em até 2x no cartão: PREÇO NORMAL; 3x ou mais no cartão: 20% de juros;

from time import sleep
produto = float(input('\033[36mDigite o valor do produto: '))
print('SELECIONE A FORMA DE PAGAMENTO: \033[m\n[1] À VISTA (DINHEIRO/CHEQUE) \n[2] À VISTA (CARTÃO) \n[3] 2x no CARTÃO \n[4] 3x ou mais no CARTÃO')
forma = int(input(''))
print('\033[33m-=-'*10)
print('\033[36mPROCESSANDO...')
sleep(1)

if forma == 1:
    f1 = produto - produto * 0.10  # produto com desconto de 10%
    print(f'\033[36mVALOR TOTAL DO PRODUTO COM 10% DE DESCONTO: \033[32mR${f1:.2f}')
elif forma == 2:
    f2 = produto - produto * 0.05  # produto com desconto de 5%
    print(f'\033[36mVALOR TOTAL DO PRODUTO COM 5% DE DESCONTO: \033[32mR${f2:.2f}')
elif forma == 3:
    print(f'\033[36mVALOR TOTAL DO PRODUTO: \033[32mR${produto:.2f}')
    print(f'\033[36mCOM \033[33m2 \033[36mPARCELAS DE \033[32mR${(produto/2):.2f}')
elif forma == 4:
    t = int(input('Em quantas parcelas? '))
    f4 = produto + produto * 0.2 # Produto com 20% de juros
    parcelas = f4/t
    print(f'\033[36mVALOR TOTAL DO PRODUTO COM 20% JUROS: \033[32mR${f4:.2f}')
    print(f'\033[36mCOM \033[32m{t} \033[36mPARCELAS de \033[32mR${parcelas}')
else:
    print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
