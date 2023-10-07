"""
Desenvolva uma função em Python chamada de codificar, que recebe uma
string como parâmetro e retorna uma string criptografia definida usando as regras a
seguir. Cada caractere em uma posição ímpar i no alfabeto será criptografado com o
caractere na posição i + 1, e cada caractere em uma posição par i será criptografado com
o caractere na posição i – 1. Por exemplo, a letra 'a' é criptografada com 'b', a letra 'b' com
'a', 'c' com 'd', 'd' com 'c' e assim por diante. Caracteres minúsculos deverão
permanecer minúsculos, e caracteres maiúsculos deverão permanecer assim. Teste sua
função com alguns exemplos.

"""

def codificar(palavra):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = abc.upper()
    bad = ''
    for l in palavra:
        if l in abc:
            pos = abc.find(l)
            if pos%2 == 0:
                bad += abc[pos+1]
            else:
                bad += abc[pos-1]
        elif l in ABC:
            pos = ABC.find(l)
            if pos%2 == 0:
                bad += ABC[pos+1]
            else:
                bad += ABC[pos-1]
        else:
            bad += l
    return bad

def decodifica(palavra):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = abc.upper()
    bad = ''
    for l in palavra:
        if l in abc:
            pos = abc.find(l)
            if pos%2 == 0:
                bad += abc[pos+1]
            else:
                bad += abc[pos-1]
        elif l in ABC:
            pos = ABC.find(l)
            if pos%2 == 0:
                bad += ABC[pos+1]
            else:
                bad += ABC[pos-1]
        else:
            bad += l
    return bad

print(f"abcd! = {codificar('abcd!')}")
print(f"Banana = {codificar('banana')}")
print(f"Rodrigo Ribeiro Merigueti = {codificar('Rodrigo Ribeiro Merigueti')}")