CREATE TABLE Cliente (
    cpf_cliente VARCHAR(20),
    nome_cliente VARCHAR(100),
    email_cliente VARCHAR(100),
    senha_cliente VARCHAR(100),
    endereco VARCHAR(200),
    contato VARCHAR(20),
    PRIMARY KEY (cpf_cliente)
);

CREATE TABLE Gerente (
    id_gerente INT AUTO_INCREMENT,
    nome_gerente VARCHAR(100),
    email_gerente VARCHAR(100),
    senha_gerente VARCHAR(100),
    PRIMARY KEY (id_gerente)
);

CREATE TABLE Funcionario (
    id_funcionario INT AUTO_INCREMENT,
    id_gerente INT,
    nome_funcionario VARCHAR(100),
    contato_funcionario VARCHAR(20),
    cargo VARCHAR(100),
    salario DECIMAL(10, 2),
    PRIMARY KEY (id_funcionario)
    FOREIGN KEY (id_gerente) REFERENCES Gerente(id_gerente)
);

CREATE TABLE Produto (
    id_produto INT AUTO_INCREMENT,
    nome_produto VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(10, 2),
    PRIMARY KEY (id_produto)
);

CREATE TABLE Ingrediente (
    id_ingrediente INT AUTO_INCREMENT,
    nome_ingrediente VARCHAR(100),
    unidade_medida VARCHAR(50),
    PRIMARY KEY (id_ingrediente)
);

CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT,
    id_cliente INT,
    id_funcionario INT,
    status_pedido VARCHAR(50),
    valor_total DECIMAL(10, 2),
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(cpf_cliente),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

CREATE TABLE PedidoProduto (
    id_pedido INT,
    id_produto INT,
    quantidade_comprada INT,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);

CREATE TABLE ProdutoIngrediente (
    id_produto INT,
    id_ingrediente INT,
    quantidade_usada INT,
    PRIMARY KEY (id_produto, id_ingrediente),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
    FOREIGN KEY (id_ingrediente) REFERENCES Ingrediente(id_ingrediente)
);