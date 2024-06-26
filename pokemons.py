import csv
import json

#EJERCICIO TIENDA
# Diccionario para almacenar los productos
Pokemons = []

# Lista de categorías disponibles
Tipos = ["Fuego", "Agua", "Electrico", "Planta", "Bicho", "Normal"]

def registrar_pokemons():
    """Función para registrar un Pokemon."""
    nombre = input("Ingrese el nombre del Pokemon: ").strip()
    print("Tipos Disponibles: ", Tipos)
    Tipos = input("Ingrese Tipo del Pokemon: ").strip()
    while Tipos not in Tipos:
        print("Categoría no válida. Intente nuevamente.")
        Tipos = input("Ingrese la categoría del producto: ").strip()
    try:
        Nivel = float(input("Ingrese el Nivel del Pokemon: "))
    except ValueError:
        print("El precio debe ser un número. Intente nuevamente.")
        return
    try:
        Vida = int(input("Ingrese la cantidad de Vida: "))
    except ValueError:
        print("La cantidad debe ser un número entero. Intente nuevamente.")
        return

    Pokemon = {
        "nombre": nombre,
        "tipo": Tipos,
        "nvel": Nivel,
        "Vida": Vida
    }
    Pokemons.append(Pokemons)
    print("Pokemon registrado exitosamente.\n")

def listar_pokemons():
    """Función para listar todos los productos registrados."""
    if not Pokemons:
        print("No hay pokemons registrados.")
        return
    for Pokemon in Pokemons:
        print(f"Nombre: {Pokemon['nombre']}, tipo: {Tipos['tipo']}, " 
              f"nivel: {Pokemon['nvel']}, Cantidad: {Pokemon['Vida']}")
    print("\n")

def imprimir_informe():
    """Función para imprimir informes de inventario en archivos de texto."""
    print("Opciones de impresión: ")
    print("1. Imprimir todos los productos")
    print("2. Imprimir por categoría específica")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        with open("informe_todos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, "
                              f"Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
        print("Informe de todos los productos generado como 'informe_todos.txt'.\n")
    elif opcion == "2":
        print("Categorías disponibles: ", categorias_disponibles)
        categoria = input("Ingrese la categoría a filtrar: ").strip()
        if categoria not in categorias_disponibles:
            print("Categoría no válida. Intente nuevamente.\n")
            return
        with open(f"informe_{categoria}.txt", "w") as archivo:
            for producto in productos:
                if producto["categoria"] == categoria:
                    archivo.write(f"Nombre: {producto['nombre']}, Categoría: {producto['categoria']}, "
                                  f"Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
        print(f"Informe de productos de la categoría {categoria} generado como 'informe_{categoria}.txt'.\n")
    else:
        print("Opción no válida. Intente nuevamente.\n")

def exportar_a_csv():
    """Función para exportar productos a un archivo CSV."""
    filename = input("Ingrese el nombre del archivo CSV (ejemplo: productos.csv): ").strip()
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Escribir encabezados
            writer.writerow(["Nombre", "Categoría", "Precio", "Cantidad"])
            # Escribir productos
            for producto in productos:
                writer.writerow([producto["nombre"], producto["categoria"], producto["precio"], producto["cantidad"]])
        print(f"Productos exportados exitosamente a {filename}\n")
    except IOError:
        print("Ocurrió un error al escribir el archivo CSV.\n")

def convertir_csv_a_json():
    """Función para convertir un archivo CSV a JSON."""
    csv_filename = input("Ingrese el nombre del archivo CSV a convertir (ejemplo: productos.csv): ").strip()
    json_filename = input("Ingrese el nombre del archivo JSON de salida (ejemplo: productos.json): ").strip()
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            productos_csv = list(csv_reader)
            with open(json_filename, mode='w') as json_file:
                json.dump(productos_csv, json_file, indent=4)
        print(f"Archivo CSV {csv_filename} convertido exitosamente a {json_filename}\n")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {csv_filename}.\n")
    except IOError:
        print("Ocurrió un error al leer o escribir el archivo.\n")

def menu_principal():
    """Función principal que muestra el menú y gestiona las opciones."""
    while True:
        print("Menú Principal:")
        print("1. Registrar producto")
        print("2. Listar todos los productos")
        print("3. Imprimir informe de inventario")
        print("4. Exportar productos a CSV")
        print("5. Convertir CSV a JSON")
        print("6. Salir del Programa")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            imprimir_informe()
        elif opcion == "4":
            exportar_a_csv()
        elif opcion == "5":
            convertir_csv_a_json()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu_principal()