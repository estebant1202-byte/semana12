#aplicar las reglas del negocio
from modelo import Producto


class ProductoServicio:

    def __init__(self, dao):
        self.dao = dao

    # 1. REGISTRAR PRODUCTO
    def registrar(self, nombre, precio, stock):

        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacio")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        producto = Producto(None, nombre.strip(), precio, stock)

        return self.dao.crear(producto)
    #2. mostrar
    def mostrar(self):
        return self.dao.mostrar()
    #3. busqueda
    def busqueda(self,id_buscar):
        if id_buscar <= 0 :
            raise ValueError("La id debe de ser un numero mayor a 0")
        return self.dao.buscar(id_buscar)
    #4. actualizacion
    def actualizacion(self, productos, id_act, nom_nuevo, pre_nuevo, sto_nuevo):
        if productos is None:
            raise ValueError("El producto debe existir")
        if id_act <= 0:
            raise ValueError("La id debe de ser un numero mayor a 0")

        # Un dato vacío significa "dejar el que ya estaba"
        nom_nuevo = nom_nuevo.strip()
        if nom_nuevo == "":
            nom_nuevo = productos[1]
        if pre_nuevo == "":
            pre_nuevo = productos[2]
        if sto_nuevo == "":
            sto_nuevo = productos[3]

        if pre_nuevo <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        if sto_nuevo < 0:
            raise ValueError("El stock no puede ser negativo")

        return self.dao.actualizar(id_act, nom_nuevo, pre_nuevo, sto_nuevo)


        return self.dao.actualizar(id_act,nom_nuevo,pre_nuevo,sto_nuevo)
    #5. eliminar
    def elimincaciones(self,id_eli):
        if id_eli <= 0 :
            raise ValueError("La id debe de ser un numero mayor a 0")
        return self.dao.eliminar(id_eli)
    #6. venta
    def ventas(self,id_b,cantidad,producto):
        if id_b <= 0 :
            raise ValueError("La id debe de ser un numero mayor a 0")
        if cantidad <= 0:
            raise ValueError("La cantidad debe de ser un numero mayor a 0")
        if producto[3] < cantidad:
            raise ValueError("La cantidad no puede ser mayor al stock")
        return self.dao.venta(id_b,cantidad)