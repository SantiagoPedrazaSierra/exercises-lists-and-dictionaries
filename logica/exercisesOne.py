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

#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.
def guardar_curso(curso):
    datos=leer_archivo("ExercisesOneList.json")
    datos.append(curso)
    escribir_archivo(datos,"ExercisesOneList.json")
    return datos

#Escribir un programa que guarde en una variable el diccionario 
#`{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}`, pregunte al usuario 
#por una divisa y muestre su símbolo o un mensaje de aviso si 
# la divisa no está en el diccionario.

def buscar_moneda (moneda):
    datos=leer_archivo("exercisesOneDict.json")
    if (datos.get(moneda)):
        return datos.get (moneda)
    else:
        return "moneda no encontrada."