"""
Questão 5. Crie um programa em Python que leia uma lista p contendo n números
inteiros representando a pontuação de um atleta nos seus jogos. Seu programa deve
imprimir na tela a quantidade de vezes que esse atleta bateu seu recorde de pontuação
máxima (p_max) e mínima (p_min). Por exemplo, dada lista p = [10, 5-, 20+, 20, 4-, 5, 2-,
25+, 1-] seu programa deve exibir p_max = 2 e p_min = 4. com + estão representados
os recordes de maior pontuação e em com - de menor pontuação.
"""

print("Escreva um valor negativo para sair")
p = []
while True:
    pontos = float(input("Quantos pontos você fez nesta jogada?\n"))
    if pontos > 0:
        p.append(pontos)
    else:
        break

p_max = 0
p_min = 0
maior_atual = p[0]
menor_atual = p[0]

for i in range(1, len(p)):
    if p[i] > maior_atual:
        maior_atual = p[i]
        p_max += 1
    if p[i] < menor_atual:
        menor_atual = p[i]
        p_min += 1

print(f"p_min = {p_min}")
print(f"p_max = {p_max}")
