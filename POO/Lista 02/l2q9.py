"""
Uma palavra que é escrita de forma idêntica quando lida da esquerda para
direita e vice-versa, por exemplo 'radar', é chamada de palíndroma. Escreva uma função
em Python chamada de eh_palindroma que recebe uma string por parâmetro e retorna
True se for um palíndroma e False caso contrário. Sua função deve ser case-insensitive,
ou seja, letras maiúsculas e minúsculas devem ser consideradas iguais. Teste sua função
com alguns exemplos.
"""


def eh_palindroma(palavra):
    aux = ''
    size = len(palavra)
    palavra = palavra.upper()
    for i in range(size - 1, -1, -1):
        aux += palavra[i]
    if (aux == palavra):
        return True
    return False

print("=======PALINDROMOS=========")
print(f"sopapos = {eh_palindroma('sopapos')}")
print(f"radar = {eh_palindroma('radar')}")
print(f"Rodrigo = {eh_palindroma('rodrigo')}")
print(f"saias = {eh_palindroma('saias')}")
print(f"Merigueti = {eh_palindroma('merigueti')}")
