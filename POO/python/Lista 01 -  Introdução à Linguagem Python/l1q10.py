"""

Questão 10. Implemente um programa em Python que leia do usuário a data de
nascimento de uma pessoa fornecida através de três números: dia, mês e ano. Seu
programa deve verificar a validade da data digitada pelo usuário. Para isso, verifique se
o dia fornecido é válido: dia > 0, dia ≤ 28 para o mês de fevereiro (29 se o ano for
bissexto), dia ≤ 30 em abril, junho, setembro e novembro, dia ≤ 31 nos outros meses.
Verifique a validade dos meses: 0 < mês < 13. Teste a validade do ano: ano ≤ ano atual
(use uma variável com o valor do ano atual). Ao final da execução, seu programa deve
imprimir: “Data Válida” ou “Data Inválida”.

"""

ano_atual = 2023

dia = int(input("Escreva o dia que você nasceu: "))
mes = int(input("Escreva o mes que você nasceu: "))
ano = int(input("Escreva o ano que você nasceu: "))

ano_ok = ano <= 2023
mes_ok = mes < 13 and mes > 0

meses31 = [4, 6, 10, 11]

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    ano_bissesto = True
else:
    ano_bissesto = False

if (mes == 2):
    if (ano_bissesto):
        dia_ok = True if (dia <= 29 and dia > 0) else False
    else:
        dia_ok = True if (dia <= 28 and dia > 0) else False

elif (mes in meses31):
    dia_ok = True if (dia <= 31 and dia > 0) else False
else:
    dia_ok = True if (dia <= 30 and dia > 0) else False

if (dia_ok and mes_ok and ano_ok):
    print("Data Valida")
else:
    print("Data Invalida")
