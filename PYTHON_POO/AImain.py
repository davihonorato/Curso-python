from PYTHON_POO.AIclasses import Cliente

c1 = Cliente('Davi')  # Cria o cliente 1
c1.adicionar_end('Natal', 'RN')  # Endereço do cliente 1
print(c1.nome)
c1.listar_end()
del c1  # Para indicar a ligação da classe Clientes com a classe Endereco (caso Clientes for apagada, a outra também
# é apagada)
print()

c2 = Cliente('JP')  # Cria o cliente 2
c2.adicionar_end('Florianópolis', 'SC')  # Endereço do cliente 2
print(c2.nome)
c2.listar_end()
del c2  # Para indicar a ligação da classe Clientes com a classe Endereco (caso Clientes for apagada, a outra também é
# apagada)
print()

c3 = Cliente('Fernando')  # Cria o cliente 3
c3.adicionar_end('São Paulo', 'SP')  # Endereço do cliente 3
print(c3.nome)
c3.listar_end()
del c3  # Para indicar a ligação da classe Clientes com a classe Endereco (caso Clientes for apagada, a outra também é
# apagada)
print()

print('#####################################')  # fim
