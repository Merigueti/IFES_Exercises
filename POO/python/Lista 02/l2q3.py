"""Questão 3. Em uma pesquisa realizada no IFES, N alunos foram solicitados a avaliar em
uma escala de 1 a 5 a qualidade da comida no refeitório, sendo 1 "PÉSSIMO" e 5
"EXCELENTE". Desenvolva um script em Python que leia as avaliações dos alunos com
avaliações na escala de 1-5 (somente valores inteiros). Seu programa deve encerrar a
votação quando o usuário digitar um valor que esteja fora do intervalo permitido. Seu
programa deve ao final determinar e exiba a frequência de cada avalição e as seguintes
estatísticas das respostas lidas: mínima, máxima, média, mediana, moda, variância e
desvio padrão."""


def get_mediada(number_list):
    number_list.sort()
    if len(number_list) % 2 == 0:
        index = int(len(number_list)/2)
        return (number_list[index-1] + number_list[index])/2
    else:
        index = int(len(number_list)/2)
        return number_list[index]


def get_media(number_list):
    return sum(number_list)/len(number_list)


def get_variancia(number_list):
    x = get_media(number_list)
    for xn in number_list:
        a = (xn-x)**2
    return a/(len(number_list)-1)


notas = []

while True:
    print("Em uma escala de 1 a 5, como você descreve a qualidade da comida do refeitório?")
    print('Sendo 1 "Péssimo" e 5 "Excelente"]')
    print("Escreva um valor fora do intervalo para finalizar a votação")
    n = int(input(" -> "))
    if n not in range(1, 6):
        break
    notas.append(n)

notas.sort()

aux = 0
moda = []
for i in range(1, 6):
    print(f"{notas.count(i)} alunos votaram: {i}")
    if notas.count(i) > aux:
        aux = notas.count(i)
        moda = [i]
    elif notas.count(i) == aux:
        moda.append(i)

print(f"A maior nota foi {max(notas)}")
print(f"A menor nota foi {min(notas)}")
print(f"A média das notas é {get_media(notas)}")
print(f"A mediana das notas é {get_mediada(notas)}")
print(f"A moda é reprezentada pelo conjunto {moda}")
print(f"A variância é de {get_variancia(notas)}")
print(f"O desvio padrão é de {get_variancia(notas)**(1/2)}")
print(notas)
