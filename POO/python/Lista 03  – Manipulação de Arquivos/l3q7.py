"""
Questão 7. Implemente um programa na linguagem Python contendo uma função que
recebe como argumentos o caminho de dois arquivos. O primeiro arquivo contém nomes
de alunos e o segundo arquivo contém as notas dos alunos. No primeiro arquivo, cada
linha corresponde ao nome de um aluno e no segundo arquivo, cada linha corresponde às
notas dos alunos (uma ou mais). Por exemplo, a primeira linha do primeiro arquivo tem
o nome do aluno e suas notas estão na primeira linha do segundo arquivo e assim
sucessivamente. As notas de cada aluno estão separadas umas das outras por espaços em
branco. Leia os dois arquivos e gere um terceiro arquivo que contém o nome do aluno
seguido da média de suas notas.
"""

def join_arq(dir_alunos, dir_notas):
    notas_txt = []
    medias = []
    alunos = []
    with open(dir_notas, 'r', encoding='utf-8') as arq:
        notas_txt = arq.readlines()
    for n in notas_txt:
        notas = n.strip().split()
        notas = [int(numero) for numero in notas]
        media = sum(notas)/len(notas)
        medias.append(media)
    
    with open(dir_alunos, 'r', encoding='utf-8') as arq:
        alunos = arq.readlines()
    
    if len(alunos) == len(medias):
        with open('./medias.txt', 'w', encoding='utf-8') as arq:
            for i in range(len(alunos)):
                arq.write(f'{alunos[i].strip()} {medias[i]}\n')
                print(f'{alunos[i].strip()} {medias[i]}')
    else:
        print("ERROR: arquivos com numero de linhas diferentes!")

join_arq('./alunos.txt', './notas.txt')
