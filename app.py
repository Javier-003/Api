from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql3.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql3683292'
app.config['MYSQL_PASSWORD'] = 'yQ5n5f8g7k'
app.config['MYSQL_DB'] = 'sql3683292'

conexion = MySQL(app)
@app.route ('/')
def api():
    return "<h1>Api de Agricomex</h1>"


@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM productos")
    datosDB = cursor.fetchall()
    # convertir los datos a una lista de diccionarios
    productos = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        productos.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(productos)

@app.route('/api/productos/<nombre>', methods=['GET'])
def obtener_productos_por_nombre(nombre):
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre=%s",(nombre,))
    datosDB = cursor.fetchall()
    # convertir los datos a una lista de diccionarios
    productos = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        productos.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(productos)
    
    
@app.route('/api/calendario', methods=['GET'])
def obtener_calendario():
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM calendario_fertilidad")
    datosDB = cursor.fetchall()
    # convertir los datos a una lista de diccionarios
    calendario = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        calendario.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(calendario)

@app.route('/api/calendario/<estado>', methods=['GET'])
def obtener_calendario_por_estado(estado):
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM calendario_fertilidad WHERE estado = %s", (estado,))
    datosDB = cursor.fetchall()
    calendario = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        calendario.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(calendario)
    
    
@app.route('/api/suelos', methods=['GET'])
def obtener_suelos():
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM suelos")
    datosDB = cursor.fetchall()
    # convertir los datos a una lista de diccionarios
    suelos = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        suelos.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(suelos)

@app.route('/api/suelos/<estado>', methods=['GET'])
def obtener_suelos_por_estado(estado):
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM suelos WHERE estado = %s", (estado,))
    datosDB = cursor.fetchall()
    suelos = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        suelos.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(suelos)
    
    
@app.route('/api/tiendas', methods=['GET'])
def obtener_tiendas():
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM tiendas")
    datosDB = cursor.fetchall()
    # convertir los datos a una lista de diccionarios
    tiendas = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        tiendas.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(tiendas)
    
    
@app.route('/api/plagas', methods=['GET'])
def obtener_plagas():
    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM plagas")
    datosDB = cursor.fetchall()
    # convertir los datos a una lista de diccionarios
    plagas = []
    columnName = [column[0] for column in cursor.description]
    for registro in datosDB:
        plagas.append(dict(zip(columnName, registro)))   
    cursor.close()
    return jsonify(plagas)
    
    
    

if __name__ == '__main__':
    app.run(debug=True)