'''
Questão 3. Faça um programa na linguagem Python que apure o resultado de uma
votação para determinar o personagem do desenho “Dragon Ball” favorito. Suponha que
existam 5 candidatos cujos códigos de identificação são: 1- Goku, 2 - Vegeta, 3 - Gohan,
4 - Broly, 5 - Freeza. Considere que existe um arquivo texto chamado de “votos.txt” que
contém, em cada linha, um determinado voto (um voto é representado pelo código de
identificação do candidato). Seu programa deverá ler o arquivo de votos e apresentar,
como resultado, o nome do candidato e a quantidade de votos do candidato mais votado,
o código de identificação e a quantidade de votos do candidato menos votado, e a
quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um
inteiro diferente de 1, 2, 3, 4 e 5).
'''

print('START!')

votacao = {}
votos = []
with open('votos.txt', 'r', encoding='utf-8') as arq:
    votos = arq.read().splitlines() 

votacao['Goku'] = 0
votacao["Vegeta"] = 0
votacao["Gohan"] = 0
votacao["Broly"] = 0
votacao["Freeza"] = 0
invalido = 0
for i in votos:
    try:
        i = int(i)
        if i == 1:
            votacao['Goku'] += 1
        elif i == 2:
            votacao['Vegeta'] += 1
        elif i == 3:
            votacao['Gohan'] += 1
        elif i == 4:
            votacao['Broly'] += 1
        elif i == 5:
            votacao['Freeza'] += 1
        else:
            invalido += 1
    except:
        pass

maior = votacao[max(votacao)]
menor = votacao[min(votacao)]
for c in votacao: #tratar empates
    if votacao[c] == maior:
        print(f"O candidato {c} teve {votacao[c]} votos e ficou com a maior colocação")
    elif votacao[c] == menor:
        print(f"O candidato {c} teve {votacao[c]} votos e ficou com a menor colocação")


print('Programa finalizado!')