'''
Questão 6. Crie uma classe chamada Fatura que possa ser utilizado por uma loja de
suprimentos de informática para representar uma fatura de um item vendido na loja. Uma
fatura deve incluir as seguintes informações como atributos: O número do item faturado,
a descrição do item, a quantidade comprada do item e o preço unitário do item. Sua classe
deve ter um construtor que inicialize os quatro atributos. 

Se a quantidade não for positiva, ela deve ser configurada como 0. Se o preço por item não for positivo ele deve ser
configurado como 0.0. Forneça os métodos get/set para cada variável de instância.

Além disso, forneça um método chamado calcular_valor_fatura que calcula o valor da fatura
(isso é, multiplica a quantidade pelo preço por item) e depois retorna o valor. Escreva
também um programa de teste (main) que demonstra as capacidades da classe Fatura.
'''

class Fatura:
    def __init__(self, numero, descricao, quant , preco):

        if quant < 0:
            self.quant = 0
        else:
            self.quant = quant

        if preco < 0:
            self.preco = 0
        else:
            self.preco = preco
        
        self.numero = numero
        self.descricao = descricao

    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def set_quant(self, quant):
        if quant < 0:
            self.quant = 0
        else:
            self.quant = quant
    
    def set_preco(self, preco):
        if preco < 0:
            self.preco = 0
        else:
            self.preco = preco

    def set_numero(self, numero):
        self.numero = numero

    def get_descricao(self):
        return self.descricao
    
    def get_quant(self):
        return self.quant
        

    def get_preco(self):
        return self.preco
        
    def get_numero(self):
        return self.numero
    
    def calcular_valor_fatura(self):
        return self.quant*self.preco
    