from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
#Conectar ao SQLite em memoria

engine = create_engine('sqlite:///meubanco.db', echo =True)

print("Conexão com SQLite estabelecida.")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)



# Cria as tabelas no banco de dados

Base.metadata.create_all(engine)