produtos = [
    {"nome": "Vacina", "preco": 60.00},
    {"nome": "Tapetes Higiênicos", "preco": 50.00},
    {"nome": "Areia para Gatos", "preco": 70.00},
    {"nome": "Brinquedos Interativos", "preco": 85.00},
    {"nome": "Camas Confortáveis", "preco": 200.00},
    {"nome": "Comedouros e Bebedouros Automáticos", "preco": 60.00},
    {"nome": "Coleiras e Guias", "preco": 30.00},
    {"nome": "Ração de Qualidade", "preco": 100.00},
    {"nome": "Shampoos e Produtos de Higiene", "preco": 40.00},
    {"nome": "Antipulgas e Carrapaticidas", "preco": 250.00},
    {"nome": "Roupinhas e Acessórios", "preco": 50.00},
    {"nome": "Casinhas e Tocas", "preco": 80.00},
    {"nome": "Snacks e Petiscos", "preco": 150.00},
    {"nome": "Caixas de Transporte", "preco": 50.00},
    {"nome": "Fonte de Água para Gatos", "preco": 100.00},
    {"nome": "Kit de Escovação Dental", "preco": 40.00}
]

def listar_produtos():
    for i in range(len(produtos)):
        print(str(i) + " - " + produtos[i]["nome"] + " | R$ " + str(produtos[i]["preco"])
        )

def buscar_produto(nome_produto):
    for produto in produtos:
        if nome_produto.lower() in produto['nome'].lower():
            return produto
    return None

def atualizar_preco(nome_produto, novo_preco):
    for produto in produtos:
        if nome_produto.lower() == produto['nome'].lower():
            produto['preco'] = novo_preco
            return produto
    return None

def adicionar_produto(nome_produto, preco_produto):
    produtos.append({"nome": nome_produto, "preco": preco_produto})