'''
Questão 7. Crie uma classe chamada Ingresso, que possui um valor em reais e um método
imprimir_valor(). Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor
adicional. Crie um método que retorne o valor do ingresso VIP (com o adicional incluído).
Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a
diferença de preços.
'''

class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    
    def imprimir_valor(self):
        print(f"Valor = {self.valor}")

class IngressoVip(Ingresso):
    def __init__(self, valor, adicional):
        self.valor = valor + adicional

ingresso = Ingresso(15)
ingresso.imprimir_valor()

inVip = IngressoVip(15, 15)
inVip.imprimir_valor()