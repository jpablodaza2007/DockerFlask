import pymysql
from flask import Flask

sample = Flask(__name__)

@sample.route("/")
def home():
    try:
        conn = pymysql.connect(
            host="servidor-bd",
            user="root",
            password="sena123",  # nosec B106
            database="adso_db"
        )
        conn.close()
        return "<h1>Conexión exitosa a la base de datos</h1>"
    except Exception as e:
        return f"<h1>Error de conexión</h1><p>{e}</p>"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)  