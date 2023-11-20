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

    def Inserir_vertice(self, _v , _A = []):
        print('===========================')
        print(f"2 {_A}")
        A = _A
        v = int(_v)
        block = False
        print(f"1 {v}")
        if v not in self.V:
            if A == []:
                self.V[v] = A
            else:
                for i in A:
                    if i not in self.V:
                        block = True
                if block == False:
                    self.V[v] = A
            return True
        else:
            return False
        
    def ListarVertices(self):
        return self.V
    
G = Grafo()

G.Inserir_vertice(0)
G.Inserir_vertice(1, [0])
G.Inserir_vertice(2, [0, 1])
G.Inserir_vertice(2, [0, 1]) #Não vai inserir pois nó V2 já foi adicionado
G.Inserir_vertice(4, [3, 1]) #Não vai inserir pois não exist V3


print(G.ListarVertices())
    

    

        
