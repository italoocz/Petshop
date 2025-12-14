import produtos
import servicos
import usuarios

def backup_produtos():
    with open('backup_produtos.txt', 'w', encoding='utf-8') as arq:
        for p in produtos.produtos:
            arq.write(f"{p['nome']};{p['preco']}\n")

def backup_servicos():
    with open('backup_servicos.txt', 'w', encoding='utf-8') as arq:
        for s in servicos.servicos:
            arq.write(f"{s['nome']};{s['preco']}\n")

def backup_usuarios():
    with open('backup_usuarios.txt', 'w', encoding='utf-8') as arq:
        for u in usuarios.usuarios:
            arq.write(f"{u['nome']};{u['email']};{u['data']}\n")

def backup_completo():
    backup_produtos()
    backup_servicos()
    backup_usuarios()
    print('\nBackup geral realizado com sucesso!')

def importar_produtos():
    produtos.produtos.clear()

    with open('backup_produtos.txt', 'r', encoding='utf-8') as arq:
        for linha in arq.readlines():
            nome, preco = linha.strip().split(';')
            produtos.produtos.append({
                'nome': nome,
                'preco': float(preco)
            })

def importar_servicos():
    servicos.servicos.clear()

    with open('backup_servicos.txt', 'r', encoding='utf-8') as arq:
        for linha in arq.readlines():
            nome, preco = linha.strip().split(';')
            servicos.servicos.append({
                'nome': nome,
                'preco': float(preco)
            })

def importar_usuarios():
    usuarios.usuarios.clear()

    with open('backup_usuarios.txt', 'r', encoding='utf-8') as arq:
        for linha in arq.readlines():
            nome, email, data = linha.strip().split(';')
            usuarios.usuarios.append({
                'nome': nome,
                'email': email,
                'data': data
            })

def importar_backup():
    importar_produtos()
    importar_servicos()
    importar_usuarios()
    print('\nDados importados com sucesso!')

