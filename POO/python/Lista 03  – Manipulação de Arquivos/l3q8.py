'''
Uma empresa está tendo problemas de espaço em disco no seu servidor de
arquivos. Para tentar resolver este problema, o administrador de rede precisa saber qual o
espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
Usando um programa, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.csv":

Nome;Espaço
Alexandre;456123789
Anderson;1245698456
Antonio;123456456
Carlos;91257581
Cesar;987458
Rosemary;789456125

O arquivo CSV gerado possui duas colunas. A primeira coluna tem o nome do
usuário e a segunda tem o espaço em disco que o usuário ocupa em bytes. Desenvolva
um programa em Python que leia o arquivo "usuarios.csv" e gera um outro arquivo
chamado de “relatorio.txt” contendo um relatório do uso de disco do servidor. Seu
relatório deve ter o seguinte formato:

    Usuário Espaço utilizado % do uso
1   alexandre   434,99 MB   16,85%
2   anderson    1187,99 MB  46,02%
3   antonio     117,73 MB   4,56%
4   carlos      87,03 MB    3,37%
5   cesar       0,94 MB     0,04%
6   rosemary    752,88 MB   29,16%


Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

OBS: Observe que no relatório a ser gerado o espaço de disco está sendo representado
em megabytes. Logo, crie uma função que realiza a conversão de bytes para megabytes.
'''
usuarios = {}
linhas = []
with open('./usuarios.csv', 'r', encoding='utf-8') as arq:
    linhas = arq.readlines()

total = 0
linhas = linhas[1:]
for linha in linhas:
    info = linha.strip().split(';')
    if len(info) == 2:
        nome, dados_size = info
        usuarios[nome] = (int(dados_size)/1024)/1024
        total += usuarios[nome]

media = total/len(usuarios)
print(f'{usuarios["Alexandre"]}')
i = 0
a = ''
with open('./relatorio.txt', 'w', encoding='utf-8') as arq:
    arq.write(f'{a:<3s}Usuário{a:<2}Espaço utilizado {a:<2s}% do uso\n')
    print(f'{a:<3s}Usuário{a:<2}Espaço utilizado {a:<2s}% do uso')
    for user, dado in usuarios.items():
        i+=1
        arq.write(f'{i:2d} {user:<10s} {dado:8.2f}MB {((dado/total)*100):8.2f}%\n')
        print(f'{i:2d} {user:<10s} {dado:8.2f}MB {((dado/total)*100):8.2f}%')

    arq.write(f"\n\nEspaço total ocupado: {total:.2f} MB\n")
    arq.write(f"Espaço médio ocupado: {media:.2f} MB\n")
    print(f"\n\nEspaço total ocupado: {total:.2f} MB")
    print(f"Espaço médio ocupado: {media:.2f} MB")
