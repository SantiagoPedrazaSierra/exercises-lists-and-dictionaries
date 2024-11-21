import json

def leer_archivo(nombre_archivo):
    try:
        with open(f"databases/{nombre_archivo}", "r", encoding="utf-8") as file:
            datos = file.read()
            return json.loads(datos)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró. Se inicializará vacío.")
        return {}
    except json.JSONDecodeError:
        print(f"El archivo {nombre_archivo} no contiene un formato JSON válido. Se inicializará vacío.")
        return {}

def escribir_archivo(datos, nombre_archivo):
    try:
        with open(f"databases/{nombre_archivo}", "w", encoding="utf-8") as file:
            convertirJson = json.dumps(datos, ensure_ascii=False, indent=4)
            file.write(convertirJson)
    except IOError as e:
        print(f"Hubo un error al escribir el archivo {nombre_archivo}: {e}")

def mostrar_nota_asignaturas(notas):
    datos = leer_archivo("ExercisesThreeList.json")

    # Asegurarse de que "asignaturas" exista y sea una lista
    if "asignaturas" not in datos:
        datos["asignaturas"] = []
    
    # Agregar las notas de las asignaturas al diccionario
    datos["asignaturas"].append(notas)

    # Guardar los datos actualizados en el archivo
    escribir_archivo(datos, "ExercisesThreeList.json")

def calcular_precio_fruta(precios_frutas, fruta, kilos):
    # Leer los datos actuales del archivo
    datos = leer_archivo("exercisesThreeDict.json")

    # Agregar o actualizar la información de la fruta y los kilos comprados
    datos[fruta] = datos.get(fruta, 0) + kilos

    # Guardar la información actualizada en el archivo JSON
    escribir_archivo(datos, "exercisesThreeDict.json")

    # Calcular el precio total
    return precios_frutas[fruta] * kilos
