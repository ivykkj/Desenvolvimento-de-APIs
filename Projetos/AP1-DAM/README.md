# API de Gestão Escolar com Flask

Bem-vindo à API de Gestão Escolar! Esta é uma API RESTful completa construída com Flask para gerenciar Professores, Turmas e Alunos.

A aplicação utiliza uma arquitetura modular com Blueprints, persistência de dados com SQLAlchemy em um banco SQLite, e documentação interativa gerada via Flasgger (Swagger).

## Integrantes - Grupo 9

- Cauan de Melo Silva
- Isaac do Nascimento Silva
- Leonardo Borges Soares

### Tecnologias Utilizadas
- Python
- Flask
- Flask-Cors
- SQLite
- Flask-SQLAlchemy
- Flasgger (Swagger UI)
- Docker

### Requisitos

Tenha o Docker instalado caso queria rodar o projeto num container

No diretório raiz do projeto, construa a imagem do container
```bash
docker build -t escola-api .
```
Execute o container
```bash
docker run –name escola-api-container -p 8080:8080 escola-api
```

Para rodar localmente sem ser via container tenho o Python instalado e no diretório raiz do projeto execute o comando para instalar as bibliotecas<br>

```bash
pip install -r requirements.txt
```

### Exemplos de Uso com cURL

A seguir estão exemplos de como interagir com os principais endpoints da API usando o `cURL` no seu terminal. Certifique-se de que a API esteja rodando em `http://localhost:8080` antes de executar os comandos.

#### Professores

**1. Criando um novo professor:**

```bash
curl -X POST http://localhost:8080/api/professores \
-H "Content-Type: application/json" \
-d '{
  "nome": "Carlos Alberto",
  "idade": 42,
  "materia": "Engenharia de Software",
  "observacoes": "Professor com 15 anos de experiência."
}'
```

**2. Listando todos os professores:**

```bash
curl http://localhost:8080/api/professores
```

**3. Buscando o professor com ID 1:**

```bash
curl http://localhost:8080/api/professores/1
```

**4. Atualizando o professor com ID 1:**

```bash
curl -X PUT http://localhost:8080/api/professores/1 \
-H "Content-Type: application/json" \
-d '{
  "nome": "Carlos Alberto Silva",
  "idade": 43,
  "materia": "Arquitetura de Software",
  "observacoes": "Atualização de matéria e idade."
}'
```

**5. Deletando o professor com ID 1:**

```bash
curl -X DELETE http://localhost:8080/api/professores/1
```

#### Turmas

*Observação: Para criar uma turma, o `professor_id` informado já deve existir.*

**1. Criando uma nova turma (associada ao professor de ID 1):**

```bash
curl -X POST http://localhost:8080/api/turmas \
-H "Content-Type: application/json" \
-d '{
  "descricao": "Análise e Desenv. de Sistemas - Noite",
  "ativo": true,
  "professor_id": 1
}'
```

**2. Listando todas as turmas:**

```bash
curl http://localhost:8080/api/turmas
```

**3. Buscando a turma com ID 1:**

```bash
curl http://localhost:8080/api/turmas/1
```

**4. Atualizando a turma com ID 1:**

```bash
curl -X PUT http://localhost:8080/api/turmas/1 \
-H "Content-Type: application/json" \
-d '{
  "descricao": "ADS - Turma 2025 - Noturno",
  "ativo": false,
  "professor_id": 1
}'
```

**5. Deletando a turma com ID 1:**

```bash
curl -X DELETE http://localhost:8080/api/turmas/1
```

#### Alunos

*Observação: Para criar um aluno, a `turma_id` informada já deve existir.*

**1. Criando um novo aluno (associado à turma de ID 1):**

```bash
curl -X POST http://localhost:8080/api/alunos \
-H "Content-Type: application/json" \
-d '{
  "nome": "Cauan Melo",
  "idade": 19,
  "data_nascimento": "25/02/2006",
  "nota_1_semestre": 8.5,
  "nota_2_semestre": 9.0,
  "turma_id": 1
}'
```

**2. Listando todos os alunos:**

```bash
curl http://localhost:8080/api/alunos
```

**3. Buscando o aluno com ID 1:**

```bash
curl http://localhost:8080/api/alunos/1
```

**4. Atualizando o aluno com ID 1:**

```bash
curl -X PUT http://localhost:8080/api/alunos/1 \
-H "Content-Type: application/json" \
-d '{
  "nome": "Cauan Melo Silva",
  "idade": 19,
  "data_nascimento": "25/02/2006",
  "nota_1_semestre": 8.8,
  "nota_2_semestre": 9.2,
  "turma_id": 1
}'
```

**5. Deletando o aluno com ID 1:**

```bash
curl -X DELETE http://localhost:8080/api/alunos/1
```
