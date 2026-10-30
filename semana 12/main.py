# mostrar el menu y recibir datos
import sqlite3

from base_datos import inicializar_bd
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio

# Preparar la base de datos y las capas (el DAO se crea primero)
inicializar_bd()
dao = ProductoDAO()
servicio = ProductoServicio(dao)


def pedir_entero(mensaje):
    """Repite la pregunta hasta que el usuario escriba un entero."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Debes escribir un número entero")


def pedir_entero_opcional(mensaje):
    """Igual que pedir_entero, pero Enter devuelve "" (el servicio conserva el dato actual)."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            return ""
        try:
            return int(texto)
        except ValueError:
            print("Debes escribir un número entero")

while True:
    print("\n===== INVENTARIO DE VIDEOJUEGOS =====")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("7. Salir")
    opcion = input("Elige una opción: ").strip()

    try:
        match opcion:
            case "1":
                nombre = input("Nombre: ")
                precio = pedir_entero("Precio: ")
                stock = pedir_entero("Stock: ")
                producto = servicio.registrar(nombre, precio, stock)
                print(f"Producto registrado con ID: {producto.id}")

            case "2":
                productos = servicio.mostrar()
                if not productos:
                    print("El inventario está vacío")
                for fila in productos:
                    print(f"|id:{fila[0]}| Juego:{fila[1]}| Precio:{fila[2]}| Stock:{fila[3]}|")

            case "3":
                id_buscar = pedir_entero("ID a buscar: ")
                fila = servicio.busqueda(id_buscar)
                if fila is None:
                    print("No existe un producto con ese ID")
                else:
                    print(f"|id:{fila[0]}| Juego:{fila[1]}| Precio:{fila[2]}| Stock:{fila[3]}|")

            case "4":
                id_act = pedir_entero("ID a actualizar: ")
                fila = servicio.busqueda(id_act)
                if fila is None:
                    print("No existe un producto con ese ID")
                else:
                    print("Presiona Enter para dejar un dato igual")
                    nombre = input(f"Nombre ({fila[1]}): ")
                    precio = pedir_entero_opcional(f"Precio ({fila[2]}): ")
                    stock = pedir_entero_opcional(f"Stock ({fila[3]}): ")
                    servicio.actualizacion(fila, id_act, nombre, precio, stock)
                    print("Producto actualizado")

            case "5":
                id_eli = pedir_entero("ID a eliminar: ")
                fila = servicio.busqueda(id_eli)
                if fila is None:
                    print("No existe un producto con ese ID")
                else:
                    print(f"|id:{fila[0]}| Juego:{fila[1]}| Precio:{fila[2]}| Stock:{fila[3]}|")
                    confirmacion = input("¿Seguro que deseas eliminarlo? (s/n): ").strip().lower()
                    if confirmacion == "s":
                        servicio.elimincaciones(id_eli)
                        print("Producto eliminado")
                    else:
                        print("Eliminación cancelada")
            case "6":
                id_venta = pedir_entero("ID del videojuego: ")
                fila = servicio.busqueda(id_venta)
                if fila is None:
                    print("No existe un producto con ese ID")
                else:
                    cantidad = pedir_entero("Cantidad a vender: ")
                    servicio.ventas(id_venta, cantidad, fila)
                    print(f"Venta realizada. Stock restante: {fila[3] - cantidad}")

            case "7":
                print("Hasta luego")
                break

            case _:
                print("Opción no válida")

    except ValueError as e:
        print(f"Error: {e}")
    except sqlite3.IntegrityError:
        print("Error: la base de datos rechazó esos datos")