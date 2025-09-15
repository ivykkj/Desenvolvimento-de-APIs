from flask import render_template, request, redirect, url_for
from models import db
from models.aluno import Aluno
from models.turma import Turma