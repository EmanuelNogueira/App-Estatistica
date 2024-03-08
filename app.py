# app.py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "relampagomarquinhos"

@app.route("/")
def home():
    return render_template("Lista.html", titulo="Lista de Chamadas")

@app.route("/form")
def new():
    return render_template("form.html", titulo="Nova Chamada")

@app.route("/formestatistica")
def formestatistica():
    # Adicione a lógica de login conforme necessário
    return render_template("formestatistica.html")


@app.route("/estatisticas")
def estatisticas():
    # Adicione a lógica de login conforme necessário
    return render_template("estatisticas.html")




if __name__ == "__main__":
    app.run(debug=True)
