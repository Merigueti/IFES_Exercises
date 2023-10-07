"""
Uma matriz isQuadrada de números inteiros é um quadrado mágico se o valor
da soma dos elementos de cada j, de cada i e da diagonal principal e da diagonal
secundária é o mesmo. Além disso, a matriz deve conter todos os números inteiros do
intervalo [1 ... n × n]
"""


def verifica_matriz(m):
    t = len(m[0])
    s = sum(m[0])
    c = 0  # |
    d1 = 0  # Diagonal \
    d2 = 0  # Diagonal /

    isQuadrada = True

    for i in range(t):
        print(f"linha {i+1} = {sum(m[i])}")
        if sum(m[i]) != s:
            isQuadrada = False
        c = 0
        for j in range(t):
            if i == j:
                d1 += m[i][j]
            if t-1 - i == j:
                d2 += m[i][j]
            c += m[j][i]

        print(f"Coluna {i+1} = {c}")
        if c != s:
            isQuadrada = False

    print(f"Diagonal \\ = {d1}")
    print(f"Diagonal / = {d2}")

    if d1 != s or d2 != s:
        isQuadrada = False

    return isQuadrada


m = [[15, 8, 1, 24, 17],
     [16, 14, 7, 5, 23],
     [22, 20, 13, 6, 4],
     [3, 21, 19, 12, 10],
     [9, 2, 25, 18, 11]]

print("======MATRIZ======")
for l in m:
    print(l)

print("\n======VERIFICAÇÃO======")
print(f"\nÉ quadrada = {verifica_matriz(m)}")

