# 📚 Api Doação de Livros

 Projeto desenvolvido para fins didáticos durante o aprendizado de APIs, Python e Banco de Dados. A proposta é colocar em prática os principais conceitos de criação de uma API, integração com banco de dados SQLite3 e MySQL, e testes utilizando o Postman.

# 🚀 Tecnologias Utilizadas
  - Python 3

  - SQLite3

  - MySQL

  - Postman

  - Flask 

  - JSON

# 📖 Objetivo do Projeto
O objetivo do projeto é criar uma API simples para gerenciar um acervo de livros, permitindo:

📌 Adicionar livros

📌 Listar todos os livros

📌 Atualizar livros

📌 Deletar livros

Tudo isso integrado a um banco de dados, praticando a manipulação de dados e o uso de rotas HTTP (GET, POST, PUT e DELETE).

# 🗃 Banco de Dados
O projeto permite o uso de dois tipos de banco de dados:

✅ SQLite3 — para praticar localmente e entender a manipulação de bancos relacionais simples.

✅ MySQL — para ter o primeiro contato com um banco mais robusto, simular um ambiente mais próximo ao real e entender a diferença entre os dois.

# 🧪 Testes com Postman
As rotas da API foram testadas utilizando o Postman, proporcionando o aprendizado na criação de requisições HTTP e interpretação de respostas da API.

# Rotas Disponíveis
GET / — Exibe uma mensagem simples de boas-vindas.

GET /livros — Lista todos os livros cadastrados no banco de dados.

POST /doar — Adiciona um novo livro no banco de dados.

PUT /livros/{id} — Atualiza as informações de um livro específico.

DELETE /livros/{id} — Deleta um livro específico.

# 🔧 Como Executar o Projeto
Clone o repositório:
  - git clone https://github.com/leticiasimoess/API-vai-no-livro.git

Acesse a pasta do projeto:
  - cd API-vai-no-livro

Instale as dependências (se houver):
  - pip install -r requirements.txt

Execute o projeto:
  - python app.py

Abra o Postman e teste as rotas disponíveis.

# 👩‍💻 Feito por
Projeto desenvolvido por Letícia Simões  para fins educacionais.
