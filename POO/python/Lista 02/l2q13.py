'''
Questão 13. Desenvolva uma função na linguagem Python que recebe por parâmetro um
texto, calcula e retorna um valor representando a sua pontuação com base nas seguintes
regras:
    • A pontuação de uma palavra é 2 se a palavra contém um número ímpar de vogais,
caso contrário, o escore da palavra é igual a 1. Letras maiúsculas e minúsculas
devem ser consideradas iguais. Considere que o texto de entrada não possui
nenhum símbolo de acentuação. A lista de vogais é: ['a', 'e', 'i', 'o', 'u']
    • A pontuação total do texto é dada pela média das pontuações das suas palavras,
ou seja, soma as pontuações das palavras individualmente e divide pelo total de
palavras do texto.
    • Fragmente o texto por espaço em branco para identificar as suas palavras.
        Exemplos:
        a) Entrada: Python e muito fácil
        Saída: 1.75
        b) Entrada: Ola Mundo
        Saída: 1.0
'''

def calcPontos(texto):
    vogais = ["A","E","I","O","U"]
    palavras = texto.upper()
    palavras = palavras.split(' ')
    pontos = 0
    print(palavras)
    for palavra in palavras:
        n_vogais = 0
        for l in palavra:
            if l in vogais:
                n_vogais += 1
        if n_vogais%2 == 0:
            pontos += 1
        else:
            pontos += 2
    pontos = pontos/len(palavras)
    return pontos
    


    # print(palavra)
print(f"'Python e muito fácil' tem {calcPontos('Python e muito facil')} pontos!")
print(f"'Ola Mundo' tem {calcPontos('Ola Mundo')} pontos!")