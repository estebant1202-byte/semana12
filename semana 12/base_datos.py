# gestionar la conexion y crear la tabla
import sqlite3

def obtener_conexion():
    conexion = sqlite3.connect("tienda.db")
    return conexion

def inicializar_bd():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio INTEGER NOT NULL CHECK (precio > 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
        )
    """)
    
    conexion.commit()
    conexion.close()

