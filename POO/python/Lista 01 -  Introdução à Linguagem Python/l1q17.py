"""
O dono de uma loja deseja informatizá-la e quer que você desenvolva um
programa na linguagem Python que leia os preços dos produtos comprados por um cliente
até que seja informado o valor zero. No final, seu programa deve informar o total da
compra e perguntar a forma de pagamento. As opções da forma de pagamento são: 1) À
vista; 2) No cartão de crédito. Se a opção escolhida for à vista, então o programa informa
o valor da compra com um desconto de 15%. Caso a compra seja no cartão de crédito, o
programa informa o valor da compra dividido em 4 vezes.
"""

total = 0
print("================loja================")
while (True):
    valor = float(input("Escreva o valor do produto ou 0 para sair: "))
    if valor > 0:
        total += valor
    else:
        break

while (True):
    print("Escolha a forma de pagamento:")
    print("[1] A vista")
    print("[2] Cartão de crédito")
    valor = int(input())
    if (valor == 1):
        print(f"Valor total da compra R${total:.2f}")
        print(
            f"Valor a pagar com desconto por pagamento a vista = R${total-total*0.15:.2f}")
        break
    elif (valor == 2):
        print(f"Valor total da compra: R${total:.2f}")
        print(f"valor dividido em 4 vezes: R${total/4:.2f}")
        break
    else:
        print("COMANDO INVALIDO\n\n")
