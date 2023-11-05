'''
Questão 4. Desenvolva na linguagem Python uma função que recebe por parâmetro dois
nomes de arquivos e copia o conteúdo do primeiro arquivo para o segundo arquivo.
Considere que o conteúdo do arquivo de origem é um texto. Sua função NÃO deve copiar
linhas comentadas (que começam com #). Teste sua função com diferentes arquivos de
entrada.
'''

def cop(dir1, dir2):
    lines = []
    try:
        with open(dir1, 'r', encoding='utf-8') as arq:
            lines = arq.read().splitlines() 
    except:
        print(f"Diretório -> {dir1} não foi encontrado")
    with open(dir2, 'w', encoding='utf-8') as arq:
        for linha in lines:
            if linha[0] == '#':
                continue
            if '\n' in linha:
                arq.write(linha)
            else:
                arq.write(linha + '\n')


cop("C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/entrada.txt", "C:/Users/20232ceca0399/Documents/lista/IFES_Exercises/POO/python/Lista 03/saida.txt")
print('Programa finalizado!')