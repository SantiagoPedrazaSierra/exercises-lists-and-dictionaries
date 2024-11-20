import json 
def leer_archivo(path):
    try:
        with open(f"databases/{path}", "r",encoding="utf-8") as file:
            datos=file.read()
            convertirList = json.loads(datos)
            return convertirList
    except FileNotFoundError:
        print(f"El archivo {path} no se encontró.")
        return []
    except json.JSONDecodeError:
        print(f"El archivo {path} no contiene un formato JSON válido.")
        return []

def escribir_archivo(datos,path ):
    try:
        with open(f"databases/{path}", "w+") as file:
            convertirJson = json.dumps(datos, indent=4).encode("utf-8")
            file.write(convertirJson)
    except IOError:
        print(f"Hubo un error al escribir el archivo {path}")

#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla el mensaje 
#`Yo estudio <asignatura>`, donde `<asignatura>`
# es cada una de las asignaturas de la lista.
def guardar_curso(curso):
    datos=leer_archivo("ExercisesTwoList.json")
    datos.append(curso)
    escribir_archivo(datos, "ExercisesTwoList.json")
    print("Curso guardado correctamente.")
    
    #Mostrar a usuario en que curso estudia
    print("Yo estudio,",curso)
