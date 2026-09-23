from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

RUTA_DB = r"C:\Users\kedrd\Documents\ProyectOne\TiendaDB.db"

#Get - Obtener productos
@app.route("/Producto")
def obtener_productos():
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Producto ORDER BY Id_producto DESC")
    resultados = cursor.fetchall()
    conexion.close()
        
    productos = []
    for fila in resultados:
        productos.append({
            "id": fila[0],
            "nombre": fila[1],
            "peso": fila[2],
            "tipo_unidad": fila[3],
            "iva": fila[4],
            "costo": fila[5],
            "valor_venta": fila[6],
            "descuento_producto": fila[7]
        })
    return jsonify(productos)    
    
# POST - Crear productos

@app.route("/Producto", methods=["POST"])    
def crear_productos():
    
    datos = request.get_json()
    
    conexion = sqlite3.connect(RUTA_DB)
    
    cursor = conexion.cursor()
    
    cursor.execute("""
        INSERT INTO Producto( 
            prod_nombre,
            prod_peso,
            tipo_unidad,
            porcentaje_iva,
            costo_unitario,
            valor_unitario,
            descuento_producto
            )
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,(datos["prod_nombre"],
                datos["prod_peso"],
                datos["tipo_unidad"],
                datos["porcentaje_iva"],
                datos["costo_unitario"],
                datos["valor_unitario"],
                datos["descuento_producto"]
                ))

    conexion.commit()
    
    id_producto = cursor.lastrowid
    
    conexion.close()
    
    return jsonify({"Mensaje: ": "Producto creado correctamente", "Id_producto": id_producto}),201

#PUT - Actualizar productos
@app.route("/Producto/<int:id_producto>", methods=["PUT"])
def actualizar_productos(id_producto):
    
        datos = request.get_json()
        
        conexion = sqlite3.connect(RUTA_DB)
        
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE Producto
            SET prod_nombre = ?, 
            prod_peso = ?, 
            tipo_unidad = ?, 
            porcentaje_iva = ?, 
            costo_unitario = ?,
            valor_unitario = ?,
            descuento_producto = ?
            WHERE Id_Producto = ?""",
            (datos["prod_nombre"],
                datos["prod_peso"],
                datos["tipo_unidad"],
                datos["porcentaje_iva"],
                datos["costo_unitario"],
                datos["valor_unitario"],
                datos["descuento_producto"],
                id_producto
            ))

        conexion.commit()
                             
        conexion.close()
            
        return jsonify({"Mensaje: ": "Producto actualizado correctamente", "Id_producto": id_producto}),200
    
    
#GET - Obtener Clientes    
@app.route("/Cliente") 
def obtener_cliente():
        conexion = sqlite3.connect(RUTA_DB)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Cliente")
        resultados = cursor.fetchall()
        conexion.close()
        
        clientes = []
        for fila in resultados:
            clientes.append({
                "Id_cliente": fila[0],
                "cli_nombre1": fila[1],
                "cli_nombre2": fila[2],
                "cli_apellido1": fila[3],
                "cli_apellido2": fila[4],
                "tipo_documento": fila[5],
                "num_documento": fila[6],
                "cli_direccion": fila[7],
                "cli_telefono": fila[8],
                "cli_estado": fila[9],
                "fecha_creacion": fila[10],
                "cli_descuento": fila[11]
            })
        return jsonify(clientes)  

 
#POST - Creacion de Clientes    
@app.route("/Cliente", methods=["POST"])
def crear_clientes():
        
        datos = request.get_json()
        
        conexion = sqlite3.connect(RUTA_DB)
        
        cursor = conexion.cursor()
        
        cursor.execute("""
            INSERT INTO Cliente(
                cli_nombre1,
                cli_nombre2,
                cli_apellido1,
                cli_apellido2,
                tipo_documento,
                num_documento,
                cli_direccion,
                cli_telefono,
                cli_estado,
                fecha_creacion,
                cli_descuento         
                )VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (datos["cli_nombre1"],
                datos["cli_nombre2"],
                datos["cli_apellido1"],
                datos["cli_apellido2"],
                datos["tipo_documento"],
                datos["num_documento"],
                datos["cli_direccion"],
                datos["cli_telefono"],
                datos["cli_estado"],
                datos["fecha_creacion"],
                datos["cli_descuento"]) )
    
        conexion.commit()

        id_cliente = cursor.lastrowid
        
        conexion.close()
        
        return jsonify({"Mensaje ": "Clientes nuevo creado correctamente", "Id_cliente": id_cliente}),201

#PUT - Actualizar Cliente
@app.route("/Cliente/<int:id_cliente>", methods=["PUT"])
def actualizar_clientes(id_cliente):
    
        datos = request.get_json()
        
        conexion = sqlite3.connect(RUTA_DB)
        
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE Cliente
            SET cli_nombre1 = ?,
            cli_nombre2 = ?,
            cli_apellido1 = ?,
            cli_apellido2 = ?,
            tipo_documento = ?,
            num_documento = ?,
            cli_direccion = ?,
            cli_telefono = ?,
            cli_estado = ?,
            fecha_creacion = ?,
            cli_descuento = ?
            WHERE Id_cliente = ?""",
            (datos["cli_nombre1"],
                datos["cli_nombre2"],
                datos["cli_apellido1"],
                datos["cli_apellido2"],
                datos["tipo_documento"],
                datos["num_documento"],
                datos["cli_direccion"],
                datos["cli_telefono"],
                datos["cli_estado"],
                datos["fecha_creacion"],
                datos["cli_descuento"],
                id_cliente
            ))

        conexion.commit()
                             
        conexion.close()
            
        return jsonify({"Mensaje: ": "Cliente actualizado correctamente", "Id_cliente": id_cliente}),200
    
# GET - Obtener Usuario
@app.route("/Usuario") 
def obtener_usuario():
        conexion = sqlite3.connect(RUTA_DB)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Usuario")
        resultados = cursor.fetchall()
        conexion.close()
        
        usuarios = []
        for fila in resultados:
            usuarios.append({
                "Id_usuario": fila[0],
                "usuario_nombre": fila[1],
                "usuario_apellido": fila[2],
                "usuario_estado": fila[3],
                })
        return jsonify(usuarios)  

#POST - Crear Usuario
@app.route("/Usuario", methods=["POST"])
def crear_usuario():
        
        datos = request.get_json()
                
        conexion = sqlite3.connect(RUTA_DB)
        
        cursor = conexion.cursor()
        
        cursor.execute("""
            INSERT INTO Usuario(
                usuario_nombre,
                usuario_apellido,
                usuario_estado         
                )VALUES (?, ?, ?)""",
                (datos["usuario_nombre"],
                datos["usuario_apellido"],
                datos["usuario_estado"]
                ) )
    
        conexion.commit()

        id_usuario = cursor.lastrowid
        
        conexion.close()
        
        return jsonify({"Mensaje ": "Usuario nuevo creado correctamente", "Id_usuario": id_usuario}),201
    
#PUT - Actualizar Usuario
@app.route("/Usuario/<int:id_usuario>", methods=["PUT"])
def actualizar_usuarios(id_usuario):
    
        datos = request.get_json()
        
        conexion = sqlite3.connect(RUTA_DB)
        
        cursor = conexion.cursor()
        
        cursor.execute("""
            UPDATE Usuario
            SET usuario_nombre = ?,
            usuario_apellido = ?,
            usuario_estado = ?
            WHERE Id_usuario = ?""",
            (datos["usuario_nombre"],
                datos["usuario_apellido"],
                datos["usuario_estado"],
                id_usuario
            ))

        conexion.commit()
                             
        conexion.close()
            
        return jsonify({"Mensaje: ": "Usuario actualizado correctamente", "Id_usuario": id_usuario}),200
        
# GET - Obtener Factura
@app.route("/Factura") 
def obtener_factura():
        conexion = sqlite3.connect(RUTA_DB)
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Factura")
        resultados = cursor.fetchall()
        conexion.close()
        
        facturas = []
        for fila in resultados:
            facturas.append({
                "Id_factura": fila[0],
                "Id_cliente": fila[1],
                "Id_producto": fila[2],
                "Id_usuario": fila[3],
                "fac_cantidad": fila[4],
                "descuento_fac": fila[5],
                "porcentaje_iva": fila[6],
                "valor_unitario": fila[7],
                "fac_valbruta": fila[8],
                "fac_valneta": fila[9],
                "fac_fecha": fila[10],
                })
        return jsonify(facturas)  

#POST - Crear factura
@app.route("/Factura", methods=["POST"])
def crear_factura():
        
        datos = request.get_json()
        
        
        subtotal = datos["fac_cantidad"]* datos["valor_unitario"]
        valor_descuento = subtotal * (datos["descuento_fac"]/100)
        fac_valbruta = subtotal - valor_descuento
        valor_iva = fac_valbruta * (datos["porcentaje_iva"]/100)
        fac_valneta = fac_valbruta + valor_iva
        
        conexion = sqlite3.connect(RUTA_DB)
        
        conexion.execute("PRAGMA foreign_keys = ON")
        
        cursor = conexion.cursor()
        
        cursor.execute("""
            INSERT INTO Factura(
                Id_cliente,
                Id_producto,
                Id_usuario,
                fac_cantidad,
                descuento_fac,
                porcentaje_iva,
                valor_unitario,
                fac_valbruta,
                fac_valneta,
                fac_fecha         
                )VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (datos["Id_cliente"],
                datos["Id_producto"],
                datos["Id_usuario"],
                datos["fac_cantidad"],
                datos["descuento_fac"],
                datos["porcentaje_iva"],
                datos["valor_unitario"],
                fac_valbruta,
                fac_valneta,
                datos["fac_fecha"]
                ) )
    
        conexion.commit()

        id_factura = cursor.lastrowid
        
        conexion.close()
        
        return jsonify({"Mensaje": "Factura creada correctamente", "Id_factura": id_factura}),201    
    
    
if __name__ == "__main__":
    app.run(debug=True)    