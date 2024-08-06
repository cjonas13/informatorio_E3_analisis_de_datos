import os
import platform

from laboratorio import (
    Producto_Electronicos,
    Producto_Vestimenta,
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
    
    
def agregar_producto (gestion_productos, tipo_producto):
  
    try:
        nombre = input('Ingrese nombre del producto: ')
        cantidad_stock = int(input('Ingrese cantidad de stock: '))
        precio = float(input('Ingrese precio del producto: '))

        if tipo_producto == '1':
            garantia = int(input('Ingrese garantia en cantidad de meses: '))
            producto = Producto_Electronicos(None, nombre, precio, cantidad_stock, garantia)
        elif tipo_producto == '2':
            categoria = input('Ingrese categoria de la vestimenta: ')
            producto = Producto_Vestimenta(None, nombre, cantidad_stock, precio, categoria)
        else:
            print('Opción inválida')
            return

        gestion_productos.crear_producto(producto)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}') 
    
if __name__ == "__main__":
    archivo_productos = 'productos_db.json'
    gestion_productos = Gestion_Productos(archivo_productos)

    '''while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == "2":
            agregar_producto (gestion_productos, opcion)
        
        
        
        elif opcion == '3':
            buscar_colaborador_por_dni(gestion)

        elif opcion == '4':
            actualizar_salario_colaborador(gestion)

        elif opcion == '5':
            eliminar_colaborador_por_dni(gestion)

        elif opcion == '6':
            mostrar_todos_los_colaboradores(gestion)

        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
        '''
        
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_producto(gestion_productos, opcion)
        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-2, 7)')

        input('Presione enter para continuar...')