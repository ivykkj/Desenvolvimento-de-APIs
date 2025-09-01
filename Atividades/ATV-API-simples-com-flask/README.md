# Entrega da Atividade de Desenvolvimento de APIs - GRUPO 9

## API de Gerenciamento de Usuários

Esta é uma API RESTful simples construída com o framework Flask em Python. Ela permite realizar as quatro operações básicas de CRUD (Create, Read, Update, Delete) para gerenciar um cadastro de usuários.

Os dados são armazenados em memória, o que significa que eles serão **perdidos ao reiniciar o servidor**.

## Funcionalidades

✔️ Criar novos usuários (Create)\
✔️ Listar todos os usuários (Read)\
✔️ Obter um usuário específico por ID (Read)\
✔️ Atualizar os dados de um usuário (Update)\
✔️ Excluir um usuário (Delete)

## Instalação e Execução

Siga os passos abaixo para executar a API localmente:

1.  **Clone o repositório ou baixe o arquivo `app.py`** em uma pasta de sua escolha.

2.  **Abra o terminal** e navegue até a pasta do projeto.

3.  **Instale as dependências** necessárias (neste caso, apenas o Flask):

    ```bash
    pip install Flask
    ```

4.  **Inicie o servidor da API:**

    ```bash
    python app.py
    ```

5.  Pronto\! O servidor estará rodando e a API estará disponível em `http://127.0.0.1:5000`.

-----

## Documentação dos Endpoints

A seguir estão detalhados todos os endpoints disponíveis na API.

### 1\. Criar um Novo Usuário

Cria um novo registro de usuário.

  - **URL:** `/users`
  - **Método:** `POST`
  - **Corpo da Requisição (JSON):**
    ```json
    {
      "nome": "string (obrigatório)",
      "email": "string (obrigatório)"
    }
    ```
  - **Exemplo de Uso (cURL):**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"nome": "Ana Silva", "email": "ana.silva@example.com"}' http://127.0.0.1:5000/users
    ```
  - **Respostas:**
      - **`201 Created`**: Retorna o objeto do usuário recém-criado, incluindo seu `id` gerado.
        ```json
        {
          "id": 1,
          "nome": "Ana Silva",
          "email": "ana.silva@example.com"
        }
        ```
      - **`400 Bad Request`**: Se os campos `nome` ou `email` não forem enviados.
        ```json
        {
          "error": "Dados incompletos: nome e email são obrigatórios"
        }
        ```

### 2\. Listar Todos os Usuários

Retorna a lista completa de usuários cadastrados.

  - **URL:** `/users`
  - **Método:** `GET`
  - **Exemplo de Uso (cURL):**
    ```bash
    curl http://127.0.0.1:5000/users
    ```
  - **Resposta de Sucesso (`200 OK`):**
      - Retorna um array de objetos de usuário. Se não houver usuários, retorna um array vazio `[]`.
        ```json
        [
          {
            "id": 1,
            "nome": "Ana Silva",
            "email": "ana.silva@example.com"
          },
          {
            "id": 2,
            "nome": "Carlos Souza",
            "email": "carlos@example.com"
          }
        ]
        ```

### 3\. Obter um Usuário por ID

Busca e retorna os dados de um usuário específico pelo seu `id`.

  - **URL:** `/users/<id>`
  - **Método:** `GET`
  - **Exemplo de Uso (cURL):**
    ```bash
    curl http://127.0.0.1:5000/users/1
    ```
  - **Respostas:**
      - **`200 OK`**: Retorna o objeto do usuário encontrado.
        ```json
        {
          "id": 1,
          "nome": "Ana Silva",
          "email": "ana.silva@example.com"
        }
        ```
      - **`404 Not Found`**: Se o `id` não corresponder a nenhum usuário.
        ```json
        {
          "error": "Usuário não encontrado"
        }
        ```

### 4\. Atualizar um Usuário

Atualiza os dados (`nome` e/ou `email`) de um usuário existente.

  - **URL:** `/users/<id>`
  - **Método:** `PUT`
  - **Corpo da Requisição (JSON):**
      - Envie apenas os campos que deseja alterar.
    <!-- end list -->
    ```json
    {
      "nome": "string (opcional)",
      "email": "string (opcional)"
    }
    ```
  - **Exemplo de Uso (cURL):**
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"email": "ana.silva.novo@example.com"}' http://127.0.0.1:5000/users/1
    ```
  - **Respostas:**
      - **`200 OK`**: Retorna o objeto completo do usuário com os dados atualizados.
        ```json
        {
          "id": 1,
          "nome": "Ana Silva",
          "email": "ana.silva.novo@example.com"
        }
        ```
      - **`404 Not Found`**: Se o `id` não for encontrado.

### 5\. Excluir um Usuário

Remove um usuário do sistema com base no `id` fornecido.

  - **URL:** `/users/<id>`
  - **Método:** `DELETE`
  - **Exemplo de Uso (cURL):**
    ```bash
    curl -X DELETE http://127.0.0.1:5000/users/1
    ```
  - **Respostas:**
      - **`200 OK`**: Retorna uma mensagem de confirmação.
        ```json
        {
          "message": "Usuário excluído com sucesso"
        }
        ```
      - **`404 Not Found`**: Se o `id` não for encontrado.
