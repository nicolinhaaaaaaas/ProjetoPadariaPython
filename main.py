from menu import *
# MySql ###########################################################
import mysql.connector
# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='55879276',
    database='projeto-teste'
)
if conexao.is_connected:  
    # Criar um cursor
    cursor = conexao.cursor()
    
    # Opções globais ###########################################################
    def menuUsuario():
        print('\nBem vindo à Padaria 2 Amantes!')
        print('Que tipo de usuário você é? \n(1)-Cliente \n(2)-Gerente \n(0)-Sair\n')

    def menuLogin():
        print('Já possui uma conta? \n(1)-Login \n(2)-Cadastrar \n(0)-Voltar\n')

    # Opções do Cliente ###########################################################
    def menuCliente():
        print('Escolha o que deseja fazer: \n(1)-Produtos \n(2)-Pedidos \n(3)-Configurações \n(0)-Sair\n')

    def menuProdutosCliente():
        print('MENU DE PRODUTOS: \n(1)-Listar produtos \n(2)-Buscar produto \n(0)-Voltar\n')

    def menuPedidoCliente():
        print('MENU DE PEDIDOS: \n(1)-Fazer um pedido \n(2)-Listar Pedidos \n(0)-Voltar\n')

    def menuConfiguracaoCliente():
        print('MENU DE CONFIGURAÇÕES: \n(1)-Atualizar conta \n(2)-Excluir conta \n(0)-Voltar\n')

    # Opções do Gerente ###########################################################
    def menuGerente():
        print('Escolha o que deseja fazer: \n(1)-Produtos \n(2)-Pedidos \n(3)-Clientes \n(4)-Configurações \n(0)-Sair\n')

    def menuProdutosGerente():
        print('MENU DE PRODUTOS: \n(1)-Listar produtos \n(2)-Buscar produto \n(3)-Cadastrar produto \n(4)-Atualizar produto \n(5)-Excluir produto \n(0)-Voltar\n')

    def menuPedidosGerente():
        print('MENU DE PEDIDOS: \n(1)-Listar Pedidos \n(2)-Buscar Pedido \n(0)-Voltar\n')

    def menuClientesGerente():
        print('MENU DE CLIENTES: \n(1)-Listar clientes \n(0)-Voltar\n')

    def menuConfiguracaoGerente():
        print('MENU DE CONFIGURAÇÕES: \n(1)-Atualizar conta \n(2)-Excluir conta \n(0)-Voltar\n')

    # MENU PRINCIPAL ###########################################################


    while True:
        menuUsuario()
        opcao = input()

        if opcao == '1': # Cliente
            while True:
                menuLogin()
                opcao = input()

                if opcao == '1': # Login
                    cliente = loginCliente(cursor)
                    if cliente is not None:
                        while True:
                            menuCliente()
                            opcao = input()

                            if opcao == '1': # Produtos
                                while True:
                                    menuProdutosCliente()
                                    opcao = input()
                                    if opcao == '1': # Listar produtos
                                        listarProdutos(cursor)
                                    elif opcao == '2': # Buscar produto
                                        buscarProduto(cursor)
                                    elif opcao == '0': # Voltar
                                        break
                                    else:
                                        print('Opção inválida!')

                            elif opcao == '2': # Pedidos
                                while True:
                                    menuPedidoCliente()
                                    opcao = input()
                                    if opcao == '1': # Fazer um pedido
                                        fazerPedido(cursor, conexao, cliente)
                                    elif opcao == '2': # Listar Pedidos
                                        listarPedidosPorCliente(cursor, cliente)
                                    elif opcao == '0': # Cancelar Pedido
                                        break
                                    else:
                                        print('Opção inválida!')

                            elif opcao == '3': # Configurações
                                while True:
                                    menuConfiguracaoCliente()
                                    opcao = input()
                                    if opcao == '1': # Atualizar conta
                                        atualizarContaCliente(cliente, cursor, conexao)
                                    elif opcao == '2': # Excluir conta
                                        removerContaCliente(cliente, cursor, conexao)
                                        break
                                    elif opcao == '0': # Voltar
                                        break
                                    else:
                                        print('Opção inválida!')

                            elif opcao == '0': # Sair
                                break
                            else:
                                print('Opção inválida!')
                    else:
                        print('Email ou senha incorretos!')
                elif opcao == '2': # Cadastrar
                    cadastroCliente(cursor, conexao)
                elif opcao == '0': # Voltar
                    break
                else:
                    print('Opção inválida!')


        elif opcao == '2': # Gerente
            while True:
                menuLogin()
                opcao = input()

                if opcao == '1': # Login
                    gerente = loginGerente(cursor)
                    if gerente is not None:
                        while True:
                            menuGerente()
                            opcao = input()

                            if opcao == '1': # Produtos
                                while True:
                                    menuProdutosGerente()
                                    opcao = input()
                                    if opcao == '1': # Listar produtos
                                        listarProdutos(cursor)
                                    elif opcao == '2': # Buscar produto
                                        buscarProduto(cursor)
                                    elif opcao == '3': # Cadastrar produto
                                        cadastroProduto(cursor, conexao)
                                    elif opcao == '4': # Atualizar produto
                                        atualizarProduto(cursor, conexao)
                                    elif opcao == '5': # Excluir produto
                                        removerProduto(cursor, conexao)
                                    elif opcao == '0': # Voltar
                                        break
                                    else:
                                        print('Opção inválida!')
                            
                            elif opcao == '2': # Pedidos
                                while True:
                                    menuPedidosGerente()
                                    opcao = input()
                                    if opcao == '1': # Listar Pedidos
                                        listarPedidos(cursor)
                                    elif opcao == '2': # Buscar Pedido
                                        buscarPedido(cursor)
                                    elif opcao == '0': # Voltar
                                        break
                                    else:
                                        print('Opção inválida!')
                            
                            elif opcao == '3': # Clientes
                                while True:
                                    menuClientesGerente()
                                    opcao = input()
                                    if opcao == '1': # Listar clientes
                                        listarClientes(cursor)
                                    elif opcao == '0': # Voltar
                                        break
                                    else:
                                        print('Opção inválida!')
                            
                            elif opcao == '4': # Configurações
                                while True:
                                    menuConfiguracaoGerente()
                                    opcao = input()
                                    if opcao == '1':
                                        atualizarContaGerente(gerente, cursor, conexao)
                                    elif opcao == '2':
                                        removerContaGerente(gerente, cursor, conexao)
                                        break
                                    elif opcao == '0':
                                        break
                                    else:
                                        print('Opção inválida!')
                            
                            elif opcao == '0': # Sair
                                break
                            else:
                                print('Opção inválida!')
                    else:
                        print('Email ou senha incorretos!')
                elif opcao == '2': # Cadastrar
                    cadastroGerente(cursor, conexao)
                elif opcao == '0': # Voltar
                    break
                else:
                    print('Opção inválida!')
                        
        elif opcao == '0': # Sair
            cursor.close()
            conexao.close()
            print('Saindo...\n')
            break

        else:
            print('Opção inválida!\n')

else:
    print('Falha na conexão')