import json

#Escribir un programa que almacene el abecedario en una lista,
#elimine de la lista las letras que ocupen posiciones múltiplos de 3,
#y muestre por pantalla la lista resultante.

def ejercicio_abecedario():
    #Crear una lista que contenga en abecedario 
    abecedario= list("abcdefghijklmnopqrstuvwxyz")

    #Eliminar letras en posiciones multiplos de 3 
    #Usando enumerate() para obtener indice y valor ,comnezando desde 1
    ejercicio_abecedario = [letter for index, letter in enumerate(abecedario, start=1) if index % 3 != 0]

    #Guardar el resultado en un archivo JSON
    with open ("databases/exercisesSevenList.json", "w") as json_file:
        json.dump(ejercicio_abecedario,json_file,indent=4)
    
    #Mostrar el resultado
    print("Lista de abecedario (sin letras en posiciones multiplos de 3): ")
    print(", ".join(ejercicio_abecedario))

    return ejercicio_abecedario

#Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de 
# la compra y el coste total, con el siguiente formato

def carrito_shop():
    #Crear un diccionario vacio para la cesta de la compra 
    carrito={}

    while True:
        #Pedir al usuario el nombre del articulo
        articulo=input("Ingrese el nombre del articulo: ").strip()
        if articulo.lower() == "salir":
            break
        #Pedir al usuario que ingrese el precio del articulo
        try:
            precio_art=float(input(f"Ingresa el precio de {articulo}: ").strip())
        except ValueError:
            print("Por favor, introduzca un precio valido.")
            continue
        #Añadir el articulo y su precio al diccionario
        carrito[articulo] = precio_art

    #Guardar el carrito de compra en un archivo JSON
    with open ("databases/exercisesSevenDict.json", "w") as json_file:
        json.dump(carrito,json_file,indent=4)
    
    #Mostrar la lista de la compra
    costo_total= 0
    print("""
====================================
| Lista de la compra | Precio      |
====================================""")
    

    for articulo, precio_art in carrito.items():
        print(f"|     {articulo:<15} |    {precio_art:>7.2f}|")
        costo_total += precio_art  # Sumar al costo total

    # Mostrar el costo total
    print("""
====================================
| Total:                 {0:>7.2f} |
====================================""".format(costo_total))

    return carrito, costo_total
    