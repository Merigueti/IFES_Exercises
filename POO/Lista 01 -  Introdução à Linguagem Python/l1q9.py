"""

Questão 9. Desenvolva um programa na linguagem Python que leia duas notas parciais
de um aluno. Seu programa deve calcular a média alcançada pelo aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a 7,0;
• A mensagem "Reprovado", se a média for menor do que 7,0;
• A mensagem "Aprovado com Distinção", se a média maior ou igual a 9,5.

"""

n1 = float(input("Escreva a nota 01: "))
n2 = float(input("Escreva a nota 02: "))

media = (n1+n2)/2
print(f"Media = {media}")

if(media >= 9.5):
    print("Aprovado com Distinção")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")
