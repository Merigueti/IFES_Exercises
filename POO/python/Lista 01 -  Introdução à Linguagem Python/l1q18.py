"""
A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
. Faça um programa na linguagem Python que solicite ao usuário o valor n e imprima
o valor do n_ésimo termo da sequência de Fibonacci. Por exemplo, se o usuário digitar o
valor 4, ou seja, n = 4, seu programa deve imprimir “O valor do 4_ésimo termo da
sequência de Fibonacci é: 3
"""


print("======Fibonacci=====")
n = int(input("Digite o valor de n: "))
if n <= 0:
    n_termo = 0
elif n == 1:
    n_termo = 1
else:
    n_anterior = 1
    n_atual = 1
    for i in range(2, n):
        n_prox = n_anterior + n_atual
        n_anterior = n_atual
        n_atual = n_prox
    n_termo = n_atual

print(f"O valor do {n}_ésimo termo da sequência de Fibonacci é: {n_termo}")
