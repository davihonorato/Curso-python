# COMO A CLASSE SUPER HERDA DA CLASSE FILHA.
# OBS: O CÓDIGO FICA COMPLEXO.

from PYTHON_POO.ASinterface import Interface

i1 = Interface()
i1.mostrar()  # Método da classe filha

print('########################')

i1.chamar_metodo_da_interface()  # Classe mãe herdando da classe filha
