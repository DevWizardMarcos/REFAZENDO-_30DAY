
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base


#criando a conexao com o banco de dados 
engine = create_engine('sqlite:///./banco.db')

#criando a fabrica de session (a conversa com o banco de dados)
SessionLocal  = sessionmaker(bind = engine)
                            #entrada especifica entrando no egine 

Base = declarative_base()

#Criando uma classe que base registra models como tabelas do banco de dados
class User(Base):
    __tablename__ = 'users'                 # indicie
    id = Column(Integer, primary_key = True, index = True) #buscando pela id 
    nome = Column(String)
    email = Column(String)    #apenas unico
    username = Column(String, unique = True, index = True)
    senha = Column(String) # hash da senha (nao consigo voltar o valor original quando definida) = hash  →  "$2b$12$Kx8F..."
    ativo = Column(Boolean, default = True)

