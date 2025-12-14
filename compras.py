import produtos
import servicos
from usuarios import Atendentes, Brindes, GastosClientes


def menu_cliente(UsuarioConectado):
    while True:
        print('\n--- Menu do Cliente ---')
        print('1 - Comprar produtos')
        print('2 - Agendar serviços')
        print('0 - Voltar')

        opcaoCliente = input('Escolha a opção: ')

        if opcaoCliente == '1':
            comprar_produtos(UsuarioConectado)

        elif opcaoCliente == '2':
            agendar_servicos(UsuarioConectado)

        elif opcaoCliente == '0':
            print('\nVoltando...\n')
            break

        else:
            print('Opção inválida!')


def comprar_produtos(UsuarioConectado):
    sacola = []
    soma = 0

    while True:
        print('\n--- Produtos Disponíveis ---')
        for i in range(len(produtos.produtos)):
            print(f"{i} - {produtos.produtos[i]['nome']} | R$ {produtos.produtos[i]['preco']}")

        indice = int(input('\nDigite o índice do produto que deseja comprar: '))
        while indice < 0 or indice >= len(produtos.produtos):
            print('Índice inválido!')
            indice = int(input('Digite novamente: '))

        sacola.append(produtos.produtos[indice])
        soma += produtos.produtos[indice]['preco']

        print(f"\nVocê adicionou {produtos.produtos[indice]['nome']} por R$ {produtos.produtos[indice]['preco']}")
        print(f"Valor total: R$ {soma}")

        continuar = input('\nDeseja comprar algo mais? <s/n>: ')
        if continuar.lower() not in ['s', 'sim']:
            break

    # ===== SACOLA =====
    print('\n--- Sacola atual ---')
    for i in range(len(sacola)):
        print(f"{i} - {sacola[i]['nome']} | R$ {sacola[i]['preco']}")

    print(f'\nTotal da compra: R$ {soma}')

    remover = input('\nDeseja remover algum item da sacola? <s/n>: ')
    while remover.lower() in ['s', 'sim'] and len(sacola) > 0:
        indice = int(input('Digite o índice do produto que deseja remover: '))
        while indice < 0 or indice >= len(sacola):
            print('Índice inválido!')
            indice = int(input('Digite novamente: '))

        soma -= sacola[indice]['preco']
        print(f"\nItem {sacola[indice]['nome']} removido!")
        sacola.pop(indice)
        print(f'Novo valor total: R$ {soma}')

        remover = input('\nDeseja remover mais algum item? <s/n>: ')

    # ===== PAGAMENTO =====
    print('\n--- Pagamento ---')
    print(f"Cliente: {UsuarioConectado['nome']} | Email: {UsuarioConectado['email']} | Nascimento: {UsuarioConectado['data']}")

    if soma > 250:
        print('\nParabéns! Você ganhou 15% de desconto')
        soma = soma * 0.85

    print(f'\nValor total a pagar: R$ {soma}')
    formaPag = input('Forma de pagamento <Dinheiro ou Pix>: ')

    # ===== ATENDENTE =====
    atendenteNome = input('Nome do atendente: ')
    achou = False

    for a in Atendentes:
        if a['nome'] == atendenteNome:
            a['qtd'] += 1
            achou = True
            break

    if not achou:
        Atendentes.append({
            'nome': atendenteNome,
            'qtd': 1
        })

    print('\nCompra finalizada! Obrigado por comprar na Au Au Fofura ')

    # ===== BRINDE =====
    if soma >= 200:
        print('\nVocê ganhou um brinde!')
        for i in range(len(Brindes)):
            print(f'{i + 1} - {Brindes[i]}')

        escolha = int(input('Escolha o número do brinde: '))
        while escolha < 1 or escolha > len(Brindes):
            print('Opção inválida!')
            escolha = int(input('Escolha o número do brinde: '))

        print(f'\nBrinde escolhido: {Brindes[escolha - 1]}')
    else:
        print('\nContinue comprando para ganhar brindes!')

    # ===== GASTOS DO CLIENTE =====
    encontrou = False
    for g in GastosClientes:
        if g['nome'] == UsuarioConectado['nome']:
            g['total'] += soma
            encontrou = True
            break

    if not encontrou:
        GastosClientes.append({
            'nome': UsuarioConectado['nome'],
            'total': soma
        })



def agendar_servicos(UsuarioConectado):
    Agendamentos = []
    soma = 0

    while True:
        print('\n--- Serviços Disponíveis ---')
        for i in range(len(servicos.servicos)):
            print(f"{i} - {servicos.servicos[i]['nome']} | R$ {servicos.servicos[i]['preco']}")

        indice = int(input('\nDigite o índice do serviço desejado: '))
        while indice < 0 or indice >= len(servicos.servicos):
            print('Índice inválido!')
            indice = int(input('Digite novamente: '))

        horario = input('Digite o horário desejado (ex: 14:30): ')

        Agendamentos.append({
            'servico': servicos.servicos[indice]['nome'],
            'preco': servicos.servicos[indice]['preco'],
            'horario': horario
        })

        soma += servicos.servicos[indice]['preco']

        print(f'\nServiço agendado: {servicos.servicos[indice]["nome"]}')
        print(f'Horário escolhido: {horario}')
        print(f'Valor: R$ {servicos.servicos[indice]["preco"]}')
        print(f'Total atual: R$ {soma}')

        continuar = input('\nDeseja agendar outro serviço? <s/n>: ')
        if continuar.lower() not in ['s', 'sim']:
            break

    # ===== RESUMO =====
    print('\n--- Agendamentos Realizados ---')
    for i in range(len(Agendamentos)):
        print(
            f"{i} - {Agendamentos[i]['servico']} | "
            f"Horário: {Agendamentos[i]['horario']} | "
            f"R$ {Agendamentos[i]['preco']}"
        )

    print(f'\nTotal: R$ {soma}')

    # ===== PAGAMENTO =====
    print('\n--- Pagamento ---')
    print(f"Cliente: {UsuarioConectado['nome']} | Email: {UsuarioConectado['email']}")

    if soma > 250:
        print('\nParabéns! Você ganhou 20% de desconto')
        soma *= 0.80

    print(f'Valor final a pagar: R$ {soma}')
    input('Forma de pagamento <Dinheiro/Pix>: ')

    # ===== ATENDENTE =====
    atendenteNome = input('Nome do atendente: ')
    achou = False

    for a in Atendentes:
        if a['nome'] == atendenteNome:
            a['qtd'] += 1
            achou = True
            break

    if not achou:
        Atendentes.append({
            'nome': atendenteNome,
            'qtd': 1
        })

    print('\nAgendamento finalizado com sucesso!')

    # ===== BRINDE =====
    if soma >= 200:
        print('\nVocê ganhou um brinde!')
        for i in range(len(Brindes)):
            print(f'{i + 1} - {Brindes[i]}')

        escolha = int(input('Escolha o número do brinde: '))
        while escolha < 1 or escolha > len(Brindes):
            print('Opção inválida!')
            escolha = int(input('Escolha o número do brinde: '))

        print(f'Brinde escolhido: {Brindes[escolha - 1]}')
    else:
        print('\nContinue comprando para ganhar brindes!')

    # ===== GASTOS DO CLIENTE =====
    encontrou = False
    for g in GastosClientes:
        if g['nome'] == UsuarioConectado['nome']:
            g['total'] += soma
            encontrou = True
            break

    if not encontrou:
        GastosClientes.append({
            'nome': UsuarioConectado['nome'],
            'total': soma
        })
