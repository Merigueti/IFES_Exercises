class Voo:
    def __init__(self, numero_voo, cidade_origem, cidade_destino, data):
        self.numero_voo = numero_voo
        self.cidade_origem = cidade_origem
        self.cidade_destino = cidade_destino
        self.data = data
        self.cadeiras = {}
        for i in range(1, 201):
            self.cadeiras[i] = False

    def proximo_livre(self):
        for cadeira, ocupado in self.cadeiras.items():
            if not ocupado:
                return cadeira
        return None

    def verifica_assento(self, numero_cadeira):
        return self.cadeiras.get(numero_cadeira, False)

    def marcar_assento(self, numero_cadeira):
        if 1 <= numero_cadeira <= 200:
            if not self.cadeiras[numero_cadeira]:
                self.cadeiras[numero_cadeira] = True
                return True
        return False

    def retornar_vagas(self):
        vagas = 0
        for ocupado in self.cadeiras.values():
            if not ocupado:
                vagas += 1
        return vagas

# Exemplo de uso da classe
voo = Voo(numero_voo=177, cidade_origem="Guarapari", cidade_destino="Jaguaré", data="24/06/1997")

print(f"proximo_livre: {voo.proximo_livre()}")

cadeira_ocupado = 5
print(f"Cadeira {cadeira_ocupado} Ocupada: {voo.verifica_assento(cadeira_ocupado)}")

cadeira_livre = voo.proximo_livre()
if cadeira_livre is not None:
    print(f"Marcando cadeira {cadeira_livre}: {voo.marcar_assento(cadeira_livre)}")

print(f"Vagas disponíveis: {voo.retornar_vagas()}")
