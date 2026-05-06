from sqlalchemy import create_engine 
from sqlalchemy import sessionmaker

#criando a conexao com o banco de dados 
egine = create_engine('sqlite:///./banco.db')

#criando a fabrica de session (a conversa com o banco de dados)
sessionLocal = sessionmaker(bind = egine)
                            #entrada especifica entrando no egine 