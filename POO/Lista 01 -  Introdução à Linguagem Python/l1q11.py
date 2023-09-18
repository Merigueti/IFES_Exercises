"""
Questão 11. Escreva um programa na linguagem Python para aprovar o empréstimo
bancário para compra de um imóvel. O programa deve solicitar ao usuário o valor do
imóvel a comprar, o salário e a quantidade de parcelas a pagar. O valor da prestação
mensal não pode ser superior a 40% do salário. Calcule o valor da prestação como sendo
o valor do imóvel a comprar dividido pelo número de parcelas a pagar.
"""

imovel = float(input('Digite o valor do imóvel: '))
salario= float(input('Agora escreva o seu salário: '))
parcelas= int(input('Escreva em quantas parcelas o senhor pretende pagar: '))

valor_por_parcela = imovel/parcelas
print(f"Valor por parcela = {valor_por_parcela:.2f} -> {(valor_por_parcela/salario)*100:.2f}%")

pode_pagar = True if (valor_por_parcela/salario)*100 <= 40 else False

if not pode_pagar:
    print("Não podemos aprovar o seu empréstimo.")
else:
    print("Emprestimo aprovado!")