from logica.exercisesFour import guardar_mostrar_numGanadores

def designFourList():
    #Preguntar a usuario los numeros ganadores de la loteria
    num_ganadores=input("Cuales son los numeros ganadores de la loteria?: ")

    #Ordenar numeros de lista de menor a ma

    #Llamar a la funcion para guardar y mostrar los numeros ganadores de menor a mayor 
    resultado=guardar_mostrar_numGanadores(num_ganadores)

    lista_ordenada=sorted(num_ganadores)

    #Mostrar los numeros ganadores de menor a mayor 
    print(num_ganadores)