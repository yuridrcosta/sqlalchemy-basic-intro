import tables
import tables
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=tables.engine)
session = Session()

# Busca o aluno pelo nome
aluno = session.query(tables.Alunos).filter(tables.Alunos.nome == 'Teste User').first()
session.delete(aluno)
# Realiza o commit das mudanças no banco
session.commit()