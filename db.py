from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

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
        id = Column(Integer, primary_key = True)
        nome = Column(String)
        email = Column(String)
        ano = Column(Integer)
        
        # Construtor do objeto Alunos
        def __init__(self, params):
            self.nome = params['nome']
            self.email = params['email']
            self.ano = params['ano']

    def insert(self,Table,params):
        tr = Table(params)
        self.session.add(tr)
        self.session.commit()

    def delete(self,Table,id):
        tr = self.session.query(Table).filter(Table.id == id).first()
        if tr != None:
            self.session.delete(tr)
            self.session.commit()

if __name__ == '__main__':
    # Para conectar a um banco de dados utilize o método create_engine com o seguinte padrão URL
    # 'dialect+driver://username:password@host:port/database' (Lembrando que Dialetos são os possíveis bancos de daods)
    bd = BancoDeDados('sqlite:///teste.sqlite',echo=True)

    # Inserindo novos alunos no banco de dados
    bd.insert(bd.Alunos,{'nome':'Yuri Dimitri Ramos Costa','email':'yuridrcosta@gmail.com','ano':16})
    bd.insert(bd.Alunos,{'nome':'Teste','email':'teste@example.com','ano':5})
    bd.insert(bd.Alunos,{'nome':'Teste2','email':'teste2@example.com','ano':5})
    bd.insert(bd.Alunos,{'nome':'Joao','email':'joao@example.com','ano':11})

    print('Realizando uma busca por alunos que estão no ensino médio')
    for a in bd.session.query(bd.Alunos).filter(bd.Alunos.ano > 9):
        print(f'[ {a.id} ] {a.nome}\t{a.email}\t{a.ano}')

    # Removendo alunos do banco de dados pelo nome
    aluno = bd.session.query(bd.Alunos).filter(bd.Alunos.nome == 'Teste').first()
    if aluno != None:
        bd.session.delete(aluno)
        bd.session.commit()

    # Removendo alunos pelo id
    bd.delete(bd.Alunos,3)

