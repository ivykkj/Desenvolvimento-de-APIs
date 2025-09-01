from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Cada classe que herda de db.Model se torna uma tabela no banco de dados.
class User(db.Model): # Declaração de um novo modelo/tabela: User
    id = db.Column(db.Integer, primary_key=True) # Define uma coluna ... 
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # define o nome da tabela no banco de dados para a classe User como "users", como boas práticas
    __tablename__ = 'users'