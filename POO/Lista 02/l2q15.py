'''
O cenário ilustrado nesta questão é fictício e não reflete a realidade. O
número que compõe o Cadastro Nacional da Pessoa Jurídica (CNPJ) segue o padrão
xx.xxx.xxx/xxxx-xx, onde x é um dígito. Esse número é composto por três segmentos de
dígitos, sendo o primeiro o número da inscrição propriamente dito, o segundo (após a
barra) o número de filiais e o terceiro representados pelos últimos dois valores que são os
dígitos verificadores. Os dois dígitos verificadores do CNPJ são gerados a partir dos 12
primeiros dígitos usando as regras apresentadas a seguir. Desenvolva uma função na
linguagem Python que recebe por parâmetro uma string contendo um número de CNPJ
no formato completo e retorna True se o CNPJ for válido, caso contrário retorne False.
Teste sua função com alguns exemplos.
Para ilustrar os cálculos de validação dos dígitos verificadores vamos usar este CNPJ
fictício 11.222.333/0001-81.
    1. A geração do 1º dígito verificador é realizada multiplicando os 12 primeiros
    dígitos do CNPJ da esquerda para direita pela seguinte sequência de números: 5,
    4, 3, 2, 9, 8, 7, 6, 5, 4, 3 e 2. Usando o CNPJ de exemplo teremos o seguinte
    cálculo:
        a) 1 * 5 + 1 * 4 + 2 * 3 + 2 * 2 + 2 * 9 + 3 * 8 + 3 * 7 + 3 * 6 + 0 * 5 + 0 * 4
        + 0 * 3 + 1 * 2 = 102
        
        b) O próximo passo é calcular o resto da divisão de 102 por 11, cujo resultado
        é 3.
        
        c) Caso o resto da divisão seja menor do que 2, o digito verificador é igual a
        0. Caso contrário, o 1º digito verificar é igual a 11 menos o valor do resto
        da divisão do passo b).
    
    i. No nosso exemplo, como 3 é maior do que 2, então calcula-se 11– 3 = 8.
    ii. Logo, o 1º dígito verificador deve ser igual a 8, que é igual ao do nosso CNPJ de exemplo.
    
    2. A geração do 2º dígito verificador é semelhante ao do 1º digito e é realizada
    multiplicando os 12 primeiros dígitos mais o 1º digito verificador do CNPJ da
    esquerda para direita pela seguinte sequência de números: 6, 5, 4, 3, 2, 9, 8, 7, 6,
    5, 4, 3 e 2. Usando o CNPJ de exemplo teremos o seguinte cálculo:
        a) 1 * 6 + 1 * 5 + 2 * 4 + 2 * 3 + 2 * 2 + 3 * 9 + 3 * 8 + 3 * 7 + 0 * 6 + 0 * 5
        + 0 * 4 + 1 * 3 + 8 * 2 = 120
        b) O próximo passo é calcular o resto da divisão de 120 por 11, cujo resultado
        é 10.
        c) Caso o resto da divisão seja menor do que 2, o digito verificador é igual a
        0. Caso contrário, o 2º digito verificar é igual a 11 menos o valor do resto
        da divisão do passo b).
        i. No nosso exemplo, como 10 é maior do que 2, então calcula-se 11 – 10 = 1.
        ii. Logo, o 2º dígito verificador deve ser igual a 1, que é igual ao do nosso CNPJ de exemplo, o que indica que o CN
'''


def validar_cnpj(_cnpj):
    d1 = 0
    d2 = 0
    cnpj = []
    mult1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    mult2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for n in list(_cnpj):
        if n.isdigit():
            cnpj.append(int(n))
    for i in range(len(mult1)):
        d1 += cnpj[i]*mult1[i]
    d1 = 0 if d1/11 < 2 else 11 - d1 % 11
    if d1 != cnpj[12]:
        return False
    for i in range(len(mult2)):
        d2 += cnpj[i]*mult2[i]
    d2 = 0 if d2/11 < 2 else 11 - d2 % 11
    if d2 != cnpj[13]:
        return False

    return True


print("VERIFICANDO CNPJ -> 11.222.333/0001-81")
print(validar_cnpj('11.222.333/0001-81'))

print("\n\nVERIFICANDO CNPJ -> 11.222.444/0001-81")
print(validar_cnpj('11.222.444/0001-81'))
