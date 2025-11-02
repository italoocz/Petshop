usuarios = []
PetsCadastrados = []
GastosClientes = []
Atendentes = []
Brindes = ['Boneco de pelucia', 'Adesivo Au Au Fofura', 'Mini Kit Shampoo', 'Chaveiro do seu pet', 'Sachê de molho especial', 'Coleira pequena']
Produtos = ['Tapetes Higiênicos', 'Areia para Gatos', 'Brinquedos Interativos','Camas Confortáveis', 'Comedouros e Bebedouros Automáticos','Coleiras e Guias', 'Ração de Qualidade', 'Shampoos e Produtos de Higiene', 'Antipulgas e Carrapaticidas', 'Roupinhas e Acessórios', 'Casinhas e Tocas', 'Snacks e Petiscos', 'Caixas de Transporte', 'Fonte de Água para Gatos', 'Kit de Escovação Dental']
PrecosProdutos = [50.00, 70.00, 85.00, 200.00, 60.00, 30.00, 100.00, 40.00, 250.00, 50.00, 80.00, 150.00, 50.00, 100.00, 40.00]
Servicos = ['Banho Simples', 'Tosa Higiênica', 'Tosa Completa', 'Banho + Tosa Completa (Pacote)', 'Hidratação de Pelos', 'Desembolo de Pelos', 'Escovação de Dentes', 'Corte de Unhas (Avulso)']
PrecosServicos = [60.00, 45.00, 60.00, 80.00, 50.00, 30.00, 15.00, 25.00] 
admin = [['admin', '12345']]

while True:
    print("\n===== Au Au Fofura =====")
    print('Bem vindo ao PetShop')
    print('1 - Fazer login')
    print('2 - Cadastrar usuário')
    print('3 - Cadastro de Pet')
    print('4 - Listar Usuários e Pets')
    print('0 - Sair\n')
    opcao = input('Escolha a opção: ')

    if opcao == '0': # Sair do Programa
        print('\nEncerrando o programa...\n')
        break

    elif opcao == '1': # login
        print('\nVocê já tem um login cadastrado?')
        TemCadastro = input('Digite <s> para sim ou <n> para não: ')
        if TemCadastro in ['n', 'N', 'não', 'Não']:
            print('\n=== Cadastro de Novo login ===')
            nomeLogin = input('Digite seu nome: ')
            email = input('Digite seu e-mail: ')
            idade = input('Digite sua data de nascimento [00/00/0000]: ')
            while '/' not in idade or len(idade) != 10:
                print('Data inválida ou sem ( / )')
                idade = input('Digite o formato dessa forma [00/00/0000]: ')
            data = idade.split('/')
            dia = data[0]
            mes = data[1]
            ano = data[2]

            senha = input('Crie sua senha: ')
            TemEmail = False
            for u in usuarios:
                if u[1] == email:
                    TemEmail = True
                    break
            if TemEmail:
                print('\nJá existe um usuário cadastrado com esse e-mail!')
            else:
                usuarios.append([nomeLogin, email, senha, idade])
                print('\nCadastro realizado com sucesso! Faça login agora.\n')               
        while True:
            usuario = input('Usuário (nome ou e-mail): ')
            senha = input('Senha: ')
            logado = 0
            tipo = 'cliente'

            for i in admin: # Verifica se é admin
                if i[0] == usuario and i[1] == senha:
                    logado = 1
                    tipo = 'admin'
                    break

            if logado == 0: # Verifica se é usuário comum
                for u in usuarios:
                    if (u[0] == usuario or u[1] == usuario):
                        if u[2] == senha:
                            logado = 1
                            nomeLogin = u[0]
                            break
                        else:
                            break

            if logado == 1:
                if tipo == 'admin':
                    print('\nLogin realizado como ADMIN!\n')
                else:
                    print(f'\nLogin realizado com sucesso! Bem-vindo, {nomeLogin}!\n')
                break
            else:
                print('\nUsuário não encontrado ou senha incorreta.')
                tentar = input('Deseja tentar novamente? <s/n>: ')
                if tentar.lower() != 's':
                    print('\nVoltando ao menu principal...\n')
                    break

        if logado == 1 and tipo == 'admin':
            print('1 - Cadastrar produto / serviço')
            print('2 - Alterar um produto / serviço')
            print('3 - Deletar um produto / serviço')
            print('4 - Listar produtos')
            print('5 - Listar serviços')
            print('6 - Rank de Clientes')
            print('7 - Rank de Funcionários')
            print('0 - Voltar\n')
            opcaoADM = input('Escolha a opção: ')

            if opcaoADM == '0':
                print('\nVoltando...\n')

            elif opcaoADM == '1':
                CadProduto = input('Deseja cadastrar produto ou serviço?: ')
                while CadProduto not in ['produto', 'serviço', 'Produto', 'Serviço']:
                    print('Valor inválido ')
                    CadProduto = input('Oque deseja cadastrar? (produto ou serviço): ')
                if CadProduto == 'produto':
                    NovoProduto = input('Digite o nome do novo produto: ')
                    NovoPrecoProd = float(input('Digite o novo preço do produto: '))
                    while NovoPrecoProd < 0:
                        print('Valor negativo ou inválido.')
                        NovoPrecoProd = float(input('Digite o novo preço do produto: '))
                    Produtos.append(NovoProduto)
                    PrecosProdutos.append(NovoPrecoProd)
                    print('Produto e preço cadastrados com sucesso!')
                else:
                    NovoServico = input('Digite o nome do novo serviço: ')
                    NovoPrecoServ = float(input('Digite o novo preço do serviço: '))
                    while NovoPrecoServ < 0:
                        print('Valor negativo ou inválido.')
                        NovoPrecoServ = float(input('Digite o novo preço do serviço: '))
                    Servicos.append(NovoServico)
                    PrecosServicos.append(NovoPrecoServ)
                    print('Serviço e preço cadastrados com sucesso!')

            elif opcaoADM == '2':
                alterar = input('Deseja alterar produto ou serviço?: ')
                while alterar not in ['produto', 'serviço']:
                    print('Valor inválido ')
                    alterar = input('Oque deseja alterar? (produto ou serviço): ')
                if alterar == 'produto':
                    for indice in range(len(Produtos)):
                        print(f'{indice} - {Produtos[indice]} | R$ {PrecosProdutos[indice]}')
                    indice = int(input('\nDigite o índice do produto que deseja alterar: '))

                    while indice < 0 or indice >= len(Produtos): 
                        print('Indice negativo ou inválido! Digite um índice que tenha na lista.')
                        indice = int(input('Digite novamente: '))
                    NovoNomeProd = input('Digite o novo nome do produto: ')
                    PrecoProdAlt = float(input('Digite o novo preço do produto: '))
                    while PrecoProdAlt < 0:
                        print('Valor negativo ou inválido.')
                        PrecoProdAlt = float(input('Digite o novo preço do produto: '))
                    Produtos[indice] = NovoNomeProd
                    PrecosProdutos[indice] = PrecoProdAlt
                else:
                    for indice in range(len(Servicos)):
                        print(f'{indice} - {Servicos[indice]} | R$ {PrecosServicos[indice]}')
                    indice = int(input('\nDigite o índice do produto que deseja alterar: '))

                    while indice < 0 or indice >= len(Servicos): 
                        print('Indice negativo ou inválido! Digite um índice que tenha na lista.')
                        indice = int(input('Digite novamente: '))
                    NovoNomeServ = input('Digite o novo nome do serviço: ')
                    PrecoServAlt = float(input('Digite o novo preço do serviço: '))
                    while PrecoServAlt < 0:
                        print('Valor negativo ou inválido.')
                        PrecoServAlt = float(input('Digite o novo preço do serviço: '))
                    Servicos[indice] = NovoNomeServ
                    PrecosServicos[indice] = PrecoServAlt

            elif opcaoADM == '3':
                deletar = input('Deseja deletar um produto ou serviço?: ')
                while deletar not in ['produto', 'serviço', 'Produto', 'Serviço']:
                    print('Valor inválido ')
                    deletar = input('Oque deseja deletar? (produto ou serviço): ')
                if deletar == 'produto':
                    for indice in range(len(Produtos)):
                        print(f'{indice} - {Produtos[indice]} | R$ {PrecosProdutos[indice]}')
                    indice = int(input('\nDigite o índice do produto que deseja alterar: '))

                    while indice < 0 or indice >= len(Produtos): 
                        print('Indice negativo ou inválido! Digite um índice que tenha na lista.')
                        indice = int(input('Digite novamente: '))
                    ProdRemovido = Produtos[indice]
                    Produtos.pop(indice)
                    PrecosProdutos.pop(indice)
                    print(f'\nProduto {ProdRemovido} removido com sucesso!')
                else:
                    for indice in range(len(Servicos)):
                        print(f'{indice} - {Servicos[indice]} | R$ {PrecosServicos[indice]}')
                    indice = int(input('\nDigite o índice do serviço que deseja alterar: '))

                    while indice < 0 or indice >= len(Servicos): 
                        print('Indice negativo ou inválido! Digite um índice que tenha na lista.')
                        indice = int(input('Digite novamente: '))
                    ServRemovido = Servicos[indice]
                    Servicos.pop(indice)
                    PrecosServicos.pop(indice)
                    print(f'\nServiço {ServRemovido} removido com sucesso!')

            elif opcaoADM == '4':
                print('\nListando Produtos...\n')
                for indice in range(len(Produtos)):
                        print(f'{indice} - {Produtos[indice]} | R$ {PrecosProdutos[indice]}')

            elif opcaoADM == '5':
                print('\nListando Serviços...\n')
                for indice in range(len(Servicos)):
                        print(f'{indice} - {Servicos[indice]} | R$ {PrecosServicos[indice]}')
            
            elif opcaoADM == '6':
                print('\n=== Rank de Clientes ===\n')
                if len(GastosClientes) == 0:
                    print('Nenhuma compra registrada ainda.\n')
                else:
                    for i in range(len(GastosClientes)):
                        for j in range(i + 1, len(GastosClientes)):
                            if GastosClientes[j][1] > GastosClientes[i][1]:
                                troca = GastosClientes[i]
                                GastosClientes[i] = GastosClientes[j]
                                GastosClientes[j] = troca

                    posicao = 1
                    for cliente in GastosClientes:
                        print(str(posicao) + 'º - ' + cliente[0] + ' | Total gasto: R$ ' + str(cliente[1]))
                        posicao += 1
            
            elif opcaoADM == '7':
                print('\n=== Rank de Funcionários ===\n')
                if len(Atendentes) == 0:
                    print('Nenhum atendimento registrado ainda.\n')
                else:
                    for i in range(len(Atendentes)):
                        for j in range(i + 1, len(Atendentes)):
                            if Atendentes[j][1] > Atendentes[i][1]:
                                troca = Atendentes[i]
                                Atendentes[i] = Atendentes[j]
                                Atendentes[j] = troca

                    posicao = 1
                    for func in Atendentes:
                        print(str(posicao) + 'º - ' + func[0] + ' | Atendimentos: ' + str(func[1]))
                        posicao += 1


        if logado == 1 and tipo == 'cliente':
            print('1 - Comprar produtos')
            print('2 - Agendamentos')
            print('0 - Voltar\n')
            opcaoCliente = input('Escolha a opção: ')
            if opcaoCliente == '0':
                print('\nVoltando...\n')
            elif opcaoCliente == '1': # Comprando Produtos
                sacola = []
                soma = 0
                while True:
                    print('\n--- Produtos Disponíveis ---')
                    for indice in range(len(Produtos)):
                        print(f'{indice} - {Produtos[indice]} | R$ {PrecosProdutos[indice]}')
                    indice = int(input('\nDigite o índice do produto que deseja comprar: '))

                    while indice < 0 or indice >= len(Produtos): 
                        print('Indice negativo ou inválido! Digite um índice que tenha na lista.')
                        indice = int(input('Digite novamente: '))
                    sacola.append([Produtos[indice], PrecosProdutos[indice]]) # Adiciona o produto e preço na sacola
                    soma += PrecosProdutos[indice]
                    print(f'\nVocê adicionou {Produtos[indice]} por R$ {PrecosProdutos[indice]}')
                    print(f'Valor total: R$ {soma}')
                    continuar = input('\nDeseja comprar algo mais? <s/n>: ')
                    if continuar not in ['s', 'sim', 'S', 'Sim']:
                        break
                print('\n--- Sacola atual ---')
                for i in range(len(sacola)):
                    print(f'{i} - {sacola[i][0]} | R$ {sacola[i][1]}')
                print(f'\nTotal da compra: R$ {soma}')
                RemoverSaco = input('\nDeseja remover algum item da sacola? <s/n>: ')
                while RemoverSaco in ['s', 'sim', 'S', 'Sim']:
                    for i in range(len(sacola)):
                        print(f'{i} - {sacola[i][0]} | R$ {sacola[i][1]}')
                    indice = int(input('\nDigite o índice do produto que deseja remover: '))
                    while indice < 0 or indice >= len(sacola):
                        print('Indice inválido!')
                        indice = int(input('Digite novamente: '))

                    print(f'\nItem {sacola[indice][0]} removido!')# Remove o item e atualiza o valor total
                    soma -= sacola[indice][1]
                    sacola.pop(indice)
                    print(f'\nNovo valor total: R$ {soma}')
                    RemoverSaco = input('\nDeseja remover mais algum item? <s/n>: ')

                print('\n--- Pagamento ---')
                print(f'Nome do cliente: {nomeLogin} | E-mail: {email} | Idade: {idade}')
                for i in range(len(sacola)):
                    print(f'{sacola[i][0]} | R$ {sacola[i][1]}')
                if soma > 250: # Desconto
                    print('\nParabens! Por sua compra ultrapassar o valor de R$ 250,00 você ganhou um desconto de 15%')
                    desconto = soma * 0.15
                    soma = soma - desconto
                print(f'\nValor total a pagar: R$ {soma}')
                formaPag = input('Qual vai ser a forma de pagamento? <Dinheiro ou Pix>: ')
                atendenteNome = input('Digite o nome do atendente que realizou o atendimento: ')
                atende = False
                for f in Atendentes:
                    if f[0] == atendenteNome:
                        f[1] = f[1] + 1
                        atende = True
                        break
                if not atende:
                    Atendentes.append([atendenteNome, 1])
                print('\nCompra finalizada! Obrigado por comprar na Au Au Fofura <3\n')
                if soma >= 200:
                    print('\nParabéns! Você ganhou um brinde especial da Au Au Fofura!')
                    print('Brindes disponíveis:')
                    for i in range(len(Brindes)):
                        print(f'{i + 1} - {Brindes[i]}')
                    indice = input('Escolha o número do brinde que deseja: ')
                    while indice < '1' or indice > str(len(Brindes)):
                        print('Opção inválida!')
                        indice = input('Escolha o número do brinde que deseja: ')
                    print(f'\nVocê escolheu o brinde: {Brindes[int(indice) - 1]} \n')
                else:
                    print('\nContinue comprando para ganhar brindes especiais \n')
                achou = False
                for g in GastosClientes:
                    if g[0] == nomeLogin:
                        g[1] = g[1] + soma # soma o valor da nova compra
                        achou = True
                        break
                if not achou:
                    GastosClientes.append([nomeLogin, soma]) 
            
            elif opcaoCliente == '2':
                Agendamentos = []
                soma = 0
                while True:
                    print('\n--- Agendamentos Disponíveis ---')
                    for indice in range(len(Servicos)):
                        print(f'{indice} - {Servicos[indice]} | R$ {PrecosServicos[indice]}')
                    indice = int(input('\nDigite o índice do tipo de agendamento que deseja: '))

                    while indice < 0 or indice >= len(Servicos): 
                        print('Indice negativo ou inválido! Digite um índice que tenha na lista.')
                        indice = int(input('Digite novamente: '))

                    Agendamentos.append([Servicos[indice], PrecosServicos[indice]]) # Adiciona o produto e preço na sacola
                    soma += PrecosServicos[indice]
                    print(f'\nVocê agendou {Servicos[indice]} por R$ {PrecosServicos[indice]}')
                    print(f'Valor total: R$ {soma}')
                    continuar = input('\nDeseja agendar algo mais? <s/n>: ')
                    if continuar not in ['s', 'sim', 'S', 'Sim']:
                        break
                print('\n--- Agendamento atual ---')
                for i in range(len(Agendamentos)):
                    print(f'{i} - {Agendamentos[i][0]} | R$ {Agendamentos[i][1]}')
                print(f'\nTotal da compra: R$ {soma}')
                RemoverAge = input('\nDeseja remover algum tipo de agendamento? <s/n>: ')
                while RemoverAge in ['s', 'sim', 'S', 'Sim']:
                    for i in range(len(Agendamentos)):
                        print(f'{i} - {Agendamentos[i][0]} | R$ {Agendamentos[i][1]}')
                    indice = int(input('\nDigite o índice do agendamento que deseja remover: '))
                    while indice < 0 or indice >= len(Agendamentos):
                        print('Indice inválido!')
                        indice = int(input('Digite novamente: '))

                    print(f'\nTipo {Agendamentos[indice][0]} removido!')# Remove o agendamento e atualiza o valor total
                    soma -= Agendamentos[indice][1]
                    Agendamentos.pop(indice)
                    print(f'\nNovo valor total: R$ {soma}')
                    RemoverAge = input('\nDeseja remover mais algum agendamento? <s/n>: ')

                print('\n--- Pagamento ---')
                print(f'Nome do cliente: {nomeLogin} | E-mail: {email} | Idade: {idade}')
                for i in range(len(Agendamentos)):
                    print(f'{Agendamentos[i][0]} | R$ {Agendamentos[i][1]}')
                if soma > 250: # Desconto
                    print('\nParabens! Por seu agendamento ultrapassar o valor de R$ 250,00 você ganhou um desconto de 20%')
                    desconto = soma * 0.20
                    soma = soma - desconto
                print(f'\nValor total a pagar: R$ {soma}')
                formaPag = input('Qual vai ser a forma de pagamento? <Dinheiro ou Pix>: ') # Desconto
                atendenteNome = input('Digite o nome do atendente que realizou o atendimento: ')
                atende = False
                for f in Atendentes:
                    if f[0] == atendenteNome:
                        f[1] = f[1] + 1
                        atende = True
                        break
                if not atende:
                    Atendentes.append([atendenteNome, 1])
                print('\nAgendamento finalizado! Obrigado por agendar na Au Au Fofura <3\n')
                if soma >= 200:
                    print('\nParabéns! Você ganhou um brinde especial da Au Au Fofura!')
                    print('Brindes disponíveis:')
                    for i in range(len(Brindes)):
                        print(f'{i + 1} - {Brindes[i]}')
                    indice = input('Escolha o número do brinde que deseja: ')
                    while indice < '1' or indice > str(len(Brindes)):
                        print('Opção inválida!')
                        indice = input('Escolha o número do brinde que deseja: ')
                    print(f'\nVocê escolheu o brinde: {Brindes[int(indice) - 1]} \n')
                else:
                    print('\nContinue comprando para ganhar brindes especiais \n')
                gastos = False
                for g in GastosClientes:
                    if g[0] == nomeLogin:
                        g[1] = g[1] + soma
                        gastos = True
                        break
                if not gastos:
                    GastosClientes.append([nomeLogin, soma]) 


    elif opcao == '2': # Cadastro de usuário
        print('\nCadastro de Usuário.\n')
        nomeLogin = input('Digite seu nome: ')
        email = input('Digite seu e-mail: ')
        idade = input('Digite sua data de nascimento [00/00/0000]: ')
        while '/' not in idade or len(idade) != 10:
            print('Data inválida ou sem ( / )')
            idade = input('Digite o formato dessa forma [00/00/0000]: ')
        data = idade.split('/')
        dia = data[0]
        mes = data[1]
        ano = data[2]
        senha = input('Crie uma senha: ')

        verifica = False
        for u in usuarios:
            if u[1] == email:
                verifica = True
                break
                
        if verifica:
            print('\nJá existe um usuário com esse e-mail!\n')
        else:
            usuarios.append([nomeLogin, email, senha, idade])
            print('\nUsuário cadastrado com sucesso!\n')

    elif opcao == '3': # Cadastro de Pet
        print('\nCadastro de Pet:\n')

        if len(usuarios) == 0:
            print('Nenhum usuário cadastrado! Cadastre um usuário antes de registrar um pet.\n')
        else:
            print('\nUsuários cadastrados:')
            for i in range(len(usuarios)):
                print(f'{i} - {usuarios[i][0]} ({usuarios[i][1]})')

            donoPet = int(input('\nDigite o número do dono do pet: '))
            while donoPet < 0 or donoPet >= len(usuarios):
                print('Número inválido!')
                donoPet = int(input('Digite novamente o número do dono do pet: '))

            nomeDono = usuarios[donoPet][0]
            nomePet = input('Qual o nome do seu Pet?: ')
            sexoPet = input('Qual o sexo do seu Pet? <f/m> : ')
            while sexoPet not in ['m', 'M', 'f', 'F']:
                print('Valor inválido ')
                sexoPet = input('Digite < f ou m >: ')
            if sexoPet == 'm' or sexoPet == 'M':
                sexoPet = 'Masculino'
            else:
                sexoPet = 'Feminino'
            idadePet = int(input('Digite quantos anos tem seu Pet: '))
            while idadePet > 30 or idadePet < 0:
                print('Idade negativa ou inválida!')
                idadePet = int(input('Digite quantos anos tem seu Pet: '))
            quilosPet = float(input('Digite quantos quilos tem seu Pet: '))
            while quilosPet > 155 or quilosPet < 0:
                print('Peso negativo ou inválio!')
                quilosPet = float(input('Digite quantos quilos tem seu Pet: '))
            PetsCadastrados.append([nomePet, sexoPet, idadePet, quilosPet, nomeDono])
            print(f'\nPet cadastrado com sucesso para o dono: {nomeDono}!\n')

    elif opcao == '4': # Listar Usuários e Pets
        print('\nLista de usuários e pets\n')
        for list in usuarios:
            print(f'Nome: {list[0]} | E-mail: {list[1]} | Idade: {list[3]}')
        if len(PetsCadastrados) == 0:
            print('\nNenhum pet cadastrado ainda.\n')
        else:
            print('\nPets Cadastrados:\n')
            for pets in PetsCadastrados:
                print(f'Nome do pet: {pets[0]} | Sexo: {pets[1]} | Idade: {pets[2]} Anos | Peso: {pets[3]} Kg | Dono: {pets[4]}')

    
    else:
        print('\nPrograma falhou, escolha a opção correta!\n')