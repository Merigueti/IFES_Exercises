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
    def __init__(self):
        self.__lista_de_produtos = []
        self.metodo = ''

    def add_na_lista(self, produto):
        self.__lista_de_produtos.append(produto)

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
    