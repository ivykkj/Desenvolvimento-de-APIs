import os
from flask import Flask
from config import Config
from flasgger import Swagger
from controllers.aluno_controller import AlunoController
from controllers.professor_controller import ProfessorController
from controllers.turma_controller import TurmaController
from models import db
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma

app = Flask(__name__)
swagger = Swagger(app, template={
    "info":{
        "title": "Minha API Flask",
        "description": "API completa em Flask, estruturada em MVC",
        "version": "1.0.0",
    }
})

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8080)