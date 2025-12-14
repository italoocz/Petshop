import produtos
import servicos
import usuarios
import compras

def main():
    while True:
        print("\n===== Au Au Fofura =====")
        print('Bem vindo ao PetShop')
        print('1 - Fazer login')
        print('2 - Cadastrar usuário')
        print('3 - Cadastro de Pet')
        print('4 - Listar Usuários e Pets')
        print('0 - Sair\n')

        opcao = input('Escolha a opção: ')

        if opcao == '1':
            resultado = usuarios.login()

            if resultado:
                tipo, usuario_logado = resultado

                if tipo == 'admin':
                    print(f'\nBem-vindo administrador {usuario_logado}!')
                    menu_admin()

                else:
                    compras.menu_cliente(usuario_logado)

        elif opcao == '2':
            usuarios.cadastrar_usuario()

        elif opcao == '3':
            usuarios.cadastrar_pet()

        elif opcao == '4':
            usuarios.listar_Pets_Users()

        elif opcao == '0':
            print('\nEncerrando sistema...')
            break

        else:
            print('Opção inválida!')


def menu_admin():
    while True:
        print('\n=== MENU ADMIN ===')
        print('1 - Cadastrar produto ou serviço')
        print('2 - Alterar produto ou serviço')
        print('3 - Deletar produto ou serviço')
        print('4 - Listar produtos')
        print('5 - Listar serviços')
        print('6 - Ranking de clientes')
        print('7 - Ranking de atendentes')
        print('0 - Voltar')

        opcao = input('Escolha a opção: ')

        if opcao == '1':
            usuarios.cadastrar_prod_serv()

        elif opcao == '2':
            usuarios.alterar_prod_serv()

        elif opcao == '3':
            usuarios.deletar_prod_serv()

        elif opcao == '4':
            produtos.listar_produtos()

        elif opcao == '5':
            servicos.listar_servicos()

        elif opcao == '6':
            usuarios.mostrar_rank_clientes()

        elif opcao == '7':
            usuarios.mostrar_rank_atendentes()

        elif opcao == '0':
            break

        else:
            print('Opção inválida!')



main()