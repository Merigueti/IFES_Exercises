'''
Questão 5. Desenvolva um programa na linguagem Python que leia do usuário o caminho
de um diretório (pasta). Seu programa deve ler e imprimir na tela todos os arquivos e
pastas contidos no diretório informado pelo usuário.
'''
from os import listdir

diretorio = input("Entre com o diretorio que deseja listar os arquivos:")
for arq in listdir(diretorio):
    print(f"- {arq}")