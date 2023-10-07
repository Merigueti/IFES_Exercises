"""
Questão 20. Um palíndromo é um número, palavra ou frase com a mesma leitura da
esquerda para direita e vice-versa. Por exemplo, cada um dos seguintes números inteiros
de cinco dígitos é um palíndromo: 12321, 55555, 45554 e 11611. Escreva um script na
linguagem Python que leia um número inteiro de cinco dígitos e determine se ele é um
palíndromo.
"""

while (True):
    n = int(input("Esreva um numero de 5 dígitos: "))
    if (n < 10000 or n > 99999):
        print("Valor invalido")
    else:
        break

dig1 = n // 10000
dig2 = (n // 1000) % 10
dig3 = (n // 100) % 10
dig4 = (n // 10) % 10
dig5 = n % 10

if dig1 == dig5 and dig2 == dig4:  # não verifico dig3 pq ele fica no centro
    print("o numero digitado é um palíndromo")
else:
    print("O numero digitado não é um palíndromo")
