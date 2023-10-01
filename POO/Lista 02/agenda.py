agenda = {}


def incluir_novo_nome(nome, telefones):
    agenda[nome] = telefones


def incluir_telefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        print(f"O nome '{nome}' não está na agenda.")
        option = input("Deseja incluir este nome na agenda? (S/N) ").lower()
        if option in 's':
            telefones = [telefone]
            incluir_novo_nome(nome, telefones)


def excluir_telefone(nome, telefone):
    if nome in agenda and telefone in agenda[nome]:
        agenda[nome].remove(telefone)
        if not agenda[nome]:
            del agenda[nome]
            print(
                f"O nome '{nome}' foi excluído da agenda, pois não possui mais telefones.")
    else:
        print(f"Telefone '{telefone}' não encontrado para o nome '{nome}'.")


def excluir_nome(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"O nome '{nome}' foi excluído da agenda.")
    else:
        print(f"O nome '{nome}' não está na agenda.")


def consultar_telefone(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        return []
