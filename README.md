# Aula17 Bootcamp Python

## SQLAlchemy

### Ricardo Marques


Este script cria uma conexão com um banco SQLite usando SQLAlchemy e define uma tabela chamada usuarios. A tabela é modelada pela classe Usuario, com colunas para id, nome e idade. Utilizando o sistema de mapeamento ORM do SQLAlchemy, ele gera automaticamente o esquema no banco de dados. A conexão é configurada para exibir as operações SQL com o parâmetro echo=True.




- O SQLAlchemy é uma biblioteca poderosa e amplamente usada em Python para mapeamento objeto-relacional (ORM) e construção de consultas SQL. Ele fornece ferramentas avançadas para interagir com bancos de dados relacionais, oferecendo flexibilidade e controle total sobre consultas e esquemas.

Com o SQLAlchemy, é possível:

- Criar e gerenciar esquemas de banco de dados usando classes Python (ORM);
- Executar consultas SQL personalizadas com o Core SQLAlchemy (para consultas mais detalhadas);
- Trabalhar com diferentes bancos de dados, como SQLite, MySQL, PostgreSQL, entre outros;
- Gerenciar transações, conexões e relacionamentos complexos de forma eficiente.

Sua abordagem permite tanto abstração para simplicidade quanto personalização para casos de uso mais avançados. Se precisar de exemplos ou detalhes sobre funcionalidades específicas, posso ajudar!



# Projeto



**Projeto SQLAlchemy com SQLite**
Este projeto tem como objetivo demonstrar o uso do SQLAlchemy para criar e manipular um banco de dados SQLite. Através dele, foi possível aplicar conceitos de ORM (Object-Relational Mapping), criando tabelas, estabelecendo relacionamentos entre elas e realizando a inserção de dados.

**Estrutura do Projeto**
O projeto é dividido em três arquivos principais:

**engine_conn.py:** Responsável pela conexão com o banco de dados SQLite utilizando o SQLAlchemy. Este arquivo configura a engine e a session, permitindo a interação com o banco.

**create_table.py:** Arquivo para criação das tabelas no banco de dados, utilizando duas abordagens:

- Anotada (Annotated): Usando Mapped[] e mapped_column para definir os tipos e relações das colunas.
Não anotada (Non-annotated): Definindo as colunas e os relacionamentos de forma mais explícita, sem o uso das anotações de tipo.
Este arquivo inclui a criação de tabelas com chaves primárias e estrangeiras, exemplificando um relacionamento entre tabelas, como o caso de um Estado e suas Cidades.

- inserir_dados.py: Arquivo responsável pela inserção de dados nas tabelas criadas. Através deste arquivo, foi possível adicionar registros ao banco de dados, utilizando o SQLAlchemy para gerenciar as transações.

- Tecnologias Utilizadas
SQLAlchemy: ORM utilizado para definir o modelo de dados e interagir com o banco de dados SQLite.
SQLite: Sistema de banco de dados utilizado para armazenar os dados.


<p align="center">
  <img src="pic/KPUUDATA.png" alt="logo" width="300"/>
</p>







