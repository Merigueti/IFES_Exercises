"""
Escreva um programa na linguagem Python que leia um número inteiro
positivo n e em seguida imprima n linhas do chamado Triângulo de Floyd.
"""

n = int(input("Escreva o numero de linhas do triangulo de Floyd: "))

num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{num}", end="\t")
        num += 1
    print()
