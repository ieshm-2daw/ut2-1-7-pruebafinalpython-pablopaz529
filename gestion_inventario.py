"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Pablo Paz Fernández
Fecha: 04/11/2025

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, nombre, contacto):
        # TODO: definir los atributos de la clase
        self.nombre = nombre
        self.contacto = contacto
        

    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        return f"Proveedor -> {self.nombre} - {self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        # TODO: definir los atributos de la clase
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor
        

    def __str__(self):
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        return f"[{self.codigo}] {self.nombre} - {self.precio} ({self.stock}) | Proveedor: {self.proveedor}"


# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        # TODO: definir los atributos e inicializar la lista de productos
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        if os.path.exists(self.nombre_fichero):
            try:
                with open(self.nombre_fichero, "r") as f:
                    datos_cargados = json.load(f)
                    self.productos = []

                    for t in datos_cargados:

                        proveedor = Proveedor(t["proveedor"]["nombre"], t["proveedor"]["contacto"])

                        producto = Producto(t["codigo"], t["nombre"], t["precio"], t["stock"], proveedor)

                        self.productos.append(producto)

                    
                    print("Datos cargados con éxito")

            except FileNotFoundError:
                print("Error al cargar datos.")
        
        else:
            print("No existe ningún fichero")

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        try:
            with open(self.nombre_fichero, "w", encoding="UTF-8") as e:
                json.dump([t.__dict__ for t in self.productos], e , indent=4, ensure_ascii=False)
                print("Datos cargados correctamente.")

        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo

        if producto in self.productos:
            print("El producto ya existe")
        else:
            self.productos.append(producto)
            print("Producto añadido")
            print(producto)

    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados
        for p in self.productos:
            print(p)

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código
        for p in self.productos:
            if p.codigo.lower() == codigo.lower:
                return p
            else:
                return None
        

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos

        for p in self.productos:
            if p.codigo.lower() == codigo.lower():
                
                if nombre:
                    nombreNuevo = nombre
                if precio:
                    precioNuevo = precio
                if stock:
                    nuevoStock = stock

            productoModificado = Producto(codigo, nombre = nombreNuevo or nombre, precio = precioNuevo or precio, stock = nuevoStock or stock)

            return productoModificado
        
        else:
            print("ERROR: No existe ningún producto con ese código")
                
        

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        pass

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        """
        # TODO: devolver la suma total del valor del stock
        pass

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        pass


# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida

    inventario = Inventario("inventario.json")
    inventario.cargar()

    while (True):

        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = int(input("Seleccione una opción: "))

        # TODO: implementar las acciones correspondientes a cada opción del menú

        if opcion == 1:

            codigo = input("Código del producto: ")

            for t in inventario.productos:
                if t.codigo.lower() == codigo.lower():
                    print("Error, ya existe un producto con ese código. Vuelva a intentarlo")
                    
                    while(t.codigo.lower() == codigo.lower()):
                        codigo = input("Vuelve a introducir el código del producto: ")


            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock del producto: "))

            print("DATOS DEL PROVEEDOR")
            proveedor_nombre = input("Nombre del proveedor: ")
            proveedor_contacto = input("Contacto del proveedor: ")
            
            proveedor = Proveedor(proveedor_nombre, proveedor_contacto)

            producto = Producto(codigo, nombre, precio, stock, proveedor)

            inventario.anadir_producto(producto)

        elif opcion == 2:

            inventario.mostrar()
            
        elif opcion == 3:

            #cod = input("Introduzca el código del producto a buscar: ")
            #inventario.buscar(cod)
            pass

        elif opcion == 4:
            #cod = input("Introduzca el código del producto a buscar: ")
            #nombre = input("Nombre ")
            

            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:

            inventario.guardar()
            print("Finalizando programa...")
            break


if __name__ == "__main__":
    main()
