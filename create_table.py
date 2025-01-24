#importação das bibliotecas necessarias
from sqlalchemy import Column, Integer, String, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from engine_conn import engine, Base

########## PROJETO ##########

# Criar duas Tabelas relacionadas Produto e Fornecedor.
# Cada produto tera um fornecedor. 
# Criar relações com chave estrangeira entre as tabelas.

#Exemplo Classico de criação de tabela com relação foreingn key

class Produto(Base):
    __tablename__ = 'Produto'
    id = Column(Integer, primary_key=True)
    id_fornecedor = Column(Integer, ForeignKey('Fornecedor.id_fornecedor'))
    nome_produto = Column(String)
    
class Fornecedor(Base):
    __tablename__ = 'Fornecedor'
    id_fornecedor = Column(Integer, primary_key=True)   
    nome_fornecedor = Column(String)
    produto = relationship("Produto")

#Exemplo Formas Declarativas criação de tabela com relação foreingn key 1:N


class Estado(Base):
    __tablename__ = 'estado'
    id_estado: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome_estado: Mapped[str] = mapped_column(String(100))
    cidades: Mapped[List["Cidade"]] = relationship("Cidade", back_populates="estados")


class Cidade(Base):
    __tablename__ = 'cidade'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_estado:Mapped[int] = mapped_column(Integer, ForeignKey('estado.id_estado'))
    cidade: Mapped[str] = mapped_column(String(100))
    
    estados: Mapped["Estado"] = relationship("Estado", back_populates= 'cidades')





# Cria as tabelas no banco de dados

Base.metadata.create_all(engine)


