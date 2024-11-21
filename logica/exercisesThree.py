import json 

def leer_archivo(nombre_archivo):
    try:
        with open(f"databases/{nombre_archivo}", "r",encoding="utf-8") as file:
            datos=file.read()
            convertirList = json.loads(datos)
            return convertirList
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return {}
    except json.JSONDecodeError:
        print(f"El archivo {nombre_archivo} no contiene un formato JSON válido.")
        return {}

def escribir_archivo(datos,nombre_archivo):
    try:
        with open(f"databases/{nombre_archivo}", "w",encoding="utf-8") as file:
            convertirJson = json.dumps(datos,ensure_ascii=False, indent=4)
            file.write(convertirJson)
    except IOError as e:
        print(f"Hubo un error al escribir el archivo {nombre_archivo}: {e}")

#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la nota que ha sacado en cada
#asignatura, y después las muestre por pantalla con el mensaje
#`En <asignatura> has sacado <nota>` donde `<asignatura>` es cada una
#des las asignaturas de la lista y `<nota>` cada una de las correspondientes 
#notas introducidas por el usuario.
def mostrar_nota_asignaturas(notas):
    datos=leer_archivo("ExercisesThreeList.json")   

    #Asegurarse de que "asignaturas" exista y sea una lista
    if "asignaturas" not in datos:
        datos["asignaturas"] = []
    
    #Agregar las notas de las asignaturas al diccionario 
    asignaturas_notas= notas
    
    #Agregar el diccionario de notas a la lista de asignaturas 
    datos["asignaturas"].append(asignaturas_notas)

    #Guardar los datos actualizados en el archivo 
    escribir_archivo(datos, "ExercisesThreeList.json")

#Escribir un programa que guarde en un diccionario los precios
#de las frutas de la tabla, pregunte al usuario por una fruta,
#un número de kilos y muestre por pantalla el precio de ese 
#número de kilos de fruta. Si la fruta no está en el diccionario
#debe mostrar un mensaje informando de ello.
def calcular_precio_fruta():
    datos=leer_archivo("ExercisesThreeDict.json")   

    #Asegurarse de que "asignaturas" exista y sea una lista
    if "frutas""kilos" not in datos:
        datos["asignaturas"] = []
    
    #Agregar las notas de las asignaturas al diccionario 
    asignaturas_notas= notas
    
    #Agregar el diccionario de notas a la lista de asignaturas 
    datos["frutas","kilos"].append(precios_frutas)

    #Guardar los datos actualizados en el archivo 
    escribir_archivo(datos, "ExercisesThreeDict.json")