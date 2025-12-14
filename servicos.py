servicos = [
    {"nome": "Vacinação", "preco": 80.00},
    {"nome": "Banho Simples", "preco": 60.00},
    {"nome": "Tosa Higiênica", "preco": 45.00},
    {"nome": "Tosa Completa", "preco": 60.00},
    {"nome": "Banho + Tosa Completa (Pacote)", "preco": 80.00},
    {"nome": "Hidratação de Pelos", "preco": 50.00},
    {"nome": "Desembolo de Pelos", "preco": 30.00},
    {"nome": "Escovação de Dentes", "preco": 15.00},
    {"nome": "Corte de Unhas (Avulso)", "preco": 25.00}
]

def listar_servicos():
    for i in range(len(servicos)):
        print(f"{i} - {servicos[i]['nome']} | R$ {servicos[i]['preco']}")

def buscar_servico(nome_servico):
    for servico in servicos:
        if nome_servico.lower() in servico['nome'].lower():
            return servico
    return None

def adicionar_servico(nome_servico, preco_servico):
    servicos.append({
        "nome": nome_servico,
        "preco": preco_servico
    })

def atualizar_preco_servico(nome_servico, novo_preco):
    for servico in servicos:
        if servico['nome'].lower() == nome_servico.lower():
            servico['preco'] = novo_preco
            return True
    return False

def remover_servico(nome_servico):
    for i in range(len(servicos)):
        if servicos[i]['nome'].lower() == nome_servico.lower():
            servicos.pop(i)
            return True
    return False