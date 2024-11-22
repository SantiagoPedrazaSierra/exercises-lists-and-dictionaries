#Escribir un programa que almacene en una lista
#los números del 1 al 10 y los muestre por pantalla
#en orden inverso separados por comas.
import json

def lista_numeros_inversos():
    # Crear la lista de números del 1 al 10
    numero = list(range(1, 11))
    
    # Invertir el orden de los números
    numeros_inversos = numero[::-1]
    
    # Guardar la lista invertida en un archivo JSON
    with open("databases/exercisesFiveList.json", "w") as json_file:
        json.dump(numeros_inversos, json_file, indent=4)
    
    # Convertir la lista a una cadena de texto separada por comas
    numeros_inversos_str = ", ".join(map(str, numeros_inversos))
    
    # Mostrar los números por pantalla
    print(f"Números en orden inverso: {numeros_inversos_str}")
    
    return numeros_inversos

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
#`{'Matemáticas': 6, 'Física': 4, 'Química': 5}` y después muestre por pantalla los créditos
#de cada asignatura en el formato `<asignatura> tiene <créditos> créditos`, donde `<asignatura>`
#es cada una de las asignaturas del curso, y `<créditos>` son sus créditos. Al final debe mostrar 
#también el número total de créditos del curso.

import json

def mostrar_creditos_curso():
    # Diccionario con las asignaturas y sus créditos
    curso_creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    
    # Guardar el diccionario en un archivo JSON
    with open("databases/exercisesFiveDict.json", "w") as json_file:
        json.dump(curso_creditos, json_file, indent=4)
    
    # Mostrar los créditos por asignatura
    total_creditos = 0
    print("Créditos de las asignaturas:")
    for subject, credits in curso_creditos.items():
        print(f"{subject} tiene {credits} créditos")
        total_creditos += credits

    # Mostrar el número total de créditos
    print(f"\nEl número total de créditos del curso es: {total_creditos}")

    return curso_creditos, total_creditos