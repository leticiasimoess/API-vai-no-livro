from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Rota de boas-vindas
@app.route("/", methods=["GET"])
def home():
    return "<h1>API de Doação de Livros está no ar!</h1>"

# Função para criar o banco de dados
def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS LIVROS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                imagem_url TEXT NOT NULL
            )
            """
        )
        conn.commit()

init_db()

# 📥 POST - Doar um livro
@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")

    if not titulo or not categoria or not autor or not imagem_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            INSERT INTO LIVROS (titulo, categoria, autor, imagem_url)
            VALUES (?, ?, ?, ?)
            """,
            (titulo, categoria, autor, imagem_url)
        )
        conn.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201

# 📤 GET - Listar todos os livros cadastrados
@app.route("/livros", methods=["GET"])
def listar_livros():
    with sqlite3.connect("database.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LIVROS")
        livros = cursor.fetchall()

    lista = [dict(livro) for livro in livros]
    return jsonify(lista), 200

# ❌ DELETE - Remover um livro pelo ID
@app.route("/livros/<int:livro_id>", methods=["DELETE"])
def deletar_livro(livro_id):
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM LIVROS WHERE id = ?", (livro_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"erro": "Livro não encontrado!"}), 404

    return jsonify({"mensagem": f"Livro com ID {livro_id} deletado com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
