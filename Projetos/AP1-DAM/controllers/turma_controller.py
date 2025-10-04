from flask import request, jsonify, Blueprint
from models import db
from models.turma import Turma
from models.professor import Professor

turma_bp = Blueprint('turma_bp', __name__)

@turma_bp.route('/turmas', methods=['POST'])
def create_turma():
    """
    Cria uma nova turma.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
            ativo:
              type: boolean
            professor_id:
              type: integer
    responses:
      201:
        description: Turma criada com sucesso.
      400:
        description: Professor com o ID fornecido não existe.
    """
    data = request.get_json()

    professor = Professor.query.get(data['professor_id'])
    if not professor:
        return jsonify({'message': 'Professor não encontrado'}), 400

    nova_turma = Turma(
        descricao=data['descricao'],
        ativo=data.get('ativo', True),
        professor_id=data['professor_id']
    )
    db.session.add(nova_turma)
    db.session.commit()
    return jsonify(nova_turma.to_dict()), 201

@turma_bp.route('/turmas', methods=['GET'])
def get_turmas():
    """
    Retorna a lista de todas as turmas.
    ---
    responses:
      200:
        description: Lista de turmas.
        schema:
          type: array
          items:
            $ref: '#/definitions/Turma'
    definitions:
      Turma:
        type: object
        properties:
          id:
            type: integer
          descricao:
            type: string
          ativo:
            type: boolean
          professor_id:
            type: integer
    """
    turmas = Turma.query.all()
    return jsonify([t.to_dict() for t in turmas])

@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    """
    Retorna uma turma específica pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Detalhes da turma.
        schema:
          $ref: '#/definitions/Turma'
      404:
        description: Turma não encontrada.
    """
    turma = Turma.query.get_or_404(id)
    return jsonify(turma.to_dict())

@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    """
    Atualiza uma turma existente.
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
          $ref: '#/definitions/Turma'
    responses:
      200:
        description: Turma atualizada com sucesso.
      400:
        description: Professor com o ID fornecido não existe.
      404:
        description: Turma não encontrada.
    """
    turma = Turma.query.get_or_404(id)
    data = request.get_json()

    if 'professor_id' in data:
        professor = Professor.query.get(data['professor_id'])
        if not professor:
            return jsonify({'message': 'Novo professor não encontrado'}), 400
        turma.professor_id = data['professor_id']

    turma.descricao = data.get('descricao', turma.descricao)
    turma.ativo = data.get('ativo', turma.ativo)
    
    db.session.commit()
    return jsonify(turma.to_dict())

@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    """
    Deleta uma turma.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Turma deletada com sucesso.
      404:
        description: Turma não encontrada.
    """
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    return '', 204