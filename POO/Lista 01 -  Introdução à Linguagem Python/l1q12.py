"""
Questão 12. O Supermercado Tabajara está com uma super promoção de carnes,
conforme a tabela a seguir:
Tipo Até 5 Kg Acima de 5 Kg
File Duplo R$ 14,90 por Kg R$ 15,80 por Kg
Alcatra R$ 15,90 por Kg R$ 16,80 por Kg
Picanha R$ 16,90 por R$ 17,80 por Kg
Para atender a todos os clientes, cada um poderá levar apenas um dos tipos de
carne da promoção, porém não há limites para a quantidade de carne por cliente. Se a
compra for feita no cartão do supermercado o cliente receberá ainda um desconto de 5%
sobre o total da compra. Escreva um programa na linguagem Python que solicite ao
cliente o tipo e a quantidade de carne comprada e gere um cupom fiscal, contendo as
informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor
do desconto e valor a pagar.
"""

produto_ate_5kg = [
    ["File Duplo", 14.90],
    ["Alcatra", 15.90],
    ["Picanha", 16.90]
]

produto_mais_de_5kg = [
    ["File Duplo", 15.80],
    ["Alcatra", 16.80],
    ["Picanha", 17.80]
]

print("Carnes")
print("[0] Filé Duplo")
print("[1] Alcatra")
print("[2] Picanha")
carne = int(input("Digite o numero correspondente a Carne: "))
peso = float(input("Digite o peso que deseja comprar [kg]"))
cartao = int(input("Você possui um cartão da loja? [0 = não; 1 = Sim]: "))
total = 0

print("\n\nCUPOM FISCAL")

total = produto_mais_de_5kg[carne][1]*peso


print(f"{produto_mais_de_5kg[carne][0]} _________ {peso}kg")
print(f"Total = R${total:.2f}" )
if(peso <= 5):
    total = produto_ate_5kg[carne][1]*peso
    print(f"Desconto do produto = R${produto_mais_de_5kg[carne][1]*peso - total:.2f}")
    print(f"valor com desconto do produto: R${total}")

if cartao:
    print("Pagamento com cartão da loja")
    print(f"Valor do deconto do cartão {total*0.05:.2f}")
    total = -total*0.05 + total
    print(f"Valor Total com desconto do cartão: {total:.2f}\n")
else:
    print("Pagamento efetuado sem cartão\n\n\n")

