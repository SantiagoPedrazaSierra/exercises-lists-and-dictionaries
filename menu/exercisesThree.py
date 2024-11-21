from logica.exercisesThree import mostrar_nota_asignaturas, calcular_precio_fruta

def designThreeList():
    # Definir las asignaturas
    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    # Crear un diccionario para almacenar las notas
    notas = {}

    # Preguntar por la nota de cada asignatura
    for asignatura in asignaturas:
        nota = input(f"- Nota de {asignatura}: ")
        notas[asignatura] = int(nota)
    
    # Llamar a la función para almacenar las notas
    mostrar_nota_asignaturas(notas)

    print()  # Espacio
    
    # Mostrar las notas
    for asignatura, nota in notas.items():
        print(f"La nota de {asignatura} es {nota}")

def designThreeDict():
    # Precios predeterminados
    precios_frutas = {
        "platano": 1.35,
        "manzana": 0.80,
        "pera": 0.85,
        "naranja": 0.70
    }

    # Mostrar los precios disponibles
    print("Precios de las frutas disponibles:")
    for fruta, precio in precios_frutas.items():
        print(f"{fruta}: {precio} por kilo")

    # Pedir al usuario la fruta y los kilos
    fruta = input("Ingrese el nombre de la fruta que desea comprar: ").lower()
    kilos = float(input(f"¿Cuántos kilos de {fruta} desea comprar?: "))

    # Verificar si la fruta está en el diccionario de precios
    if fruta in precios_frutas:
        precio_total = calcular_precio_fruta(precios_frutas, fruta, kilos)
        print(f"El precio total por {kilos} kilos de {fruta} es: {precio_total:.2f}$")
    else:
        print(f"Lo siento, no tenemos {fruta} en nuestra tienda.")
