from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
# Cria um conector com o banco de dados


# Para conectar a um banco de dados utilize o método create_engine com o seguinte padrão URL
# 'dialect+driver://username:password@host:port/database' (Lembrando que Dialetos são os possíveis bancos de daods)
engine = create_engine('sqlite:///sqlalchemy_basic_intro.sqlite',echo=True)

# Classe base para definições de classes pro banco de dados
base = declarative_base()

# Criação de uma tabela Alunos
class Alunos(base):
    __tablename__ = 'alunos'

    # Definição das colunas da tabela
    aluno_id = Column(Integer, primary_key = True)
    nome = Column(String)
    email = Column(String)
    ano = Column(Integer)

    def __init__(self, aluno_id,nome,email,ano):
        self.aluno_id = aluno_id
        self.nome = nome
        self.email = email
        self.ano = ano

base.metadata.create_all(engine)
    
