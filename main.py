from menu.exercisesOne import designOneList,designOneDict

while True:
    opcion = int(input(f"""
=========================
Elija una opción:
=========================
1. Ejercicios de Lista
2. Ejercicios de Diccionarios
=========================
"""))

    match opcion:
        case 1: designOneList()
        case 2: designOneDict()
        case _: print ("Opcion no valida ")