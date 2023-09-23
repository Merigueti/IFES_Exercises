"""

Questão 2. Implemente um script na linguagem Python que leia do usuário uma
mensagem de texto e a converta fazendo as seguintes alterações:
• A letra a ➔ !
• A letra e ➔ @
• A letra i ➔ #
• A letra o ➔ $
• A letra u ➔ &
Seu programa considerar letras maiúsculas e minúsculas como iguais. Ao final deve-
se imprimir na tela a nova mensagem resultante após as trocas realizadas.

"""

txt = str(input("Escreva a mensagem: "))
txt = txt.lower()
txt = txt.replace('a','!')
txt = txt.replace('e','@')
txt = txt.replace('i','#')
txt = txt.replace('o','$')
txt = txt.replace('u','&')
print(txt)