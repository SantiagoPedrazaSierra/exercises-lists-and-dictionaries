import json 
def leer_archivo(ruta_archivo):
    try:
        with open(f"databases/{ruta_archivo}", "r",encoding="utf-8") as file:
            datos=file.read()
            convertirList = json.loads(datos)
            return convertirList
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return []
    except json.JSONDecodeError:
        print(f"El archivo {ruta_archivo} no contiene un formato JSON válido.")
        return []

def escribir_archivo(datos,ruta_archivo ):
    try:
        with open(f"databases/{ruta_archivo}", "w+") as file:
            convertirJson = json.dumps(datos, indent=4).encode("utf-8")
            file.write(convertirJson)
    except IOError:
        print(f"Hubo un error al escribir el archivo {ruta_archivo}")


#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
def guardar_mostrar_numGanadores (num_ganadores):
    datos=leer_archivo("exercisesForDict.json")
    datos.append(num_ganadores)
    escribir_archivo(datos,"exercisesFourDict.json")
    return datos


#Escribir un programa que pregunte una fecha en formato `dd/mm/aaaa` y muestre por pantalla 
# la misma fecha en formato `dd de <mes> de aaaa` donde `<mes>` es el nombre del mes.
