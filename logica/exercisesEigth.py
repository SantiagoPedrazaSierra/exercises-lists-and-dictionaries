import json
import os

#Escribir un programa que pida al usuario una palabra y muestre
#por pantalla si es un palíndromo.

def determinar_palindromo():
    #Solitar a usuario una pantalla 
    palabra=input("Ingrese una palabra: ").strip().lower()

    #Determinar si la palabra del usuario es un palindramo
    if palabra == palabra[::-1]:
        print(f"La palabra '{palabra}' es un palindromo.")

    else:
        print(f"La palabra '{palabra}' no es un palindromo")
    
    #Ruta del archivo JSON
    ruta_archivo ="databases/exercisesEigthList.json"

    #Guardar el resultado en un archivo JSON

    #Leer el contenido existente 
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as json_file:
            try:
                lista_palabras = json.load(json_file)
                if not isinstance(lista_palabras, list):  # Verificar que sea una lista
                    lista_palabras = []
            except json.JSONDecodeError:  # Manejar archivos JSON mal formateados
                lista_palabras = []
    else:
        lista_palabras = []

    # Agregar la palabra a la lista
    lista_palabras.append(palabra)

    # Guardar la lista actualizada en el archivo JSON
    with open(ruta_archivo, "w") as json_file:
        json.dump(lista_palabras, json_file, indent=4)

    return lista_palabras

#Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
#y cada par `<palabra>:<traducción>` separados por comas. El programa debe crear 
#un diccionario con las palabras y sus traducciones. Después pedirá una frase en 
#español y utilizará el diccionario para traducirla palabra a palabra.
#Si una palabra no está en el diccionario debe dejarla sin traducir.

def crear_diccionario_traduccion():
    #Solicitar a usuario las palabras en español e ingles
    entrada=input("Ingrese palabras separadas, Ej(<palabra>:<traducción>) separadas por comas: ")

    if not entrada:
        print("No se proporcionaron palabras para el diccionario, intentalo de nuevo.")
        return
    #cargar el diccionario existente si el archivo ya tiene contenido
    try:
        with open("databases/exercisesEigthDict.json", "r") as json_file:
            diccionario = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        diccionario = {}
    
    #Crear el diccionario de traduccion
    
    pares=[par.strip() for par in entrada.split(",")]
    for par in pares:
        if ":" in par:
            palabra,traduccion =map(str.strip, par.split(":",1))
            diccionario[palabra]=traduccion
        else:
            print(f"Formato invalido ignorado: '{par}'")
    
    if not diccionario:
        print("No se pudo crear el diccionario.Intenta usar el formato correcto.")
        return

    #Mostrar el diccionario creado
    print("Diccionario creado:")
    for palabra,traduccion in diccionario.items():
        print(f"{palabra} -> {traduccion}")

    #Solicitar al usuario una frase en español para traduccir 
    frase = input("\nIntroduce una frase en español para traducir: ").strip()
    
    if not frase:
        print("No se proporcionó una frase para traducir.")
        return
    
    # Traducir la frase
    palabras = frase.split()
    traduccion = [
        diccionario.get(palabra, palabra) for palabra in palabras
    ]  # Dejar sin traducir si no está en el diccionario

    #Guardar el resultado en un archivo JSON
    with open ("databases/exercisesEigthDict.json", "w") as json_file:
        json.dump(diccionario,json_file,indent=4)

    # Mostrar la frase traducida
    frase_traducida = " ".join(traduccion)
    print(f"\nFrase traducida: {frase_traducida}")

