'''
Questão 2. Escreva um programa na linguagem Python que leia um arquivo chamado de
nomes.txt contendo vários nomes de pessoas (1 por linha). Seu programa deve ordenar
os nomes e gerar um novo arquivo chamado de nomes_ordenados.txt com os nomes
ordenados. DICA: Leias os nomes dos arquivos e armazene em uma lista de nomes.
Pesquise na internet como ordenar uma lista em Python.
'''
print('START!')

lines = []
with open('C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/nomes.txt', 'r', encoding='utf-8') as arq:
    lines = arq.readlines()
    print(lines)

lines.sort()
print(lines)
with open('C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/nomes_ordenados.txt', 'w', encoding='utf-8') as arq:
    for nome in lines:
        if '\n' in nome:
            arq.write(nome)
        else:
            arq.write(nome + '\n')

print('Programa finalizado!')