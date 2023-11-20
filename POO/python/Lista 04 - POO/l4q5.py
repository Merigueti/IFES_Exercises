'''
    Questão 5. Identifique e implemente na linguagem Python classes junto com seus
    atributos e métodos para o seguinte cenário: “O supermercado vende diferentes tipos de
    produtos. Cada produto tem um preço e uma quantidade em estoque. Um pedido de um
    cliente é composto de itens, onde cada item especifica o produto que o cliente deseja e a
    respectiva quantidade. Esse pedido pode ser pago em dinheiro, cheque ou cartão.”
'''

class mercado:
    def __init__(self):
        self.__lista_de_produtos = []
    def add_na_lista(self, produto):
        self.__lista_de_produtos.append(produto)
    def remove_da_lista(self, produto):
        if produto in self.__lista_de_produtos:
            self.__lista_de_produtos.pop(produto)
    def get_lista(self):
        return self.__lista_de_produtos

class produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_preco(self):
        return self.preco
    
    def set_preco(self, preco):
        self.preco = preco

    def get_quantidade(self):
        return self.quantidade
    
    def set_quantidade(self, quantidade):
        self.quantidade = quantidade

class pedido:
    def __init__(self, dinheiro_diponivel):
        self.dinheiro_diponivel = dinheiro_diponivel
        self.__lista_de_produtos = []
        self.metodo = ''

    def add_na_lista(self, produto):
        self.__lista_de_produtos.append(produto)
        self.dinheiro_diponivel -= produto.get_preco()

    def remove_da_lista(self, produto):
        if produto in self.__lista_de_produtos:
            self.__lista_de_produtos.pop(produto)

    def get_lista(self):
        return self.__lista_de_produtos
    
    def get_valor_total(self):
        total = 0
        for poduto in self.__lista_de_produtos:
            total += poduto.get_preco()
    
    def set_metodo_de_pagamento(self, metodo):
        self.metodo = metodo
    