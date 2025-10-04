from flask import request, jsonify, Blueprint
from models import db
from models.aluno import Aluno
from models.turma import Turma
from datetime import datetime

aluno_bp = Blueprint('aluno_bp', __name__)

@aluno_bp.route('/alunos', methods=['POST'])
def create_aluno():
    """
    Cria um novo aluno.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            idade:
              type: integer
            data_nascimento:
              type: string
              format: date
              example: "2005-10-20"
            nota_primeiro_semestre:
              type: number
              format: float
            nota_segundo_semestre:
              type: number
              format: float
            turma_id:
              type: integer
    responses:
      201:
        description: Aluno criado com sucesso.
      400:
        description: Turma com o ID fornecido não existe.
    """
    data = request.get_json()

    novo_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date(),
        nota_primeiro_semestre=data['nota_primeiro_semestre'],
        nota_segundo_semestre=data['nota_segundo_semestre'],
        turma_id=data['turma_id']
    )
    
    novo_aluno.calcular_media()

    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201

@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():
    """
    Retorna a lista de todos os alunos.
    ---
    responses:
      200:
        description: Lista de alunos.
        schema:
          type: array
          items:
            $ref: '#/definitions/Aluno'
    definitions:
      Aluno:
        type: object
        properties:
          id:
            type: integer
          nome:
            type: string
          idade:
            type: integer
          data_nascimento:
            type: string
            format: date
          nota_primeiro_semestre:
            type: number
            format: float
          nota_segundo_semestre:
            type: number
            format: float
          media_final:
            type: number
            format: float
          turma_id:
            type: integer
    """
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos])

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    """
    Retorna um aluno específico pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Detalhes do aluno.
        schema:
          $ref: '#/definitions/Aluno'
      404:
        description: Aluno não encontrado.
    """
    aluno = Aluno.query.get_or_404(id)
    return jsonify(aluno.to_dict())

@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    """
    Atualiza um aluno existente.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/Aluno'
    responses:
      200:
        description: Aluno atualizado com sucesso.
      400:
        description: Turma com o ID fornecido não existe.
      404:
        description: Aluno não encontrado.
    """
    aluno = Aluno.query.get_or_404(id)
    data = request.get_json()

    aluno.nome = data.get('nome', aluno.nome)
    aluno.idade = data.get('idade', aluno.idade)
    if 'data_nascimento' in data:
        aluno.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date()

    if 'turma_id' in data:
        turma = Turma.query.get(data['turma_id'])
        if not turma:
            return jsonify({'message': 'Nova turma não encontrada'}), 400
        aluno.turma_id = data['turma_id']

    aluno.nota_primeiro_semestre = data.get('nota_primeiro_semestre', aluno.nota_primeiro_semestre)
    aluno.nota_segundo_semestre = data.get('nota_segundo_semestre', aluno.nota_segundo_semestre)
    aluno.calcular_media_final()
    
    db.session.commit()
    return jsonify(aluno.to_dict())

@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    """
    Deleta um aluno.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Aluno deletado com sucesso.
      404:
        description: Aluno não encontrado.
    """
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return '', 204