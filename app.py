from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

#o GET vai pegar algo
@app.route("/", methods=["GET"])
def home():
    return "<h1>API de Doação de Livros está no ar!</h1>"


def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS LIVROS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                image_url TEXT NOT NULL
            )
            """
        )
        conn.commit()


init_db()

#o POST vai criar algo novo
@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()
    print(f" AQUI ESTÃO OS DADOS RETORNADOS DO CLIENTE {dados}")

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    with sqlite3.connect("database.db") as conn:

        conn.execute(f"""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url)
            VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
            """)

        conn.commit()

    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201


@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
            dicionario_livros = {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4]
            }
            livros_formatados.append(dicionario_livros)
    

    return jsonify(livros_formatados)


#o PUT vai mudar algo
@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado enviado"}), 400

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    with sqlite3.connect("database.db") as conn:
        resultado = conn.execute
        (f""" 
        UPDATE LIVROS
         SET titulo = "{titulo}", categoria = "{categoria}", autor = "{autor}", image_url = "{image_url}" WHERE id = {id}
        """)

        conn.commit()
        return jsonify({"mensagem": "Livro atualizado com sucesso!"}), 200

# o DELETE vai apagar algo
@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    with sqlite3.connect("database.db") as conn:
        resultado = conn.execute("DELETE FROM LIVROS WHERE id = ?", (id,))
        conn.commit()

        if resultado.rowcount == 0:
            return jsonify({"erro": "Livro não encontrado"}), 404

    return jsonify({"mensagem": "Livro deletado com sucesso!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
