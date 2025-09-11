from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app, template={
    "info":{
        "title": "Minha API Flask",
        "description": "API feita com Flask e documentação Swagger",
        "version": "1.0.0",
    }
})

users = []
current_id = 0

@app.route('/users', methods=['POST'])
def create_user():
    """
    Cria um novo Usuário
    ---
    tags:
        - Usuários
    description: Cria um novo usuário com nome e email
    consume:
        - application/json
    produce:
        - application/json
    parameters:
        - in: body
        name: users
        description: Objeto json com os dados do Usuário
        required: True
        schema:
            id: UserInput
            type: object
            required:
                - nome
                - email
            properties:
                nome:
                    type: string
                    example: João Silva
                email:
                    type: string
                    example: joao@email.com
    responses:
        201:
            description: Usuário criado com sucesso
            schema:
                id: UserOutput
                type: object
                properties:
                    id:
                        type: integer
                        example: 1
                    nome:
                        type: string
                        example: João Silva
                    email:
                        type: string
                        example: joao@email.com
        400:
            description: Requisição Inválida, faltando nome ou email
            schema:
                type: object
                properties:
                    error:
                        type: string
                        example: "nome e email são obrigatótios"
    """
    global current_id
    data = request.get_json()
    if not data or 'nome' not in data or 'email' not in data:
        return jsonify({'error': 'Dados incompletos: nome e email são obrigatórios'}), 400
    current_id += 1
    new_user = {
        'id': current_id,
        'nome': data['nome'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users', methods=['GET'])
def get_users():
    """
    Lista todos os Usuários
    ---
    tags:
        - Usuários
    description: retorna todos os usuários informando id, nome e email
    responses:
        200:
            description: Lista de usuários retornada com sucesso
            schema:
                type: array
                items:
                    $ref: '#/definitions/UserOutput' 
    """
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Busca um usuário específico pelo ID
    ---
    tags:
        - Usuários
    description: Busca um usuário na lista com base no ID
    parameters:
        - name: user_id
        in: path
        type: integer
        required: true
        description: O ID do usuário a ser buscado
    responses:
        200:
            description: Dados do usuário retornados com sucesso
            schema:
                $ref: '#/definitions/UserOutput'
        404:
            description: Requisição inválida, usuário não encontrado
            schema:
                type: object
                properties:
                    error:
                        type: string
                        example: "ID inválido"
    """
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Atualiza os dados de um usuário
    ---
    tags:
        - Usuários
    description: Busca um usuário pelo ID e atualiza seus dados
    parameters:
        - name: user_id
        in: path
        type: integer
        required: true
        description: o ID do usuário a ser atualizado
        - name: body
        in: body
        required: true
        schema:
            id: UserUpdateInput
            type: object
            properties:
                nome:
                    type: string
                    example: João da Silva
                email:
                    type: string
                    example: joao.silva@email.com
    responses:
        200:
            description: Usuário atualizado com sucesso
            schema:
                $ref: '#/definitions/UserOutput'
        404:
            description: Requisição inválida, usuário não encontrado
            schema:
                type: object
                properties:
                    error:
                        type: string
                        example: "ID inválido"
    """
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    data = request.get_json()
    user['nome'] = data.get('nome', user['nome'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Exclui um usuário do sistema
    ---
    tags:
        - Usuários
    description: Exclui um usuário com base no ID forncido
    parameters:
        - name: user_id
        in: path
        type: integer
        required: true
        description: o ID do usuário a ser excluído
    responses:
        200:
            description: Usuário excluído com sucesso
            schema:
                type: object
                properties:
                    message:
                        type: string
        404:
            description: Requisição inválida, usuário não encontrado
            schema:
                type: object
                properties:
                    error:
                        type: string
                        example: "ID inválido"
    """
    global users
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'Usuário excluído com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)