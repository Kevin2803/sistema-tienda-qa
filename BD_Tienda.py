import sqlite3

conexion = sqlite3.connect(r"C:\Users\kedrd\Documents\ProyectOne\TiendaDB.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM Producto")

resultado = cursor.fetchall()

for fila in resultado:
    print(fila)

conexion.close()    