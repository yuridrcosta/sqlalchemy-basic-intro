import tables
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=tables.engine)
session = Session()

# Obtem todos os dados
for s in session.query(tables.Alunos).all():
    print(f'[ {s.aluno_id} ] {s.nome}\t{s.email}\t{s.ano}')


print('\n\nAlunos que já passaram do ensino médio: ')

for s in session.query(tables.Alunos).filter(tables.Alunos.ano > 9):
    print(f'[ {s.aluno_id} ] {s.nome}\t{s.email}\t{s.ano}')
