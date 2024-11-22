import json 

#Escribir un programa que almacene en una lista los siguientes precios
#50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

def mostrar_min_max():
    #Crear una lista que contenga precios
    precios=[50,75,46,22,80,65,8]
    #Formula para mostar por pantalla el menor y mayor de los precios
    menor=min(precios)
    mayor=max(precios)

    #Estructura de los datos para guardar en el archivo JSON
    datos={
        "precios": precios,
        "menor_precio": menor,
        "mayor_precio": mayor
    }

    #Guardar el resultado en un archivo JSON
    with open ("databases/exercisesTenList.json", "w") as json_file:
        json.dump(datos,json_file,indent=4)
        
    #Mostrar resultado
    print(f"-El menor precio de {precios} es: {menor}")
    print(f"-El mayor precio de {precios} es: {mayor}")

    return menor,mayor 

#Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
#Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
#y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
#donde preferente tendrá el valor `True` si se trata de un cliente preferente.
#El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente,
#(3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar.
#En función de la opción elegida el programa tendrá que hacer lo siguiente:

#1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#3. Preguntar por el NIF del cliente y mostrar sus datos.
#4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#6. Terminar el programa.

def gestionar_clientes():
    # Intentar cargar los clientes desde un archivo JSON
    try:
        with open("databases/exercisesTenDict.json", "r") as json_file:
            clientes = json.load(json_file)
            print("Clientes cargados desde el archivo.")
    except (FileNotFoundError, json.JSONDecodeError):
        clientes = {}
        print("No se encontraron clientes guardados, comenzando con una base de datos vacía.")

    while True:
        print("\n=============================")
        print("Menú de Gestión de Clientes")
        print("=============================")
        print("1. Añadir cliente")
        print("2. Eliminar cliente")
        print("3. Mostrar cliente")
        print("4. Listar todos los clientes")
        print("5. Listar clientes preferentes")
        print("6. Terminar")
        opcion = input("Seleccione una opción (1/2/3/4/5/6): ").strip()

        if opcion == "1":
            # Añadir nuevo cliente
            nif = input("Ingrese el NIF del cliente: ").strip()
            if nif in clientes:
                print(f"Error: Ya existe un cliente con el NIF {nif}.")
                continue
            nombre = input("Ingrese el nombre del cliente: ").strip()
            direccion = input("Ingrese la dirección del cliente: ").strip()
            telefono = input("Ingrese el teléfono del cliente: ").strip()
            correo = input("Ingrese el correo del cliente: ").strip()
            preferente = input("¿Es cliente preferente? (s/n): ").strip().lower() == 's'

            clientes[nif] = {
                'nombre': nombre,
                'direccion': direccion,
                'telefono': telefono,
                'correo': correo,
                'preferente': preferente
            }
            print(f"Cliente {nombre} añadido con NIF {nif}.")

        elif opcion == "2":
            # Eliminar un cliente
            nif = input("Ingrese el NIF del cliente que desea eliminar: ").strip()
            if nif in clientes:
                del clientes[nif]
                print(f"Cliente con NIF {nif} eliminado.")
            else:
                print(f"Error: No se encontró un cliente con el NIF {nif}.")

        elif opcion == "3":
            # Mostrar datos de un cliente
            nif = input("Ingrese el NIF del cliente que desea ver: ").strip()
            if nif in clientes:
                cliente = clientes[nif]
                print(f"Datos del cliente {nif}:")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Dirección: {cliente['direccion']}")
                print(f"Teléfono: {cliente['telefono']}")
                print(f"Correo: {cliente['correo']}")
                print(f"Preferente: {'Sí' if cliente['preferente'] else 'No'}")
            else:
                print(f"Error: No se encontró un cliente con el NIF {nif}.")

        elif opcion == "4":
            # Listar todos los clientes
            if clientes:
                print("Lista de todos los clientes:")
                for nif, cliente in clientes.items():
                    print(f"NIF: {nif}, Nombre: {cliente['nombre']}")
            else:
                print("No hay clientes registrados.")

        elif opcion == "5":
            # Listar clientes preferentes
            preferentes = {nif: cliente for nif, cliente in clientes.items() if cliente['preferente']}
            if preferentes:
                print("Lista de clientes preferentes:")
                for nif, cliente in preferentes.items():
                    print(f"NIF: {nif}, Nombre: {cliente['nombre']}")
            else:
                print("No hay clientes preferentes registrados.")

        elif opcion == "6":
            # Terminar el programa y guardar los clientes en el archivo JSON
            with open("databases/exercisesTenDict.json", "w") as json_file:
                json.dump(clientes, json_file, indent=4)
            print("Clientes guardados en el archivo.")
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor elija una opción entre 1 y 6.")
