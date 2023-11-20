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

from Fatura import Fatura

if __name__ == '__main__':
    f = Fatura(1,"Batata",15 , 1)
    print(f.calcular_valor_fatura())
    f2 = Fatura(2,"Teste 2", -1, 15)
    print(f2.get_numero())
    print(f2.get_quant())

    f2.set_descricao("descricao")
    print(f2.get_descricao())

    f2.set_quant(20)
    print(f2.get_quant())

    f2.set_preco(25)
    print(f2.get_preco())

    f2.set_numero(3)
    print(f2.get_numero())