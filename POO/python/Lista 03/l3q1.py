'''
Questão 1. Desenvolva um programa em Python que solicite ao usuário o nome de um
arquivo existente e uma palavra. Seu programa deve retornar o número de vezes que a
palavra lida aparece no arquivo.
'''

diretorio = input('Escreva o diretório do arquivo:\n')
palavra = input('Escreva a palavra que deseja contar: ')
q = 0

try:
    with open(diretorio, 'r', encoding='utf-8') as arq:
        texto = arq.read()
        q = texto.count(palavra)
except:
    print(f"Diretório -> {diretorio} não foi encontrado")

print(f'{q} ocorrências foram encontradas')

