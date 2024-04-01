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

        # Verifica se todos os campos estão preenchidos
        if nome.strip() == '' or cpf.strip() == '' or email.strip() == '' or senha.strip() == '' or endereco.strip() == '' or contato.strip() == '':
            print('Por favor, preencha todos os campos.')
            return
        
        cursor.execute(f'SELECT * FROM cliente WHERE cpf_cliente = "{cpf}"')
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
                cursor.execute(f'INSERT INTO cliente (nome_cliente, cpf_cliente, email_cliente, senha_cliente, endereco, contato) VALUES ("{cliente.nome_cliente}", "{cliente.cpf}", "{cliente.email_cliente}", "{cliente.senha_cliente}", "{cliente.endereco}", "{cliente.contato}")')
                conexao.commit()
                print('Cliente cadastrado com sucesso!')
    
    except mysql.connector.Error as err:
        print(err)
        return None


def loginCliente(cursor):
    try:
        # Parte que importa
        email = input('Digite seu Email: ')
        senha = input('Digite sua Senha: ')

        # Verifica se os campos estão preenchidos
        if email.strip() == '' or senha.strip() == '':
            print('Por favor, preencha todos os campos.')
            return None

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
            novo_nome = input('Digite seu novo nome:')
            novo_email = input('Digite seu novo email:')
            nova_senha = input('Digite sua nova senha:')
            novo_endereco = input('Digite seu novo endereço:')
            novo_contato = input('Digite seu novo contato:')

            # Verifica se todos os campos estão preenchidos
            if novo_nome.strip() == '' or novo_email.strip() == '' or nova_senha.strip() == '' or novo_endereco.strip() == '' or novo_contato.strip() == '':
                print('Por favor, preencha todos os campos.')
                return None

            objeto_cliente.nome_cliente = novo_nome
            objeto_cliente.email_cliente = novo_email
            objeto_cliente.senha_cliente = nova_senha
            objeto_cliente.endereco = novo_endereco
            objeto_cliente.contato = novo_contato

            cursor.execute(f'UPDATE cliente SET nome_cliente = "{objeto_cliente.nome_cliente}", email_cliente = "{objeto_cliente.email_cliente}", senha_cliente = "{objeto_cliente.senha_cliente}", endereco = "{objeto_cliente.endereco}", contato = "{objeto_cliente.contato}" WHERE cpf = "{objeto_cliente.cpf}"')
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
            cursor.execute(f'DELETE FROM cliente WHERE cpf_cliente = "{objeto_cliente.cpf}"')
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
            print(f'CPF: {cliente[0]}\tNome: {cliente[1]}\tEmail: {cliente[2]}\tSenha: {cliente[3]}\tEndereço: {cliente[4]}\tContato: {cliente[5]}\n')
    except mysql.connector.Error as err:
        print(err)
        return None

# Funções do Gerente ###########################################################
def cadastroGerente(cursor, conexao):
    try:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')

        # Verifica se todos os campos estão preenchidos
        if nome.strip() == '' or email.strip() == '' or senha.strip() == '':
            print('Por favor, preencha todos os campos.')
            return

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

        # Verifica se os campos estão preenchidos
        if email.strip() == '' or senha.strip() == '':
            print('Por favor, preencha todos os campos.')
            return None

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
            novo_nome = input('Digite seu novo nome:')
            novo_email = input('Digite seu novo email:')
            nova_senha = input('Digite sua nova senha:')

            # Verifica se todos os campos estão preenchidos
            if novo_nome.strip() == '' or novo_email.strip() == '' or nova_senha.strip() == '':
                print('Por favor, preencha todos os campos.')
                return None

            objeto_gerente.nome_gerente = novo_nome
            objeto_gerente.email_gerente = novo_email
            objeto_gerente.senha_gerente = nova_senha

            cursor.execute(f'UPDATE gerente SET nome_gerente = "{objeto_gerente.nome_gerente}", email_gerente = "{objeto_gerente.email_gerente}", senha_gerente = "{objeto_gerente.senha_gerente}" WHERE id_gerente = "{objeto_gerente.id_gerente}"')
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
def cadastrarIngrediente(cursor, conexao, nome, unidade_medida):
    try:
        cursor.execute("INSERT INTO ingrediente (nome_ingrediente, unidade_medida) VALUES (%s, %s)", (nome, unidade_medida))
        conexao.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar ingrediente: {err}")
        return None

def cadastrarProdutoIngrediente(cursor, conexao, id_produto, id_ingrediente, quantidade_usada):
    try:
        cursor.execute("INSERT INTO produtoingrediente (id_produto, id_ingrediente, quantidade_usada) VALUES (%s, %s, %s)", (id_produto, id_ingrediente, quantidade_usada))
        conexao.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar produto ingrediente: {err}")

def cadastroProduto(cursor, conexao):
    try:
        nome = input('Nome do produto: ')
        descricao = input('Descrição do produto: ')
        preco = float(input('Preço do produto: '))

        if nome.strip() == '' or descricao.strip() == '' or preco <= 0:
            print('Por favor, preencha todos os campos corretamente.')
            return

        cursor.execute("INSERT INTO produto (nome_produto, descricao, preco) VALUES (%s, %s, %s)", (nome, descricao, preco))
        conexao.commit()
        id_produto = cursor.lastrowid

        quantidade = int(input('Quantos ingredientes esse produto leva? '))
        for _ in range(quantidade):
            ingrediente = input('Digite o nome do ingrediente: ')
            quantidade_utilizada = float(input('Digite a quantidade do ingrediente: '))
            unidade_medida = input('Digite a unidade de medida do ingrediente: ')

            id_ingrediente = cadastrarIngrediente(cursor, conexao, ingrediente, unidade_medida)
            if id_ingrediente:
                cadastrarProdutoIngrediente(cursor, conexao, id_produto, id_ingrediente, quantidade_utilizada)

        print('Produto cadastrado com sucesso!')
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar produto: {err}")


def atualizarProduto(cursor, conexao):
    try:
        print('Produtos cadastrados no sistema: ')
        listarProdutos(cursor)
        id = input('Digite o ID do produto que deseja atualizar: (0)-Cancelar')
        
        # Verifica se o campo ID foi preenchido
        if id.strip() == '':
            print('Por favor, insira o ID do produto.')
            return None
        
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

                    # Verifica se todos os campos estão preenchidos
                    if nome.strip() == '' or descricao.strip() == '' or preco.strip() == '':
                        print('Por favor, preencha todos os campos.')
                        return None

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
                    cursor.execute(f'DELETE FROM pedidoproduto WHERE id_produto = "{id}"')
                    cursor.execute(f'DELETE FROM produtoingrediente WHERE id_produto = "{id}"')
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
        cursor.execute(f'SELECT * FROM Produto WHERE id_produto = "{id}"')
        resultado = cursor.fetchone()
        if resultado is None:
            print('Produto não encontrado!')
            return None
        else:
            produto = Produto(resultado[0], resultado[1], resultado[2], resultado[3])
            print(f'ID: {produto.id_produto}\tNome: {produto.nome_produto}\tDescrição: {produto.descricao}\tPreço: {produto.preco}\n')
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
                    pedidoProduto = PedidoProduto(id_pedido, id_produto, quantidade_comprada)
                    cursor.execute(f'INSERT INTO pedidoproduto (id_pedido, id_produto, quantidade_comprada) VALUES ("{pedidoProduto.id_pedido}", "{pedidoProduto.id_produto}", "{pedidoProduto.quantidade_comprada}")')
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
            print(f'ID: {pedido.id_pedido}\tCPF do cliente: {pedido.id_cliente}\tValor total: {pedido.valor_total}\n')
            return pedido
    except mysql.connector.Error as err:
        print(err)
        return None