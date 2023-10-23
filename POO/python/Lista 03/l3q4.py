'''
Questão 4. Desenvolva na linguagem Python uma função que recebe por parâmetro dois
nomes de arquivos e copia o conteúdo do primeiro arquivo para o segundo arquivo.
Considere que o conteúdo do arquivo de origem é um texto. Sua função NÃO deve copiar
linhas comentadas (que começam com #). Teste sua função com diferentes arquivos de
entrada.
'''

entrada = input('Escreva o diretório de entrada:\n')
lines = []
try:
    with open("C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/entrada.txt", 'r', encoding='utf-8') as arq:
        lines = arq.read().splitlines() 
except:
    print(f"Diretório -> {entrada} não foi encontrado")

saida = input('Escreva o diretório de saida:\n')
with open("C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/saida.txt", 'w', encoding='utf-8') as arq:
    for linha in lines:
        if linha[0] == '#':
            continue
        if '\n' in linha:
            arq.write(linha)
        else:
            arq.write(linha + '\n')

print('Programa finalizado!')