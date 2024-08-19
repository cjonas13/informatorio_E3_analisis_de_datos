import os
import platform

from laboratorio import (
    producto_electronicos,
    producto_vestimenta,
    Gestion_Productos,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("========== Menú de Gestión de Colaboradores ==========")
    print('1. Agregar Producto Electronico')
    print('2. Agregar Producto Vestimenta')
    print('3. Buscar Producto por Nombre')
    print('4. Eliminar Producto por ID')
    print('5. Moficiar cantidad de stock')
    
    
def agregar_producto (Gestion_Productos, tipo_producto):
  
    try:
        nombre = input('Ingrese nombre del producto: ')
        cantidad_stock = int(input('Ingrese cantidad de stock: '))
        precio = float(input('Ingrese precio del producto: '))

        if tipo_producto == '1':
            garantia = int(input('Ingrese garantia en cantidad de meses: '))
            producto = producto_electronicos(None, nombre, precio, cantidad_stock, garantia)
        elif tipo_producto == '2':
            categoria = input('Ingrese categoria de la vestimenta: ')
            producto = producto_vestimenta(None, nombre, precio, cantidad_stock, categoria)
        else:
            print('Opción inválida')
            return

        Gestion_Productos.crear_producto(producto)
        input('Presione enter para continuar ...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}') 

def encontrar_producto(nombre):
    
    resultados = Gestion_Productos.buscar_producto_por_nombre(nombre)
    if resultados:
        print("Productos encontrados:")
        for producto in resultados:
            print(producto)
    else:
        print("No se encontraron productos con ese nombre.")
    input('Presione enter para continuar...')
    
def borrar_producto (Gestion_Productos):   
    id_producto = input('Ingrese el ID del producto a eliminar: ')
    Gestion_Productos.eliminar_producto(id_producto)
    input('Presione enter para continuar...')

def modificar_cantidad_stock (Gestion_Productos):   
    id_producto = input('Ingrese el ID del producto a modificar: ')
    nuevo_stock = input ('Ingrese el nuevo Stock')
    Gestion_Productos.modificar_stock(id_producto, nuevo_stock)
    input('Presione enter para continuar...')
    
if __name__ == "__main__":
    archivo_productos = 'productos_db.json' 
    Gestion_Productos = Gestion_Productos(archivo_productos)

        
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(Gestion_Productos, opcion)
        
        elif opcion == '3':  
            nombre = input('Ingrese el nombre del producto a buscar: ')
            resultados = encontrar_producto(nombre)
        
        elif opcion == '4':    
            
            #id_producto = input('Ingrese el ID del producto a eliminar: ')
            borrar_producto (Gestion_Productos)
            input('Presione enter para continuar...')
        elif opcion == '5':    
            
            #id_producto = input('Ingrese el ID del producto a eliminar: ')
            modificar_cantidad_stock(Gestion_Productos)
            input('Presione enter para continuar...')
            
        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-2, 7)')

            input('Presione enter para continuar...')
