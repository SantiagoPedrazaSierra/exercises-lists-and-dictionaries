from logica.exercisesTwo import mostrar_y_guardar_asignaturas,mostrar_y_guardar_datos
def designTwoList():
    nueva_asignatura=(input("-Ingrese su asignatura: "))
    datos=mostrar_y_guardar_asignaturas(nueva_asignatura)
    #Mostrar mensaje
    if "asignaturas" in datos:
        for asignatura in datos["asignaturas"]:
            print (f"\n Yo estudio {asignatura}. ")
    else:
        print("No se encontaron asignaturas ")
    

def designTwoDict():
    nombre = input("Ingrese su nombre: ").strip()
    edad = input("Ingrese su edad: ").strip()
    direccion = input("Ingrese su direccion: ").strip()
    telefono = input("Ingrese su telefono: ").strip()
    
    # Llamar a la función con los parámetros correctos
    datos_usuario = mostrar_y_guardar_datos(nombre, edad, direccion, telefono)
    
    # Mostrar mensaje
    if "datos_usuario" in datos_usuario.keys():
        print(f"{nombre} tiene {edad} años, vive en {direccion} y su numero de telefono es {telefono}")