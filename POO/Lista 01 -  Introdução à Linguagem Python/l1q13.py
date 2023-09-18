"""
Questão 13. Escreva um programa na linguagem Python que solicite ao usuário a
distância que um passageiro deseja percorrer em quilômetros (km). Calcule o preço da
passagem, cobrando R$ 0,80 por km para viagens de até de 200 km, e R$ 0,50 para
viagens mais longas.
"""

km = int(input("Escreva quantos kilometros pretende percorrer: "))
total = km*0.80 if km <= 200 else km*0.50
print(f"valor total da corrida = R${total:.2f}")