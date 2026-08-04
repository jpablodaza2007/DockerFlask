import pymysql
from flask import Flask, render_template, request, redirect

sample = Flask(__name__)

def conectar():
    return pymysql.connect(
        host="servidor-bd",
        user="root",
        password="sena123",
        database="adso_db",
        cursorclass=pymysql.cursors.DictCursor
    )

@sample.route("/")
def home():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM aprendices ORDER BY id DESC")
    aprendices = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", aprendices=aprendices)

@sample.route("/registrar", methods=["POST"])
def registrar():

    nombre = request.form["nombre_completo"]
    documento = request.form["numero_documento"]
    ficha = request.form["ficha"]

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO aprendices
    (nombre_completo, numero_documento, ficha)
    VALUES (%s,%s,%s)
    """

    cursor.execute(sql, (nombre, documento, ficha))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)