'''
Questão 12. Implemente uma função em Python chamada sublista que receba duas listas
por parâmetro lista_1 e lista_2 e retorna True se a lista_1 é uma sublista da lista_2, ou
False caso contrário. Uma lista 1 é considerada uma sublista de uma lista 2, se todos os
elementos da lista 1 aparecem na lista 2 na mesma ordem em que eles ocorrem na lista 1.
Crie uma função principal e teste sua função com alguns exemplos.

Exemplos:
    • [15, 1, 100] é uma sublista de [20, 15, 30, 50, 1, 100]
    • [15, 50, 20] não é uma sublista de [20, 15, 30, 50, 1, 100]
'''

def sublista(lista_1, lista_2):
    for i in range(len(lista_2) - len(lista_1) + 1): 
        if lista_2[i : i + len(lista_1)] == lista_1: 
            return True 
    return False

l1 = [50, 1, 100]
l2 = [50, 15, 1, 78, 1, 100]
print(f"{l1} é sublista de {l2} -> {sublista(l1,l2)}")

l1 = [50, 1, 100]
l2 = [20, 15, 30, 50, 1, 100]
print(f"{l1} é sublista de {l2} -> {sublista(l1,l2)}")