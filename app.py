from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="musicpro"
)

@app.route("/")
def index():
    return 5000

@app.route("/productos", methods=["GET"])
def productos():
    cursor = con.cursor()
    query = "SELECT * FROM producto;"
    cursor.execute(query)
    query_result = cursor.fetchall()
    productos = []
    for p in query_result:
        productos.append({
            'codigo': p[0],
            'nombre': p[1],
            'descripcion': p[2],
            'precio': p[3],
            'stock': p[4],
            'imagen': p[5],
            'id_categoria': p[6],
        })
    return jsonify(productos)

@app.route("/actualizar", methods=["PUT"])
def actualizar():
    codigo = int(request.args.get("codigo"))
    nuevo_precio = int(request.args.get("nuevo_precio"))
    cursor = con.cursor()
    query = f"UPDATE producto SET precio = {nuevo_precio} WHERE codigo = {codigo};"
    cursor.execute(query)
    con.commit()
    return "PRODCUTO ACTUALIZADO"

if __name__ == "__main__":
    app.run(debug=True)