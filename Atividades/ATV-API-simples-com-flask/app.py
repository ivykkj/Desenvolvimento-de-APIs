from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

current_id = 0

@app.route('/users', methods=['POST'])
def create_user():
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
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    data = request.get_json()
    user['nome'] = data.get('nome', user['nome'])
    user['email'] = data.get('email', user['email'])

    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404
    users = [u for u in users if u['id'] != user_id]

    return jsonify({'message': 'Usuário excluído com sucesso'}), 200

if name == 'main':

    app.run(debug=True)
