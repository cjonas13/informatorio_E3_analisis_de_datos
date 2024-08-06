import json
'''


Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

-ok-Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
-Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
-Implementar operaciones CRUD para gestionar productos del inventario.
-ok-Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
-Persistir los datos en archivo JSON.
'''
#----------------------------definición de clase base-----------------------------#
class Productos:
    def __init__ (self, id, nombre, precio, cantidad_stock):
        self.__id = id
        self.__nombre = nombre
        self.__precio = self.validar_precio (precio)
        self.__cantidad_stock = self.validar_cantidad (cantidad_stock)
        
    @property
    def id(self):
        return self.__id
    @property
    def nombre (self):
        return self.__nombre
    
    @property
    def precio (self):
        return self.__precio
    
    @property
    def cantidad_stock (self):
        return self.__cantidad_stock
    
#-------------------------------------------------------------------------------
#-----control de datos -----#
    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id
        
    @cantidad_stock.setter
    def cantidad_stock (self, nueva_cantidad_stock):
        self.__cantidad_stock = self.validar_cantidad (nueva_cantidad_stock)
        
    def validar_cantidad (self, stock):
        try:
            cantidad_stock = int (stock)
            if cantidad_stock < 0:
                raise ValueError ("la cantidad stock debe ser un número positivo")
            return cantidad_stock
        except ValueError:
            raise ValueError("la cantidad debe ser un número valido mayor a cero")
    
    @precio.setter
    def precio (self, nuevo_precio):
        self.__precio = self.validar_precio (nuevo_precio)
        
    def validar_precio (self, valor):
        try:
            valor_producto = float (valor)
            if valor_producto < 0:
                raise ValueError ("el valor debe ser un número positivo")
            return valor_producto
        except ValueError:
            raise ValueError("el valor debe ser un número valido mayor a cero")
            
#------crea diccionario para guarda en json-------------------#
    def to_dict(self):
        return{
            "id": self.__id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad_stock": self.cantidad_stock
        }
        
    def __str__(self):
        return f"{self.__id}{self.__nombre} {self.__precio} {self.__cantidad_stock}"
        
#---------subclases------------------------#
class Producto_Electronicos (Productos):
    def __init__(self, id, nombre, precio, cantidad_stock, garantia):
        super().__init__(id, nombre, precio, cantidad_stock)
        self.__garantia = self.validar_garantia (garantia)
                
    @property
    def garantia (self):
        return self.__garantia
    
    def validar_garantia (self, meses):
        try:
            cantidad_garantia = int (meses)
            if cantidad_garantia < 0:
                raise ValueError ("la cantidad debe ser un número positivo")
            return cantidad_garantia
        except ValueError:
            raise ValueError("la cantidad debe ser un número valido mayor a cero")
        
    @garantia.setter
    def garantia (self, nueva_garantia):
        self.__garantia = self.validar_garantia (nueva_garantia)
        
    def to_dict(self):
        data = super().to_dict()
        data ['Garantia'] = self.__garantia
        return data
    
    def __str__(self):
        return f"{super().__str__()} - Garantia: {self.__garantia}"
    
   
class Producto_Vestimenta (Productos):
    def __init__(self, id, nombre, precio, cantidad_stock, categoria):
        super().__init__(id, nombre, precio, cantidad_stock)
        self.__categoria = categoria
                
    @property
    def categoria (self):
        return self.__categoria
    '''
   hacer algun control sobre categorias
       ''' 
    @categoria.setter
    def categoria (self, nueva_categoria):
        self.__categoria = nueva_categoria
        
    def to_dict(self):
        data = super().to_dict()
        data ['Categoria'] = self.__categoria
        return data
    
    def __str__(self):
        return f"{super().__str__()} - Categoria: {self.__categoria}"
   
   
   
   
#------gestion de productos-----------#    
class Gestion_Productos:
    def __init__(self,archivo):
        self.archivo = archivo
        self.productos = self.leer_datos()
    
    def leer_datos (self):
        try:
            with open (self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return{}
        except Exception as error:
            raise Exception (f'Error inesperado al leer datos del archivo: {error}')
        else:   
            return datos
    
    def guardar_datos(self):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(self.productos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')
    
    
    def crear_producto(self, producto):
        try:
            id = self.obtener_nuevo_id()
            producto.id = id
            self.productos[str(id)] = producto.to_dict()
            self.guardar_datos()
            print(f"Producto {producto.nombre} creado correctamente con ID {id}.")
        except Exception as error:
            print(f'Error inesperado al crear colaborador/producto: {error}')

    def obtener_nuevo_id(self):
        if not self.productos:
            return 1
        else:
            ids = [int(id) for id in self.productos.keys()]
            return max(ids) + 1