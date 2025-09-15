from models import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Aluno(db.Model):
    pass

#to do: criar tabela, seus dados e seu relacionamento