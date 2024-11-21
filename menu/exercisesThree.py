from logica.exercisesThree import mostrar_nota_asignaturas 

def designThreeList():
    #Definir las asignaturas
    asignaturas=["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    #Crear un diccionario para almacenar las notas 
    notas={}

    #Preguntar por la nota de cada asignatura
    for asignatura in asignaturas:
        nota= input(f"-Nota de {asignatura}: ")
        notas[asignatura]=int(nota)
    
    #Llamar la funcion para almacenar las notas
    mostrar_nota_asignaturas(notas)

    print()#Espacio
    
    #Mostrar las notas 
    for asignatura, nota in notas.items():
        print(f"La nota de {asignatura} es {nota}")

def desingThreeDict():
    #Definir las frutas con sus precios por kilo 
    precios_frutas={
        "Platano": 1.35,
        "Manzana": 0.80,
        "Pera": 0.85,
        "Naranja": 0.70
        
    }
    #Pedir al usuario la fruta y la cantidad de kilos 
    fruta=input("Ingrese el nombre de la fruta que desea comprar: ")
    kilos=float(input(f"¿Cuantos kiloa de fruta desea comprar?: "))

    #Verificar si la fruta esta en el diccionario 
    if fruta in precios_frutas:
        #Calcular el precio total
        precio_total=precios_frutas[fruta]*kilos
        print(f"El precio de {kilos} kilos de {fruta} es {precio_total} dolares.")
    else:
        #Si la fruta no esta en el diccionario
        print(f"Lo siento, no tenemos {fruta} en  nuestra tienda.")
        