'''
Questão 8. Um Grafo é uma estrutura de dados muito comum em computação, e os
algoritmos sobre grafos são fundamentais para a área. Um grafo G = (V, A) consiste em:
• Um conjunto finito de pontos V. Os elementos de V são chamados de vértices de
G.
• Um conjunto finito A de pares não ordenados de V, que são chamados de arestas
de G.
Uma aresta a em A é um par não ordenado (v, w) de vértices v, w em V, que são
chamados de extremidades de a. Uma aresta a em A é chamada de incidente com um
vértice v em V, se v for uma extremidade de a. Um vértice v em V diz-se vizinho de outro
vértice w em V se existir uma aresta a em A incidente com v e w. Um grafo pode ser
representado por listas de adjacência ou por uma matriz de adjacência.


Desenvolva na linguagem Python uma classe para representar grafos. Escolha
entre a representação por listas de adjacência ou por matriz de adjacência. A classe deve
oferecer as seguintes operações:

1. Inserir um vértice;
2. Inserir uma aresta entre dois vértices já inseridos no grado;
3. Listar todos os vértices;
4. Listar todas as arestas;
5. Determinar se dois vértices são vizinhos;
6. Determinar a lista de todos os vértices que são vizinhos de um dado
vértice.

Considere que cada vértice é representado por um número inteiro. Escreva um
script principal para testar sua classe.
'''

class Grafo:
    def __init__(self):
        self.V = {}

    def Inserir_vertice(self, _v):
        if _v in self.V:
            pass
        else:
            self.V[_v] = []

    def Inserir_aresta(self, v1, v2):
        if v1 in self.V and v2 in self.V:
            if v1 not in self.V[v2]:
                self.V[v1].append(v2)
                self.V[v2].append(v1)
            else:
                pass #Já foi adicionado

    def ListarVertices(self):
        print("Vertice - Aresta")
        for v in self.V:
            print(f"{v} - {self.V[v]}")
    
    def ListarVizinhosDe(self, v):
        for a in self.V[v]:
            print(f"{a}")
    
    def ListarArestas(self): #não fiz tratamento para evitar repetição
        for V in self.V:
            for a in self.V[V]:
                print(f"{a} ------ {V}")
    
    def sao_vizinhos(self, v1, v2):
        if v1 in self.V[v2]:
            return True
        else:
            return False
    
    
G = Grafo()

G.Inserir_vertice(1)
G.Inserir_vertice(2)
G.Inserir_vertice(3)
G.Inserir_vertice(4)
G.Inserir_vertice(5)

G.Inserir_aresta(1, 2)
G.Inserir_aresta(1, 5)
G.Inserir_aresta(2, 1)#Essa aresta já foi adcionada
G.Inserir_aresta(2, 5)
G.Inserir_aresta(2, 4)
G.Inserir_aresta(2, 3)
G.Inserir_aresta(5, 4)
G.Inserir_aresta(3, 4)

G.ListarVertices()
print(f"1 e 2 são vizinhos: {G.sao_vizinhos(1, 2)}")
print(f"3 e 5 são vizinhos: {G.sao_vizinhos(5, 3)}")
print(f"TODAS AS ARESTAS")
G.ListarArestas()

print("Quais são os vizinhos de 2")
G.ListarVizinhosDe(2)

    

        
