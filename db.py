from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# Classe base para definições de classes pro banco de dados

class BancoDeDados:

    base = declarative_base()
    engine = None
    session = None

    def __init__(self, database_url,echo=True):
        self.engine = create_engine(database_url,echo=echo)
        self.base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        self.session = session

    # Criação de uma tabela Alunos
    class Alunos(base):
        __tablename__ = 'alunos'

        # Definição das colunas da tabela
        aluno_id = Column(Integer, primary_key = True)
        nome = Column(String)
        email = Column(String)
        ano = Column(Integer)
        
        # Construtor do objeto Alunos
        def __init__(self, params):
            self.aluno_id = params['aluno_id']
            self.nome = params['nome']
            self.email = params['email']
            self.ano = params['ano']

    def insert(self,Table,params):
        tr = Table(params)
        self.session.add(tr)
        self.session.commit()

if __name__ == '__main__':
    # Para conectar a um banco de dados utilize o método create_engine com o seguinte padrão URL
    # 'dialect+driver://username:password@host:port/database' (Lembrando que Dialetos são os possíveis bancos de daods)
    bd = BancoDeDados('sqlite:///teste.sqlite',echo=True)
    bd.insert(bd.Alunos,{'aluno_id':1,'nome':'Yuri Dimitri Ramos Costa','email':'yuridrcosta@gmail.com','ano':16})
