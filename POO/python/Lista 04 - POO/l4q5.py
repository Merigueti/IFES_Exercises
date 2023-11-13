class mercado():
    def __init__(self):
        self.__lista_de_produtos
    
    def add_produto(self, produto):
        self.__lista_de_produtos.append(produto)

class produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    def set_preco(self, preco):
        self.__preco = preco
    
    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade
    
class pedido:
    def __init__(self):
        self.__lista_de_compra = {}
        self.metodo_de_pagamento = ''
    
    def add_na_lista_de_compra(self, produto, quantidade):
        if produto.get_quantidade() >= quantidade:
            self.__lista_de_compra[produto.get_nome()] = quantidade
            produto.set_quantidade = (produto.get_quantidade() - quantidade)
        else:
            print("O mercado não pode fornecer essa quantidade de produtos!")
    
    def get_lista_de_compra(self):
        return self.__lista_de_compra

    def remove_item_da_lista(self, produto):
        self.__lista_de_compra.pop(produto)
    
    def set_metodo_de_pagemnteo(self, metodo):
        if metodo == 1:
            self.metodo_de_pagamento = 'cartão'
        elif metodo == 2:
            self.metodo_de_pagamento = 'dinheiro'
        elif metodo == 3:
            self.metodo_de_pagamento = 'cheque'
        else:
            return None
        return True

class cliente:
    def __init__(self, dinheiro, pedido):
        self.dinheiro = dinheiro
    
    def pagar(self, pedido):
        if self.dinheiro < pedido.get_total_compra()
            print("Pedido pago!")
        else:
            print('Pedido negado por falta de grana!')


    

carone = mercado()
