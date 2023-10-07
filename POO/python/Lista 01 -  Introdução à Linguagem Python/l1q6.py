"""
Aluno: Rodrigo Ribeiro Merigueti

Questão 6. Implemente um programa na linguagem Python que leia do usuário um valor
inteiro representando o tempo em segundos, converta e imprima na tela esse tempo em
horas, minutos e segundos. Por exemplo, 7564 segundos possuem “2 horas, 6 minutos e
4 segundos”.

"""

valor_em_segundos = int(input("Escreva um valor em segundos:"))

horas = int(valor_em_segundos/(60*60))  # Verifica a quantidade de horas
segundos = int(valor_em_segundos % (60*60))  # Pega o restante de segundos
minutos = int(segundos/60)  # Converte o restante em minutos
segundos = segundos % 60  # Pega o restante de segundos novamente

print(f"{valor_em_segundos} segundos possuem {horas} horas, {minutos} minutos e {segundos} segundos")
