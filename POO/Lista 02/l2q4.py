"""
Desenvolva um programa na linguagem Python que leia do usuário duas listas
de números inteiros l1 e l2 com o mesmo tamanho n (esse valor também deve ser definido
pelo usuário). Essas listas correspondem a pontuação de dois alunos a1 e a2 em um
desafio. Seu programa deve exibir a pontuação dos dois alunos (p_a1 e p_a2), que é dado
usando as regras explicadas seguir. Por exemplo, dadas as listas l1 = [4, 6, 7, 2] e l2 = [3,
9, 8, 5], seu programa deve exibir p_a1 = 1 e p_a2 = 3.
• Se l1[i] > l2[i], o aluno 1 (a1) ganha um ponto;
• Se l1[i] < l2[i], o aluno 2 (a2) ganha um ponto;
• Se l1[i] = l2[i], ninguém ganha ponto.
"""

n = int(input("Escrava o tamanho da lista de pontos:"))
aluno1 = []
aluno2 = []

p_a1 = 0
p_a2 = 0

print("===========ALUNO 1==========")
for i in range(n):
    aluno1.append(int(input(f"nota {i+1}: ")))
print("===========ALUNO 2==========")
for i in range(n):
    aluno2.append(int(input(f"nota {i+1}: ")))

for i in range(n):
    if aluno1[i] < aluno2[i]:
        p_a2 += 1
    elif aluno1[i] > aluno2[i]:
        p_a1 += 1
    else:
        pass

print(f"p_a1 = {p_a1}")
print(f"p_a2 = {p_a2}")
