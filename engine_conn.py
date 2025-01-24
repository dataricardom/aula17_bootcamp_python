from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Cria a conexão com o banco.

engine = create_engine('sqlite:///meubanco.db', echo =True)

Session = sessionmaker(bind=engine)

#Instanciando 
Base = declarative_base()