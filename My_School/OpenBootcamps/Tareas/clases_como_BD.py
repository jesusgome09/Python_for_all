class Categorias:
    idCategoria = 0
    nombre = ""

class Proveedores:
    idProveedor = 0
    nombre = "Ara"
    direccion = ""
    telefono = ""

class Productos:
    idProducto = 0
    categoriaProducto = Categorias()
    precio = 0
    tamaño = 0
    tipoDeProducto = None
    CIFProveedor = Proveedores()
    email = ""

p = Productos()
print(p.CIFProveedor.nombre)