import mysql.connector
from classes import Cliente, Ingrediente, Produto, Pedido, Gerente, ProdutoIngrediente, PedidoProduto

# Funções do Cliente ###########################################################
def cadastroCliente(cursor, conexao):
    try:
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        email = input('Digite seu Email: ')
        senha = input('Digite sua Senha: ')
        endereco = input('Digite seu Endereço: ')
        contato = input('Digite seu telefone de Contato: ')

        cursor.execute(f'SELECT * FROM cliente WHERE cpf = "{cpf}"')
        if cursor.fetchone() is not None:
            print('CPF já cadastrado!')
            return
        else:
            cursor.execute(f'SELECT * FROM cliente WHERE email_cliente = "{email}"')
            if cursor.fetchone() is not None:
                print('Email já cadastrado!')
                return
            else:   
                cliente = Cliente(nome, cpf, email, senha, endereco, contato)
                cursor.execute(f'INSERT INTO cliente (nome_cliente, cpf, email_cliente, senha_cliente, endereco, contato) VALUES ("{cliente.nome}", "{cliente.cpf}", "{cliente.email}", "{cliente.senha}", "{cliente.endereco}", "{cliente.contato}")')
                conexao.commit()
                print('Cliente cadastrado com sucesso!')
    
    except mysql.connector.Error as err:
        print(err)
        return None


def loginCliente(cursor):
    try:
        #parte que importa
        email = input('Digite seu Email: ')
        senha = input('Digite sua Senha: ')
        cursor.execute(f'SELECT * FROM cliente WHERE email_cliente = "{email}" AND senha_cliente = "{senha}"')
        
        resultado = cursor.fetchone()

        if resultado is None:
            print('Email ou senha incorretos!')
            return None
        else:
            cliente = Cliente(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5])
            return cliente
        #
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar cliente: {erro}")
        return None


def atualizarContaCliente(objeto_cliente, cursor, conexao):
    try:
        print('Deseja atualizar seus dados? (1)-Sim (0)-Não')
        if (input() == '1'):
            objeto_cliente.nome = input('Digite seu novo nome:')
            objeto_cliente.email = input('Digite seu novo email:')
            objeto_cliente.senha = input('Digite sua nova senha:')
            objeto_cliente.endereco = input('Digite seu novo endereço:')
            objeto_cliente.contato = input('Digite seu novo contato:')

            cursor.execute(f'UPDATE cliente SET nome_cliente = "{objeto_cliente.nome}", email_cliente = "{objeto_cliente.email}", senha_cliente = "{objeto_cliente.senha}", endereco = "{objeto_cliente.endereco}", contato = "{objeto_cliente.contato}" WHERE cpf = "{objeto_cliente.cpf}"')
            conexao.commit()
            print('Dados atualizados com sucesso!')

        else:
            print('Operação cancelada')
            return None

    except mysql.connector.Error as err:
        print(err)
        return None


def removerContaCliente(objeto_cliente, cursor, conexao):
    try:
        print('Deseja remover sua conta? (1)-Sim (0)-Não')
        if (input() == '1'):
            cursor.execute(f'DELETE FROM cliente WHERE cpf = "{objeto_cliente.cpf}"')
            conexao.commit()
            print('Conta removida com sucesso!')
        else:
            print('Operação cancelada')
            return None
    except mysql.connector.Error as err:
        print(err)
        return None

def listarClientes(cursor):
    try:
        cursor.execute('SELECT * FROM cliente')
        resultado = cursor.fetchall()
        for cliente in resultado:
            print(f'Nome: {cliente[0]}\tCPF: {cliente[1]}\tEmail: {cliente[2]}\tSenha: {cliente[3]}\tEndereço: {cliente[4]}\tContato: {cliente[5]}\n')
    except mysql.connector.Error as err:
        print(err)
        return None

# Funções do Gerente ###########################################################
def cadastroGerente(cursor, conexao):
    try:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')

        cursor.execute(f'SELECT * FROM gerente WHERE email_gerente = "{email}"')
        if cursor.fetchone() is not None:
            print('Email já cadastrado!')
            return
        else:
            cursor.execute(f'INSERT INTO gerente (nome_gerente, email_gerente, senha_gerente) VALUES ("{nome}", "{email}", "{senha}")')
            conexao.commit()
            print('Gerente cadastrado com sucesso!')

    except mysql.connector.Error as err:
        print(err)
        return None


def loginGerente(cursor):
    try:
        email = input('Digite seu Email: ')
        senha = input('Digite sua Senha: ')
        cursor.execute(f'SELECT * FROM gerente WHERE email_gerente = "{email}" AND senha_gerente = "{senha}"')
        
        resultado = cursor.fetchone()

        if resultado is None:
            print('Email ou senha incorretos!')
            return None
        else:
            gerente = Gerente(resultado[0], resultado[1], resultado[2], resultado[3])
            return gerente

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar gerente: {erro}")
        return None

def atualizarContaGerente(objeto_gerente, cursor, conexao):
    try:
        print('Deseja atualizar seus dados? (1)-Sim (0)-Não')
        if (input() == '1'):
            objeto_gerente.nome = input('Digite seu novo nome:')
            objeto_gerente.email = input('Digite seu novo email:')
            objeto_gerente.senha = input('Digite sua nova senha:')

            cursor.execute(f'UPDATE gerente SET nome_gerente = "{objeto_gerente.nome}", email_gerente = "{objeto_gerente.email}", senha_gerente = "{objeto_gerente.senha}" WHERE email_gerente = "{objeto_gerente.email}"')
            conexao.commit()
            print('Dados atualizados com sucesso!')

        else:
            print('Operação cancelada')
            return None

    except mysql.connector.Error as err:
        print(err)
        return None

def removerContaGerente(objeto_gerente, cursor, conexao):
    try:
        print('Deseja remover sua conta? (1)-Sim (0)-Não')
        if (input() == '1'):
            cursor.execute(f'DELETE FROM gerente WHERE email_gerente = "{objeto_gerente.email}"')
            conexao.commit()
            print('Conta removida com sucesso!')
        else:
            print('Operação cancelada')
            return None
        
    except mysql.connector.Error as err:
        print(err)
        return None

# Funções do Produto ###########################################################
def cadastroProduto(cursor, conexao):
    try:
        nome = input('Nome do produto: ')
        descricao = input('Descrição do produto: ')
        preco = input('Preço do produto: ')
        cursor.execute(f'INSERT INTO produto (nome_produto, descricao, preco) VALUES ("{nome}", "{descricao}", "{preco}");')
        conexao.commit()
        cursor.execute(f'SELECT LAST_INSERT_ID();')
        id_produto = cursor.fetchone()

        quantidade = input('Quantos ingredientes esse produto leva? ')
        if quantidade.isdigit():
            quantidade = int(quantidade)
            for i in range(0, quantidade):
                ingrediente = input('Digite o nome do ingrediente: ')
                quantidadeUtilizada = input('Digite a quantidade do ingrediente: ')
                cursor.execute(f'SELECT * FROM ingrediente WHERE nome_ingrediente = "{ingrediente}"')
                resultado = cursor.fetchone()
                if resultado is None:
                    unidadeMedida = input('Digite a unidade de medida do ingrediente: ')
                    cursor.execute(f'INSERT INTO ingrediente (nome_ingrediente unidade_medida) VALUES ("{ingrediente}", "{unidadeMedida}")')
                    conexao.commit()
                    cursor.execute(f'SELECT LAST_INSERT_ID()')
                    id_ingrediente = cursor.fetchone()
                    produtoIngrediente1 = ProdutoIngrediente(id_produto, id_ingrediente, quantidadeUtilizada)
                    cursor.execute(f'INSERT INTO produto_ingrediente (id_produto, id_ingrediente, quantidade_usada) VALUES ("{produtoIngrediente1.produto_id}", "{produtoIngrediente1.ingrediente_id}", "{produtoIngrediente1.quantidade_usada}");')
                    conexao.commit()
                    i += 1
                else:
                    ingrediente = Ingrediente(resultado[0], resultado[1], resultado[2])
                    produtoIngrediente2 = ProdutoIngrediente(id_produto, id_ingrediente, quantidadeUtilizada)
                    cursor.execute(f'INSERT INTO produto_ingrediente (id_produto, id_ingrediente, quantidade_usada) VALUES ("{produtoIngrediente2.produto_id}", "{produtoIngrediente2.ingrediente_id}", "{produtoIngrediente2.quantidade_usada}");')
                    conexao.commit()
                    i += 1
        else:
            print('Valor inválido!')
            return None
    except mysql.connector.Error as err:
        print(err)
        return None

def atualizarProduto(cursor, conexao):
    try:
        print('Produtos cadastrados no sistema: ')
        listarProdutos(cursor)
        id = input('Digite o ID do produto que deseja atualizar: (0)-Cancelar')
        if id == '0':
            print('Operação cancelada')
            return None
        else:
            cursor.execute(f'SELECT * FROM produto WHERE id_produto = "{id}"')
            resultado = cursor.fetchone()
            if resultado is None:
                print('Produto não encontrado!')
                return None
            else:
                print('Deseja atualizar os dados do produto? (1)-Sim (0)-Não')
                if (input() == '1'):
                    nome = input('Digite o novo nome do produto: ')
                    descricao = input('Digite a nova descrição do produto: ')
                    preco = input('Digite o novo preço do produto: ')
                    cursor.execute(f'UPDATE produto SET nome_produto = "{nome}", descricao = "{descricao}", preco = "{preco}" WHERE id_produto = "{id}"')
                    conexao.commit()
                    print('Dados atualizados com sucesso!')
                else:
                    print('Operação cancelada')
                    return None
    except mysql.connector.Error as err:
        print(err)
        return None

def removerProduto(cursor, conexao):
    try:
        print('Produtos cadastrados no sistema:')
        listarProdutos(cursor, conexao)
        id = input('Digite o ID do produto que deseja remover: (0)-Cancelar')
        if id == '0':
            print('Operação cancelada')
            return None
        else:
            cursor.execute(f'SELECT * FROM produto WHERE id_produto = "{id}"')
            resultado = cursor.fetchone()
            if resultado is None:
                print('Produto não encontrado!')
                return None
            else:
                print('Deseja remover o produto? (1)-Sim (0)-Não')
                if (input() == '1'):
                    cursor.execute(f'DELETE FROM compra WHERE id_produto = "{id}"')
                    cursor.execute(f'DELETE FROM produto_ingrediente WHERE id_produto = "{id}"')
                    cursor.execute(f'DELETE FROM produto WHERE id_produto = "{id}"')
                    conexao.commit()
                    print('Produto removido com sucesso!')
                else:
                    print('Operação cancelada')
                    return None
    except mysql.connector.Error as err:
        print(err)
        return None

def listarProdutos(cursor):
    try:
        cursor.execute('SELECT * FROM produto')
        resultado = cursor.fetchall()
        for produto in resultado:
            print(f'ID: {produto[0]}\tNome: {produto[1]}\tDescrição: {produto[2]}\tPreço: {produto[3]}\n')
    except mysql.connector.Error as err:
        print(err)
        return None

def buscarProduto(cursor):
    try:
        id = input('Digite o ID do produto: ')
        cursor.execute(f'SELECT * FROM produto WHERE id_produto = "{id}"')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Produto não encontrado!')
            return None
        else:
            produto = Produto(resultado[0], resultado[1], resultado[2], resultado[3])
            print(f'ID: {produto.produto_id}\tNome: {produto.nome}\tDescrição: {produto.descricao}\tPreço: {produto.preco}\n')
            return produto
    except mysql.connector.Error as err:
        print(err)
        return None



# Funções do Pedido ###########################################################
def fazerPedido(objeto_cliente, cursor, conexao):
    try:
        input('Deseja fazer um pedido? (1)-Sim (0)-Não')
        if input() == '0':
            print('Operação cancelada')
            return None
        else:
            valor_total = 0
            cursor.execute(f'INSERT INTO pedido (cliente_cpf, valor_total) VALUES ("{objeto_cliente.cpf}", "{valor_total}")')
            conexao.commit()
            cursor.execute(f'SELECT LAST_INSERT_ID()')
            id_pedido = cursor.fetchone()
            pedido = Pedido(id_pedido, objeto_cliente.cpf, valor_total)
            print('Produtos disponíveis no sistema: ')
            listarProdutos(cursor)
            while True:
                id_produto = input('Digite o ID do produto que deseja comprar: ')
                cursor.execute(f'SELECT * FROM produto WHERE id_produto = "{id_produto}"')
                resultado = cursor.fetchone()
                if resultado is None:
                    print('Produto não encontrado!')
                    return None
                else:
                    produto = Produto(resultado[0], resultado[1], resultado[2], resultado[3])
                    quantidade_comprada = input('Digite a quantidade que deseja comprar: ')
                    valor_compra = produto.preco * quantidade_comprada   
                    compra = PedidoProduto(id_pedido, id_produto, quantidade_comprada)
                    cursor.execute(f'INSERT INTO compra (id_pedido, id_produto, quantidade_comprada) VALUES ("{compra.pedido_id}", "{compra.produto_id}", "{compra.quantidade_comprada}")')
                    conexao.commit()
                    input('Deseja continuar comprando? (1)-Sim (0)-Não')
                    if input() == '0':
                        cursor.execute(f'UPDATE pedido SET valor_total = "{valor_total + valor_compra}" WHERE id_pedido = "{id_pedido}"')
                        conexao.commit()
                        print('Pedido realizado com sucesso!')
                        break
                    else:
                        cursor.execute(f'UPDATE pedido SET valor_total = "{valor_total + valor_compra}" WHERE id_pedido = "{id_pedido}"')
                        conexao.commit()
                        print('Produto adicionado ao pedido com sucesso!')
    except mysql.connector.Error as err:
        print(err)
        return None

def listarPedidos(cursor):
    try:
        cursor.execute('SELECT * FROM pedido')
        resultado = cursor.fetchall()
        for pedido in resultado:
            print(f'ID: {pedido[0]}\tCPF do cliente: {pedido[1]}\tValor total: {pedido[2]}\n')
    except mysql.connector.Error as err:
        print(err)
        return None

def listarPedidosPorCliente(objeto_cliente, cursor):
    try:
        cursor.execute(f'SELECT * FROM pedido WHERE cliente_cpf = "{objeto_cliente.cpf}"')
        resultado = cursor.fetchall()
        for pedido in resultado:
            print(f'ID: {pedido[0]}\tCPF do cliente: {pedido[1]}\tValor total: {pedido[2]}\n')
    except mysql.connector.Error as err:
        print(err)
        return None

def buscarPedido(cursor):
    try:
        id_pedido = input('Digite o ID do pedido: ')
        cursor.execute(f'SELECT * FROM pedido WHERE id_pedido = "{id_pedido}"')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Pedido não encontrado!')
            return None
        else:
            pedido = Pedido(resultado[0], resultado[1], resultado[2])
            print(f'ID: {pedido.pedido_id}\tCPF do cliente: {pedido.cliente_cpf}\tValor total: {pedido.valor_total}\n')
            return pedido
    except mysql.connector.Error as err:
        print(err)
        return None