import json

#Escribir un programa que almacene las asignaturas de un curso
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura
#y elimine de la lista las asignaturas aprobadas. Al final el programa debe 
#mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def manejo_asignaturas():
    #Lista de asignatura del curso
    asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = {}

    print("Introduce las notas para las siguientes asignaturas:")

    # Solicitar notas al usuario y filtrar asignaturas aprobadas
    pendientes = []
    for asignatura in asignaturas:
        nota = float(input(f"{asignatura}: "))
        notas[asignatura] = nota
        if nota < 5.0:
            pendientes.append(asignatura)

    # Guardar las notas en un archivo JSON
    ruta_archivo = "databases/exercisesSixList.json"
    with open(ruta_archivo, "w") as archivo_json:
        json.dump(notas, archivo_json, indent=4)

    # Informar de las asignaturas pendientes
    print("\nResultados:")
    if pendientes:
        print("Estas son las asignaturas que debes repetir:")
        print("\n".join(f"- {asignatura}" for asignatura in pendientes))
    else:
        print("¡Enhorabuena! Has aprobado todas las asignaturas.")

    return notas, pendientes

#Escribir un programa que cree un diccionario vacío y lo vaya llenado 
#con información sobre una persona (por ejemplo nombre, edad, sexo,
#teléfono, correo electrónico, etc.) que se le pida al usuario.
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def recolectar_datos_persona():

    datos_persona = {}

    print("  Escribe 'salir' cuando desees finalizar.\n")

    continuar = True
    while continuar:
        # Solicitar nombre del campo
        campo = input("-Que dato desea registrar ejm.('nombre','edad','numero'....): ").strip()

        if campo.lower() == "salir":
            continuar = False
            continue

        # Solicitar valor del campo
        valor = input(f"Introduce el valor para '{campo}': ").strip()
        datos_persona[campo] = valor

        # Mostrar los datos actuales
        print("""
  =======================================
    Datos registrados hasta el momento.
  =======================================""")
        for clave, valor in datos_persona.items():
            print(f"- {clave}: {valor}")
        print("-" * 30)

    # Guardar los datos en un archivo JSON
    archivo_salida = "databases/exercisesSixDict.json"
    with open(archivo_salida, "w") as archivo_json:
        json.dump(datos_persona, archivo_json, indent=4)

    print("""
  =======================================
            Registro completo.
  =======================================""")
    for clave, valor in datos_persona.items():
        print(f"- {clave}: {valor}")

    return datos_persona