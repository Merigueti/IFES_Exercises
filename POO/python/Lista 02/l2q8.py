"""
Dado uma lista de números inteiros de tamanho N (a1, a2, a3, ..., 𝑎n) e uma
variável soma (s). Construa uma função em Python que verifique se existe um par (𝑎𝑖, 𝑎𝑗)
com i ≠ j, cuja soma seja igual a s (𝑎𝑖 + 𝑎𝑗 = s). Sua função deve receber por parâmetro
uma lista e valor da soma. Teste sua função com alguns exemplos.

Exemplos:
    • (1, 2, 3, 4) e soma = 8 ➔ False
    • (1, 2, 3, 4, 4) e soma = 8 ➔ True (4, 4)
"""

def verifica_lista(l, s):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i]+l[j] == s:
                return True
    return False

l1 = (1,2,3,4)
print(f'l = {l1}, s = 8-> {verifica_lista(l1 , 8)}')
l2 = (1,2,3,4,4)
print(f'l = {l2}, s = 8-> {verifica_lista(l2 , 8)}')
            
                
                
        