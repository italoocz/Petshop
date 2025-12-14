import produtos
import servicos
import matplotlib.pyplot as plt

usuarios = [
    {
        'nome': 'usuario',
        'email': 'usuario@gmail.com',
        'senha': '12345',
        'data': '20/11/2004'
    }
]
admin = [
    {
    'login': 'admin',
    'senha': '12345'
    }
]

petsCadastrados = []

GastosClientes = []

Atendentes = []

Brindes = ['Boneco de pelucia', 'Adesivo Au Au Fofura', 'Mini Kit Shampoo', 'Chaveiro do seu pet', 'Sachê de molho especial', 'Coleira pequena']

def cadastrar_usuario():
    print('\nVocê já tem um login cadastrado?')
    TemCadastro = input('Digite <s> para sim ou <n> para não: ')

    if TemCadastro in ['n', 'N', 'não', 'Não']:
        print('\n=== Cadastro de Novo Login ===')
        TipoCadastro = input('Você quer cadastrar um <cliente> ou <admin>? : ')

        while TipoCadastro not in ['cliente', 'admin']:
            print('Tipo inválido! Digite apenas "cliente" ou "admin".')
            TipoCadastro = input('Você quer cadastrar um <cliente> ou <admin>? : ')

        # ===== CADASTRO CLIENTE =====
        if TipoCadastro == 'cliente':
            nome = input('Digite seu nome: ')

            email = input('Digite seu e-mail: ')
            while '@' not in email:
                print('Email inválido! Coloque um "@"')
                email = input('Digite seu e-mail: ')

            # Verifica email repetido
            for u in usuarios:
                if u['email'] == email:
                    print('\nJá existe um usuário cadastrado com esse e-mail!')
                    return None, None

            idade = input('Digite sua data de nascimento [00/00/0000]: ')
            while '/' not in idade or len(idade) != 10:
                print('\nData inválida!')
                idade = input('Digite sua data de nascimento [00/00/0000]: ')

            data = idade.split('/')
            dia = int(data[0])
            mes = int(data[1])
            ano = int(data[2])

            while dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1900 or ano > 2025:
                print('\nDia, mês ou ano inválidos!')
                idade = input('Digite sua data de nascimento [00/00/0000]: ')
                data = idade.split('/')
                dia = int(data[0])
                mes = int(data[1])
                ano = int(data[2])

            senha = input('Crie sua senha: ')
            while len(senha) < 4:
                print('Senha inválida, digite com mais caracteres!')
                senha = input('Crie sua senha: ')

            usuarios.append({
                'nome': nome,
                'email': email,
                'senha': senha,
                'data': idade
            })

            print('\nCadastro realizado com sucesso! Faça login agora.\n')

        # ===== CADASTRO ADMIN =====
        else:
            nomeAdmin = input('Digite o nome do administrador: ')
            senhaAdmin = input('Crie sua senha: ')

            while len(senhaAdmin) < 4:
                print('Senha inválida, digite com mais caracteres!')
                senhaAdmin = input('Crie sua senha: ')

            for a in admin:
                if a['login'] == nomeAdmin:
                    print('\nJá existe um administrador com esse nome!')
                    return

            admin.append({
                'login': nomeAdmin,
                'senha': senhaAdmin
            })

            print('\nAdministrador cadastrado com sucesso! Faça login agora.\n')

def login():
    usuario = input('Login (nome ou email): ')
    senha = input('Senha: ')

    for a in admin:
        if a['login'] == usuario and a['senha'] == senha:
            return 'admin', usuario

    for u in usuarios:
        if (u['nome'] == usuario or u['email'] == usuario) and u['senha'] == senha:
            return 'cliente', u

    print('Login inválido!')
    return

def cadastrar_pet():
    print('\n=== Cadastro de Pet ===\n')

    if len(usuarios) == 0:
        print('Nenhum usuário cadastrado! Cadastre um usuário antes.\n')
        return

    print('Usuários cadastrados:')
    for i in range(len(usuarios)):
        print(f"{i} - {usuarios[i]['nome']} ({usuarios[i]['email']})")

    donoPet = int(input('\nDigite o número do dono do pet: '))
    while donoPet < 0 or donoPet >= len(usuarios):
        print('Número inválido!')
        donoPet = int(input('Digite novamente o número do dono do pet: '))

    nomeDono = usuarios[donoPet]['nome']

    nomePet = input('Nome do pet: ')

    sexoPet = input('Sexo do pet <f/m>: ')
    while sexoPet not in ['f', 'F', 'm', 'M']:
        print('Valor inválido!')
        sexoPet = input('Sexo do pet <f/m>: ')

    if sexoPet in ['m', 'M']:
        sexoPet = 'Masculino'
    else:
        sexoPet = 'Feminino'

    idadePet = int(input('Idade do pet (anos): '))
    while idadePet < 0 or idadePet > 30:
        print('Idade inválida!')
        idadePet = int(input('Idade do pet (anos): '))

    pesoPet = float(input('Peso do pet (kg): '))
    while pesoPet < 0 or pesoPet > 155:
        print('Peso inválido!')
        pesoPet = float(input('Peso do pet (kg): '))

    petsCadastrados.append({
        'nome': nomePet,
        'sexo': sexoPet,
        'idade': idadePet,
        'peso': pesoPet,
        'dono': nomeDono
    })

    print(f'\nPet cadastrado com sucesso para o dono {nomeDono}!\n')

def listar_Pets_Users():
    print('\n--- Lista de usuários e pets ---\n')

    for u in usuarios:
        print(f"Nome: {u['nome']} | E-mail: {u['email']} | Data de nascimento: {u['data']}")

    if len(petsCadastrados) == 0:
        print('\n--- Nenhum pet cadastrado ainda ---\n')
    else:
        print('\n--- Pets Cadastrados ---\n')
        for p in petsCadastrados:
            print(
                f"Nome do pet: {p['nome']} | "
                f"Sexo: {p['sexo']} | "
                f"Idade: {p['idade']} anos | "
                f"Peso: {p['peso']} kg | "
                f"Dono: {p['dono']}"
            )

    print('\n--- Lista de Admins ---\n')
    for a in admin:
        print(f"Nome do administrador: {a['login']}")



def atualizar_gastos(nome, valor):
    for g in GastosClientes:
        if g['nome'] == nome:
            g['total'] += valor
            return

    GastosClientes.append({
        'nome': nome,
        'total': valor
    })

def atualizar_atendente(nome):
    for a in Atendentes:
        if a['nome'] == nome:
            a['qtd'] += 1
            return

    Atendentes.append({
        'nome': nome,
        'qtd': 1
    })

# adm options

def cadastrar_prod_serv():
    cadastrar = input('Deseja cadastrar produto ou serviço?: ').lower()

    while cadastrar not in ['produto', 'serviço', 'servico']:
        print('Valor inválido!')
        cadastrar = input('O que deseja cadastrar? (produto ou serviço): ').lower()

    # ===== CADASTRAR PRODUTO =====
    if cadastrar == 'produto':
        nome = input('Digite o nome do novo produto: ')
        preco = float(input('Digite o preço do produto: '))
        while preco < 0:
            print('Preço inválido!')
            preco = float(input('Digite o preço do produto: '))

        produtos.produtos.append({
            'nome': nome,
            'preco': preco
        })

        print('\nProduto cadastrado com sucesso!\n')

    # ===== CADASTRAR SERVIÇO =====
    else:
        nome = input('Digite o nome do novo serviço: ')
        preco = float(input('Digite o preço do serviço: '))
        while preco < 0:
            print('Preço inválido!')
            preco = float(input('Digite o preço do serviço: '))

        servicos.servicos.append({
            'nome': nome,
            'preco': preco
        })  

        print('\nServiço cadastrado com sucesso!\n')



def alterar_prod_serv():
    alterar = input('Deseja alterar produto ou serviço?: ').lower()

    while alterar not in ['produto', 'serviço', 'servico']:
        print('Valor inválido!')
        alterar = input('O que deseja alterar? (produto ou serviço): ').lower()

    # ===== ALTERAR PRODUTO =====
    if alterar == 'produto':
        if len(produtos.produtos) == 0:
            print('\nNenhum produto cadastrado!\n')
        else:
            print('\n--- Produtos Cadastrados ---')
            for i in range(len(produtos.produtos)):
                print(f"{i} - {produtos.produtos[i]['nome']} | R$ {produtos.produtos[i]['preco']}")

            indice = int(input('\nDigite o índice do produto que deseja alterar: '))
            while indice < 0 or indice >= len(produtos.produtos):
                print('Índice inválido!')
                indice = int(input('Digite novamente: '))

            novo_nome = input('Digite o novo nome do produto: ')
            novo_preco = float(input('Digite o novo preço do produto: '))
            while novo_preco < 0:
                print('Preço inválido!')
                novo_preco = float(input('Digite o novo preço do produto: '))

            produtos.produtos[indice]['nome'] = novo_nome
            produtos.produtos[indice]['preco'] = novo_preco

            print('\nProduto alterado com sucesso!\n')

    # ===== ALTERAR SERVIÇO =====
    else:
        if len(servicos.servicos) == 0:
            print('\nNenhum serviço cadastrado!\n')
        else:
            print('\n--- Serviços Cadastrados ---')
            for i in range(len(servicos.servicos)):
                print(f"{i} - {servicos.servicos[i]['nome']} | R$ {servicos.servicos[i]['preco']}")

            indice = int(input('\nDigite o índice do serviço que deseja alterar: '))
            while indice < 0 or indice >= len(servicos.servicos):
                print('Índice inválido!')
                indice = int(input('Digite novamente: '))

            novo_nome = input('Digite o novo nome do serviço: ')
            novo_preco = float(input('Digite o novo preço do serviço: '))
            while novo_preco < 0:
                print('Preço inválido!')
                novo_preco = float(input('Digite o novo preço do serviço: '))

            servicos.servicos[indice]['nome'] = novo_nome
            servicos.servicos[indice]['preco'] = novo_preco

            print('\nServiço alterado com sucesso!\n')



def deletar_prod_serv():
    deletar = input('Deseja deletar um produto ou serviço? ').lower()

    while deletar not in ['produto', 'serviço', 'servico']:
        print('Valor inválido!')
        deletar = input('O que deseja deletar? (produto ou serviço): ').lower()

    # ===== REMOVER PRODUTO =====
    if deletar == 'produto':
        if len(produtos.produtos) == 0:
            print('\nNenhum produto cadastrado!\n')
        else:
            print('\n--- Produtos Cadastrados ---')
            for i in range(len(produtos.produtos)):
                print(f"{i} - {produtos.produtos[i]['nome']} | R$ {produtos.produtos[i]['preco']}")

            indice = int(input('\nDigite o índice do produto que deseja remover: '))
            while indice < 0 or indice >= len(produtos.produtos):
                print('Índice inválido!')
                indice = int(input('Digite novamente: '))

            removido = produtos.produtos[indice]['nome']
            produtos.produtos.pop(indice)

            print(f'\nProduto "{removido}" removido com sucesso!\n')

    # ===== REMOVER SERVIÇO =====
    else:
        if len(servicos.servicos) == 0:
            print('\nNenhum serviço cadastrado!\n')
        else:
            print('\n--- Serviços Cadastrados ---')
            for i in range(len(servicos.servicos)):
                print(f"{i} - {servicos.servicos[i]['nome']} | R$ {servicos.servicos[i]['preco']}")

            indice = int(input('\nDigite o índice do serviço que deseja remover: '))
            while indice < 0 or indice >= len(servicos.servicos):
                print('Índice inválido!')
                indice = int(input('Digite novamente: '))

            removido = servicos.servicos[indice]['nome']
            servicos.servicos.pop(indice)

            print(f'\nServiço "{removido}" removido com sucesso!\n')



def mostrar_rank_clientes():
    print('\n--- Ranking de Clientes ---')
    posicao = 1
    for c in GastosClientes:
        print(str(posicao) + 'º - ' + c['nome'] + ' | Total: R$ ' + str(c['total']))
        posicao += 1

def mostrar_rank_atendentes():
    print('\n--- Ranking de Atendentes ---')
    posicao = 1
    for a in Atendentes:
        print(str(posicao) + 'º - ' + a['nome'] + ' | Atendimentos: ' + str(a['qtd']))
        posicao += 1


def grafico_prod_serv():
    # ===== 5 Produtos mais caros =====
    produtos_ordenados = sorted(produtos.produtos, key=lambda x: x['preco'], reverse=True)[:5]
    nomes_prod = [p['nome'] for p in produtos_ordenados]
    precos_prod = [p['preco'] for p in produtos_ordenados]

    # ===== 5 Serviços mais caros =====
    servicos_ordenados = sorted(servicos.servicos, key=lambda x: x['preco'], reverse=True)[:5]
    nomes_serv = [s['nome'] for s in servicos_ordenados]
    precos_serv = [s['preco'] for s in servicos_ordenados]

    # ===== gráfico =====
    plt.figure(figsize=(12, 6))

    # Produtos
    plt.bar(nomes_prod, precos_prod, color='blue', label='Produtos')
    # Serviços
    plt.bar(nomes_serv, precos_serv, color='red', alpha=0.7, label='Serviços')

    plt.title('Top 5 Produtos e Serviços Mais Caros')
    plt.ylabel('Preço (R$)')
    plt.xticks(rotation=20, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.show()