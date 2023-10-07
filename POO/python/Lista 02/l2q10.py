'''
Escreva a função reverte_agenda, que aceite como entrada uma agenda, ou
seja, um dicionário mapeando nomes (as chaves) a números de telefone (os valores). A
função deverá retornar outro dicionário representando a agenda reversa, mapeando
números de telefone (as chaves) aos nomes (os valores). Teste sua função com alguns
exemplos.
'''

def reverte_agenda(agem):
    agenda_reversa = {}
    for nome, telefone in agem.items():
        agenda_reversa[telefone] = nome
    return agenda_reversa

agenda = {"Rodrigo": "3321-8600",
          "Jorge" : "9975-7080",
          "Bianca" :"9913-4778",
          "Matheus": "9983-3354"}

print(f"Agenda original -> {agenda}")
print(f"Agenda invertida -> {reverte_agenda(agenda)}")
