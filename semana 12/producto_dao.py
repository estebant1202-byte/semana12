#ejecutar las operaciones sql
from base_datos import obtener_conexion
from modelo import Producto

class ProductoDAO:
    #1. crear un producto
    def crear(self, producto):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            sql = """ 
                INSERT INTO productos (nombre, precio, stock)
                VALUES (?, ?, ?)
            """
            cursor.execute(sql,(producto.nombre, producto.precio, producto.stock))
            producto.id = cursor.lastrowid
            conexion.commit()
        finally:
            conexion.close()
        return producto
    #2.mostrar porductos
    def mostrar(self):
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql = "SELECT * FROM productos"
            cursor.execute(sql)
            productos = cursor.fetchall()
        finally:
            conexion.close()
        return productos

    #3. Buscar videojuego
    def buscar(self,id_buscar):
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql = "SELECT * FROM productos WHERE id = ?"
            cursor.execute(sql,(id_buscar,))
            productos = cursor.fetchone()
        finally:
            conexion.close()
            if productos != None:
                return productos
            else:
                return None
    #4. actualizar videojuego
    def actualizar(self,id_act,nom_nuevo,pre_nuevo,sto_nuevo):
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql_2 = """UPDATE productos
                        SET nombre = ?,precio = ?, stock = ?
                        WHERE id = ?
                        """
            cursor.execute(sql_2,(nom_nuevo,pre_nuevo,sto_nuevo,id_act))
            conexion.commit()
        finally:
            conexion.close()
    #5 Eliminar
    def eliminar(self,id_eli):
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql ="""DELETE FROM productos
                    WHERE id= ?
                    """
            cursor.execute(sql,(id_eli,))
            conexion.commit()
        finally:
            conexion.close()
    #6 venta de unidades
    def venta(self,id_b,cantidad):
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql ="""UPDATE productos
                    SET stock = stock - ? 
                    WHERE id = ?
                    """
            cursor.execute(sql,(cantidad,id_b))
            conexion.commit()
        finally:
            conexion.close()