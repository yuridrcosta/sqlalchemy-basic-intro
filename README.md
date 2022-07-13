# Introdução

**SQLAlchemy** é um uma biblioteca Python que nos permite operar bancos de dados em um nível mais alto, transformando classes Python em tabelas. Se trata de uma técnica conhecida como Object Relational Mapping (ORM).

Com o SQLAlchemy é possível usar bancos de dados **PostgreSQL**, **MySQL** (ou **MariaDB**), **SQLite**, **Oracle** e **Microsoft SQL Server**.

Mais informações podem ser encontradas em: www.sqlalchemy.org.

---

O arquivo `tables.py` demonstra como criar/utilizar um banco de dados SQLite utilizando SQLAlchemy. Mostra também como criar uma tabela chamada alunos. Já o arquivo `insert.py` mostra como inserir uma instância em uma tabela, assim como `delete.py` mostra como deletar uma instância de uma tabela.

Um exemplo de estruturação em classes para lidar com um banco de dados está disponível no arquivo `db.py`.

# Instalação 

````{:.py}
pip install sqlalchemy
````