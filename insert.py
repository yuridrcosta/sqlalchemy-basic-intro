import tables
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=tables.engine)
session = Session()

aluno = tables.Alunos(1,'Yuri Dimitri','yuridrcosta@gmail.com',16)
session.add(aluno)

aluno = tables.Alunos(2,'Teste User','teste@example.com',2)
session.add(aluno)

aluno = tables.Alunos(3,'João','joao@example.com',9)
session.add(aluno)

aluno = tables.Alunos(4,'Maria','maria@example.com',12)
session.add(aluno)

session.commit()