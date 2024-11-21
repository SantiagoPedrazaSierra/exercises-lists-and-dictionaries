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
#en una lista y la muestre por pantalla el mensaje
#`Yo estudio <asignatura>`, donde `<asignatura>` 
#es cada una de las asignaturas de la lista.

def mostrar_y_guardar_asignaturas(asignatura):
    datos=leer_archivo("ExercisesTwoList.json")
    if "asignaturas" not in datos:
        datos["asignaturas"]=[]

    datos["asignaturas"].append(asignatura)
    escribir_archivo(datos,"ExercisesTwoList.json")
    return datos 


    

#Escribir un programa que pregunte al usuario su nombre, edad, dirección
# y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla 
# el mensaje `<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono 
# es <teléfono>`.
def mostrar_y_guardar_datos(nombre, edad, direccion, telefono):
    # Leer el archivo de datos
    datos = leer_archivo("ExercisesTwoDict.json")
    
    # Asegurarse de que "datos_usuario" sea una lista
    if "datos_usuario" not in datos or not isinstance(datos["datos_usuario"], list):
        datos["datos_usuario"] = []
    
    # Crear un diccionario con los datos del usuario
    nuevousuario = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }
    
    # Agregar el nuevo usuario a la lista "datos_usuario"
    datos["datos_usuario"].append(nuevousuario)
    
    # Guardar los datos actualizados en el archivo
    escribir_archivo(datos, "ExercisesTwoDict.json")
    
    return datos