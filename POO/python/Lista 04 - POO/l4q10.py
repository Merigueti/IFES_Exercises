"""
Filas são estruturas de dados muito utilizadas para o desenvolvimento de
diversos tipos de sistemas e algoritmos clássicos na Computação. Uma Fila segue um
padrão chamado de First In Firt Out (FIFO), ou seja, o primeiro elemento inserido na
fila deve ser o primeiro elemento a ser removido. Assim, elementos em uma Fila devem
ser inseridos no fim da fila e a remoção dos elementos sempre no início da fila. A Figura
a seguir ilustra uma fila.


Implemente uma classe em Python para representar a estrutura de dados Fila. Para isso,
você deve representar a fila de elementos em sim como uma lista (atributo da classe Fila).
Além disso, você deve implementar os métodos de: (i) inserir um novo elemento na Fila;
(ii) remover um elemento existente; e (iii) verificar se a fila está vazia. Esses métodos
devem respeitar a regra FIFO mencionada anteriormente. Utilize as estratégias de
encapsulamento para garantir que as operações de inserção e remoção na fila serão feitas
somente usados os métodos implementados anteriormente e não diretamente usando a
atributo da classe Fila. Por fim, implemente alguns testes para sua classe com a inserção
e remoção de alguns elementos
"""


class Fila:
    def __init__(self, lista):
        self.__fila = lista

    @property
    def fila(self):
        return self.__fila
    
    def pop(self):
        self.__fila.pop(0)
    
    def append(self, n):
        self.__fila.append(n)

    def __str__(self):
        return str(self.__fila)

a = Fila([1,2,3,4])
print(f"Fila inicial = {a}")
print("pop")
a.pop()
a.append(5)
print("apend(5)")
print(f"Print fila final {a}")
