"""
Questão 6. Desenvolva uma função em Python que recebe por parâmetro uma matriz n x
m, calcula e retorna sua transposta. Teste sua função com alguns exemplos.
"""


def transpor_matriz(matriz):
    n = len(matriz)
    m = len(matriz[0])

    matriz_transposta = []
    for _ in range(m):
        matriz_transposta.append([0]*n)

    for i in range(n):
        for j in range(m):
            matriz_transposta[j][i] = matriz[i][j]

    return matriz_transposta


matriz = [[1, 2, 3],
          [4, 5, 6]]

print(f"Original : {matriz}")
print(f"Transposta : {transpor_matriz(matriz)}")
