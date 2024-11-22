import json

#Escribir un programa que pida al usuario una palabra
#y muestre por pantalla el número de veces que contiene cada vocal.

def vocales_palabra():
    #Solicitar a usuario una palabra
    palabra=input("Ingrese una palabra: ")

    #Diccionario para contar las vocales
    conteo_vocales={vocal:0 for vocal in "aeiou"}

    #Recorrer cada letra de la palabra 
    for letra in palabra:
        if letra in conteo_vocales: #Verificar si la letra es una vocal
            conteo_vocales[letra] += 1
    
    #Guardar el resultado en un archivo JSON
    with open ("databases/exercisesNineList.json", "w") as json_file:
        json.dump(conteo_vocales,json_file,indent=4)

    #Mostrar el resultado
    print(f"\nEn la palabra {palabra} hay {conteo_vocales} vocales.")

    return conteo_vocales

#Escribir un programa que gestione las facturas
# pendientes de cobro de una empresa. Las facturas 
#se almacenarán en un diccionario donde la clave de 
#cada factura será el número de factura y el valor
#el coste de la factura. El programa debe preguntar
#al usuario si quiere añadir una nueva factura,
#pagar una existente o terminar. Si desea añadir
#una nueva factura se preguntará por el número de
#factura y su coste y se añadirá al diccionario. 
#Si se desea pagar una factura se preguntará por el número 
#de factura y se eliminará del diccionario. Después de cada operación 
#el programa debe mostrar por pantalla la cantidad cobrada hasta el momento
#y la cantidad pendiente de cobro.

import json

def gestionar_facturas():
    # Intentar cargar las facturas desde un archivo JSON
    try:
        with open("facturas.json", "r") as json_file:
            facturas = json.load(json_file)
            print("Facturas cargadas desde el archivo.")
    except (FileNotFoundError, json.JSONDecodeError):
        facturas = {}
        print("No se encontraron facturas guardadas, comenzando con un archivo vacío.")

    total_cobrado = 0

    while True:
        print("\n=====================")
        print("Menú de Gestión de Facturas")
        print("=====================")
        print("1. Añadir nueva factura")
        print("2. Pagar una factura")
        print("3. Terminar")
        opcion = input("Seleccione una opción (1/2/3): ").strip()

        if opcion == "1":
            # Añadir nueva factura
            numero_factura = input("Ingrese el número de la factura: ").strip()
            if numero_factura in facturas:
                print("Error: Ya existe una factura con este número.")
                continue
            try:
                coste = float(input("Ingrese el coste de la factura: ").strip())
                facturas[numero_factura] = coste
                print(f"Factura {numero_factura} añadida con un coste de {coste:.2f}")
            except ValueError:
                print("Error: El coste debe ser un número válido.")
                continue

        elif opcion == "2":
            # Pagar una factura
            numero_factura = input("Ingrese el número de la factura que desea pagar: ").strip()
            if numero_factura in facturas:
                total_cobrado += facturas[numero_factura]
                del facturas[numero_factura]
                print(f"Factura {numero_factura} pagada.")
            else:
                print("Error: No se encontró la factura con ese número.")

        elif opcion == "3":
            # Terminar y guardar las facturas en el archivo JSON
            try:
                with open("facturas.json", "w") as json_file:
                    json.dump(facturas, json_file, indent=4)
                print("Facturas guardadas en el archivo.")
            except IOError:
                print("Error al guardar las facturas.")
            
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor elija 1, 2 o 3.")
            continue

        # Mostrar el total cobrado y el total pendiente de cobro
        total_pendiente = sum(facturas.values())
        print(f"\nTotal cobrado hasta el momento: {total_cobrado:.2f}")
        print(f"Total pendiente de cobro: {total_pendiente:.2f}")



