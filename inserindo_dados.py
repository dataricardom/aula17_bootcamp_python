from create_table import Produto, Fornecedor
from engine_conn import Session

# Realizar inserções nessas tabelas para praticas manipulação de dados.


#Inserindo Dados nas Tableas Produto e Fornecedor
with Session() as session:
    fornecedor1 = Fornecedor(nome_fornecedor = 'Dell') 
    fornecedor2 = Fornecedor(nome_fornecedor = 'Alienware')
    session.add_all([fornecedor1,fornecedor2])
    session.commit()

# Em produto foi adicionado a chave estrangeira do fornecedor
    produto1 = Produto(nome_produto='Notebook', id_fornecedor=fornecedor1.id_fornecedor)
    produto2 = Produto(nome_produto='Monitor',id_fornecedor=fornecedor2.id_fornecedor)
    session.add_all([produto1,produto2])
    session.commit()