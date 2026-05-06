
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import sessionmaker, declarative_base


#criando a conexao com o banco de dados 
engine = create_engine('sqlite:///./banco.db')

#criando a fabrica de session (a conversa com o banco de dados)
SessionLocal  = sessionmaker(bind = engine)
                            #entrada especifica entrando no egine 

Base = declarative_base()

#Criando uma classe que base registra models como tabelas do banco de dados
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    nome = Column(String)