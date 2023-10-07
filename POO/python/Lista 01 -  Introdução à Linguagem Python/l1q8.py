"""

Questão 8. Implemente um script na linguagem Python que calcula o salário bruto,
descontos e o salário de líquido dos funcionários de uma empresa. Seu script deve solicitar
o valor que o funcionário ganha por hora e o número de horas trabalhadas no mês. Calcule
e exiba o total do seu salário bruto e líquido no referido mês, sabendo que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato do salário bruto.
Ao final da execução seu script deve exibir:

Salário Bruto: R$
IR (11%): R$
INSS (8%): R$
Sindicato (5%): R$
Salário Liquido: R$
OBS: O salário líquido é igual ao salário bruto menos os descontos.

"""

bruto = float(input("Escreva o Salário Bruto:"))

ir = bruto*0.11
inss = bruto*0.08
sindicato = bruto*0.05
Liquido = bruto-ir-inss-sindicato

print(f"\nSalário Bruto: R${bruto:.2f}")
print(f"IR (11%): R${ir:.2f}")
print(f"INSS (8%): R${inss:.2f}")
print(f"Sindicato (5%): R${sindicato:.2f}")
print(f"Salário Liquido: R${Liquido:.2f}")
