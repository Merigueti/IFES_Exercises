"""
Questão 14. Crie um script na linguagem Python que leia do usuário um número inteiro
n, correspondente a um valor em reais. Calcule a quantidade mínima de notas que um
banco deve fornecer para atingir o valor. Notas disponíveis: 100,00 reais; 50,00 reais;
10,00 reais; 5,00 reais e 1,00 real.
"""

reais = int(input("Quantos reais você deseja retirar?\n"))

notas100 = int(reais/100)
print(f"{notas100} notas de 100")
notas50 = int((reais % 100)/50)
print(f"{notas50} notas de 50")
notas10 = int(((reais % 100) % 50)/10)
print(f"{notas10} notas de 10")
notas5 = int((((reais % 100) % 50) % 10)/5)
print(f"{notas5} notas de 5")
notas1 = int((((reais % 100) % 50) % 10) % 5)
print(f"{notas1} notas de 1")
