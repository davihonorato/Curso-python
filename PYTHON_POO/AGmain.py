# Criar um escritor, uma caneta e uma máquina de escrever. Cada um terá uma classe diferente e elas terão que se
# relacionar.

from PYTHON_POO.AGclasses import Escritor
from PYTHON_POO.AGclasses import Caneta
from PYTHON_POO.AGclasses import MaquinaDeEscrever

escritor = Escritor('Zilla')  # Cria um escritor
caneta = Caneta('azul')  # Cria uma caneta
maquina = MaquinaDeEscrever()  # Cria uma máquina
escritor.ferramenta = caneta  # 'ferramenta' recebe o conteúdo de 'caneta'
escritor.ferramenta.escrever()  # Através de 'ferramenta' é possível acessar os métodos da classe Caneta.
escritor.ferramenta = maquina  # ferramenta recebe o conteúdo de 'maquina'
escritor.ferramenta.escrever()  # Através de 'ferramenta', é possível acessar os métodos da classe MaquinaDeEscrever
