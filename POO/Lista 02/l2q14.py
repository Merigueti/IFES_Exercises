'''Escreva um programa em Python para armazenar uma agenda de telefones
em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é
o nome da pessoa. Seu programa deve ter as seguintes funções:

    • incluir_novo_nome - essa função acrescenta um novo nome na agenda, com um
    ou mais telefones. Ela deve receber como argumentos o nome e os telefones;
    • incluir_telefone - essa função acrescenta um telefone em um nome existente na
    agenda. Caso o nome não exista na agenda, você deve perguntar se a pessoa
    deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir
    o novo nome;
    • excluir_telefone - essa função exclui um telefone de uma pessoa que já está na
    agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda;
    • excluir_nome - essa função exclui uma pessoa da agenda;
    • consultar_telefone - essa função retorna os telefones de uma pessoa na agenda;

Seu programa deve ter dois arquivos de código, um arquivo somente com as
implementações das funções e um outro arquivo contendo um menu com uma opção para
que o usuário execute cada uma das funções listadas anteriormente. Seu programa deve
ficar repetindo a exibição do menu e respondendo as ações do usuário até que ele Escreva
a opção 6 - Sair.

    ------ Menu Agenda ------
    1 - Incluir novo nome
    2 - Incluir telefone
    3 - Excluir telefone
    4 - Excluir nome
    5 - Consultar telefone
    6 - Sair
'''

from agenda import *

def limpar_tela():
    print("\n" * 50)

def list_names(agenda):
    print("======NOMES======")
    for n in agenda.keys():
        print(n)

def list_number(agenda, nome):
    print("=====Telefones=====")
    if nome in agenda:
        for n in agenda[nome]:
            print(n)

while True:
    print("\n------ Menu Agenda ------")
    print("1 - Incluir novo nome")
    print("2 - Incluir telefone")
    print("3 - Excluir telefone")
    print("4 - Excluir nome")
    print("5 - Consultar telefone")
    print("6 - Sair")
    
    option = input("Escolha uma opção: ")

    if option == '1': #Incluir novo nome
        limpar_tela()
        nome = input("Escreva o nome: ")
        telefones = input("Escreva os telefones usando espaço para separar: ").strip().split(' ')
        incluir_novo_nome(nome, telefones)
    elif option == '2': #Incluir Telefone
        limpar_tela()
        list_names(agenda)
        nome = str(input("Escreva o nome ao qual deseja incluir um telefone: "))
        list_number(agenda, nome)
        telefone = input("Escreva o numero de telefone: ")
        incluir_telefone(nome, telefone)
    elif option == '3':
        limpar_tela()
        list_names(agenda)
        nome = input("Escreva o nome ao qual deseja excluir um telefone: ")
        list_number(agenda, nome)
        telefone = input("Escreva o telefone que dejesa excluído: ")
        excluir_telefone(nome, telefone)
    elif option == '4':
        limpar_tela()
        list_names(agenda)
        nome = input("Escreva o nome que dejesa excluído: ")
        excluir_nome(nome)
    elif option == '5':
        limpar_tela()
        list_names(agenda)
        nome = input("Escreva o nome para consultar os telefones: ")
        telefones = consultar_telefone(nome)
        if telefones:
            print(f"Telefones de '{nome}': {', '.join(telefones)}")
        else:
            print(f"'{nome}' não encontrado na agenda.")
    elif option == '6':
        break
    else:
        limpar_tela()
        print("Opção inválida!")
        input("Aperte enter para continuar...")
