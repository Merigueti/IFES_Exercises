"""
Questão 15. Implemente um programa na linguagem Python que calcule o preço a pagar
pelo fornecimento de energia elétrica. Solicite ao usuário a quantidade de kWh consumida
e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o
preço a pagar de acordo com a tabela a seguir:
"""

kWh = float(input("Escreva a quantidade de kWh consumida:"))
print("Slecione o tipo de instalação:")
print("[R] - Residência")
print("[I] - Indústria")
print("[C] - Comércio")
tipo = str(input(""))
tipo = tipo.upper()

if(tipo == "R"):
    valorTotal = 0.4*kWh if kWh <= 500 else 0.65*kWh
    print(f"Residência: valor total = R${valorTotal:.2f}")
elif(tipo == "C"):
    valorTotal = 0.55*kWh if kWh <= 1000 else 0.60*kWh
    print(f"Comércio: valor total = R${valorTotal:.2f}")
elif(tipo == "I"):
    valorTotal = 0.55*kWh if kWh <= 5000 else 0.60*kWh
    print(f"Indústria: valor total = R${valorTotal:.2f}")
else:
    print("Comando invalido")