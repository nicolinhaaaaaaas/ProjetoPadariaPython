class Cliente:
    def __init__(self, cpf, nome_cliente, email_cliente, senha_cliente, endereco, contato):
        self.cpf = cpf
        self.nome_cliente = nome_cliente
        self.email_cliente = email_cliente
        self.senha_cliente = senha_cliente
        self.endereco = endereco
        self.contato = contato

    def __str__(self):
        return f"Cliente: {self.nome_cliente} - CPF: {self.cpf} - Email: {self.email_cliente} - Endereço: {self.endereco} - Contato: {self.contato}"
    
class Gerente:
    def __init__(self, id_gerente, nome_gerente, email_gerente, senha_gerente):
        self.id_gerente = id_gerente
        self.nome_gerente = nome_gerente
        self.email_gerente = email_gerente
        self.senha_gerente = senha_gerente

    def __str__(self):
        return f"Gerente: {self.nome_gerente} - ID: {self.id_gerente} - Email: {self.email_gerente}"
    
class Funcionario:
    def __init__(self, id_funcionario, id_gerente, nome_funcionario, contato_funcionario, cargo, salario):
        self.id_funcionario = id_funcionario
        self.id_gerente = id_gerente
        self.nome_funcionario = nome_funcionario
        self.contato_funcionario = contato_funcionario
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome_funcionario} - ID: {self.id_funcionario} - Contato: {self.contato_funcionario} - Cargo: {self.cargo} - Salário: R${self.salario}"
    
class Produto:
    def __init__(self, id_produto, nome_produto, descricao, preco):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome_produto} - ID: {self.id_produto} - Descrição: {self.descricao} - Preço: R${self.preco}"
    
class Ingrediente:
    def __init__(self, id_ingrediente, nome_ingrediente, unidade_medida):
        self.id_ingrediente = id_ingrediente
        self.nome_ingrediente = nome_ingrediente
        self.unidade_medida = unidade_medida

    def __str__(self):
        return f"Ingrediente: {self.nome_ingrediente} - ID: {self.id_ingrediente} - Unidade de Medida: {self.unidade_medida}"
    
class Pedido:
    def __init__(self, id_pedido, id_cliente, id_funcionario, status_pedido, valor_total):
        self.id_pedido = id_pedido
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.status_pedido = status_pedido
        self.valor_total = valor_total

    def __str__(self):
        return f"Pedido: {self.id_pedido} - ID Cliente: {self.id_cliente} - ID Funcionário: {self.id_funcionario} - Status: {self.status_pedido} - Valor Total: R${self.valor_total}"
    
class PedidoProduto:
    def __init__(self, id_pedido, id_produto, quantidade_comprada):
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade_comprada = quantidade_comprada

    def __str__(self):
        return f"Pedido: {self.id_pedido} - Produto: {self.id_produto} - Quantidade: {self.quantidade_comprada}"
    
class ProdutoIngrediente:
    def __init__(self, id_produto, id_ingrediente, quantidade_usada):
        self.id_produto = id_produto
        self.id_ingrediente = id_ingrediente
        self.quantidade_usada = quantidade_usada

    def __str__(self):
        return f"Produto: {self.id_produto} - Ingrediente: {self.id_ingrediente} - Quantidade: {self.quantidade_usada}"