'''
Implemente um programa na linguagem Python que crie e manipule um
arquivo (binário) de produtos. Para cada produto, seu sistema deve solicitar os seguintes
dados: código, nome, quantidade em estoque e preço. Seu programa deverá exibir o
seguinte menu:

CADASTRO DE PRODUTOS
    1 - INSERIR UM NOVO PRODUTO
    2 - ALTERAR UM PRODUTO
    3 - EXCLUIR UM PRODUTO
    4 - EXCLUIR TODOS OS PRODUTOS
    5 - CONSULTAR UM PRODUTO
    6 - LISTAR TODOS OS PRODUTOS
    7 - EXIBIR DADOS ESTATÍSTICOS
    8 - SAIR
DIGITE SUA OPÇÃO:


OBSERVAÇÕES:
    • Na opção 1 e 2, seu programa não deve permitir o cadastro de dois ou mais
    produtos com o mesmo código.
    • Nas opções 3 e 5 você deve usar o código para encontrar o produto desejado.
    • Pesquise estratégias que você pode utilizar para realizar as opções 2 e 3.
    • Na opção 7 deverá ser apresentada as seguintes estatísticas:
        a) A quantidade de produtos cadastrados;
        b) A quantidade e o percentual de produtos com estoque baixo (<= 20);
        c) A quantidade e o percentual de produtos acima da média;
        d) A média geral e o desvio padrão dos preços dos produtos cadastrados.
    • Modularize seu programa criando diferentes funções para realizar as tarefas
    necessárias.
'''
import pickle

MENU = '''
CADASTRO DE PRODUTOS
    1 - INSERIR UM NOVO PRODUTO
    2 - ALTERAR UM PRODUTO
    3 - EXCLUIR UM PRODUTO
    4 - EXCLUIR TODOS OS PRODUTOS
    5 - CONSULTAR UM PRODUTO
    6 - LISTAR TODOS OS PRODUTOS
    7 - EXIBIR DADOS ESTATÍSTICOS
    8 - SAIR
DIGITE SUA OPÇÃO: '''

MENU_2 = '''
ALTERAR
    1 - NOME
    2 - CODIGO
    3 - QUANTIDADE EM ESTOQUE
    4 - PREÇO
    5 - VOLTAR
DIGITE SUA OPÇÃO: '''

def inserir(produto):
    with open('produtos.pkl', 'ab') as arq:
        pickle.dump(produto, arq)

def editar(new_produto, code):
    print(new_produto)
    produtos = listar_produtos()
    index = -1
    for i in range(len(produtos)):
        print(produtos[i]['code'])
        if produtos[i]['code'] == code:
            if new_produto != None:
                produtos[i] = new_produto
            else:
                index = i
    if index != -1:
        produtos.pop(index)
        
    limpar_arquivo()
    for produto in produtos:
        inserir(produto)
    
def limpar_arquivo():
    with open('produtos.pkl', 'w') as arq:
        arq.write('')

def menu_inserir():
    produto = {}
    try:
        produto['name'] = input('NOME: ')
        codes = get_codes()
        produto['code'] = input('CODIGO: ')
        while produto['code'] in codes:
            print("ERRO: CODIGO EM USO")
            produto['code'] = input('CODIGO: ')
        produto['quant'] = ''
        while not produto['quant'].isdigit():
            produto['quant'] = input('Quantidade em estoque: ')
            if not produto['quant'].isdigit():
                print("Escreva um valor numerico!")
        produto['preco'] = ''
        while not produto['preco'].isdigit():
            produto['preco'] = input('PREÇO (R$): ')
            if not produto['preco'].isdigit():
                print("Escreva um valor numerico!")
        print(produto)
        inserir(produto)
        return True
    except:
        return False
    
def menu_alterar():
    listar_produtos()
    code = input('Escreva o codigo do Produto: ')
    produto = listar_produtos(code)
    codigo = produto['code']
    if produto == None:
        print("Error: Produto não encontrado.")
        return
    print(MENU_2, end='')
    opt = int(input(''))
    if opt == 1:
        produto['name'] = input('NOME: ')
    elif opt == 2:
        codes = get_codes()
        produto['code'] = input('CODIGO: ')
        while produto['code'] in codes:
            print("ERRO: CODIGO EM USO")
            produto['code'] = input('CODIGO: ')
    elif opt == 3:
        produto['quant'] = ''
        while not produto['quant'].isdigit():
            produto['quant'] = input('Quantidade em estoque: ')
            if not produto['quant'].isdigit():
                print("Escreva um valor numerico!")
    elif opt == 4:
        produto['preco'] = ''
        while not produto['preco'].isdigit():
            produto['preco'] = input('PREÇO (R$): ')
            if not produto['preco'].isdigit():
                print("Escreva um valor numerico!")
    else:
        return
    editar(produto, codigo)
    
def excluir_produto():
    codigos = get_codes()
    listar_produtos()
    code = input("Escreva o codigo do produto: ")
    if code in codigos:
        editar(None, code)
    else:
        print("Codigo não encontrado!")

def listar_produtos(codigo = ''):
    produtos = []
    try:
        print('NOME \t CODIGO \t QUANTIDADE \t PREÇO')
        with open('./produtos.pkl', 'rb') as arq:
            while True:
                try:
                    produto = pickle.load(arq)
                    if codigo == '':
                        produtos.append(produto)
                        print(f'{produto["name"]} \t\t {produto["code"]} \t\t {produto["quant"]} \t\t {produto["preco"]}')
                    elif codigo == produto['code']:
                        print(f'{produto["name"]} \t\t {produto["code"]} \t\t {produto["quant"]} \t\t {produto["preco"]}')
                        return produto
                except EOFError:
                    if len(produtos) > 0:
                        return produtos
                    else:
                        return None
    except:
        return None

def estatistica():
    produtos = listar_produtos()
    if produtos != None:
        print(f"Quantidade cadastrada = {len(produtos)}")
        eb = 0
        media = 0
        am = 0
        dp = 0
        for produto in produtos:
            if int(produto['quant']) < 20:
                eb += 1
            media = (float(produto['preco'])+media)/2
        for produto in produtos:
            dp += (float(produto['preco'])-media)**2 
            if float(produto['preco']) > media:
                am += 1
        dp = (dp/len(produtos))**(1/2)
        print(f"Quantidade de produtos com estoque baixo (<= 20): {eb} -> {(eb/len(produtos))*100}%")
        print(f"Preço medio: {media}")
        print(f"Quantidade de produtos acima da media: {am} -> {(am/len(produtos))*100}")
        print(f"Desvio padrão: {dp}")



def get_codes():
    codes = []
    try:
        with open('./produtos.pkl', 'rb') as arq:
            while True:
                try:
                    produto = pickle.load(arq)
                    codes.append(produto["code"])
                except EOFError:
                    break
        return codes
    except:
        return []

if __name__ == '__main__':
    while True:
        print(MENU, end='')
        opt = int(input(''))
        if opt == 1:
            ok = menu_inserir()
            if ok:
                print('Sucesso: O produto inserido!')
            else:
                print('ERROR: O produto não pode ser inserido!')
        elif opt == 2:
            menu_alterar()
        elif opt == 3:
            excluir_produto()
        elif opt == 4:
            limpar_arquivo()
        elif opt == 5:
            code = input('Escrava o codigo do Produto: ')
            produto = listar_produtos(code)
            if produto == None:
                print("Error: Produto não encontrado.")
            else:
                input('Aperte enter para continuar.')
        elif opt == 6:
            listar_produtos()
            input('Aperte enter para continuar.')
        elif opt == 7:
            estatistica()
        else:
            break