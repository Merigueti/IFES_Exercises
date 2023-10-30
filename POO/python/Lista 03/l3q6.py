'''. Implemente um programa na linguagem Python que analise um arquivo
chamado de “pontuacoes.csv” contendo dados das pontuações dos jogadores nas partidas.
Seu programa deve ler, processar o arquivo e gerar um outro arquivo CSV chamado
“maiores_pontuacoes.csv” em que cada linha do arquivo tem o nome do jogador e sua
maior pontuações. Seguem exemplos dos arquivos “pontuacoes.csv” e
“maiores_pontuacoes.csv”:
'''
import csv


lines = []
with open('C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/pontuacoes.csv', 'r', encoding='utf-8') as arq:
    lines = arq.readlines()
    print(lines)

pontos = {}
maior = {}

for l in lines:
    line = l.replace("\n", "")
    line = line.split(";")
    pontos[line[0]] = line[1]
    if line[0] in maior:
        if maior[line[0]] < line[1]:
            maior[line[0]] = line[1]
    else:
        maior[line[0]] = line[1]
        
maior.pop('nome')

with open('C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/maiores_pontuacoes.csv', 'w', encoding='utf-8') as arq:
    arq.write(f"nome;maior pontuação\n")
    for i in maior:
        print((f"{i};{maior[i]}"))
        arq.write(f"{i};{maior[i]}\n")
    
