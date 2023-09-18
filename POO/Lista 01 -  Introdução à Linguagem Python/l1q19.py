"""
Desenvolva um programa na linguagem Python que mostre os n termos da
Série a seguir. O valor de n deve ser solicitado ao usuário e ao final da execução seu
programa deve exibir o valor final de S
"""

n = int(input("Escrava o n desejado para o calculo de S: "))

m = 1
s = 0
for i in range(1, n):
    print(f"{i}/{m} + ..")
    s += (i/m)
    m += 2

print(f"Valor final -> S = {s}")

