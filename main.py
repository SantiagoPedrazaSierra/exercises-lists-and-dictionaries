from menu.exercisesOne import designOneList,designOneDict
from menu.exercisesTwo import designTwoList
import os
#Menu Principal
def Main_menu():
    while True:
        try:
            opcion = int(input(f"""
    =================================
   |         Elige una opcion        |
   |=================================|
   | 1. Ejercicios Listas.           |
   | 2. Ejercicio Diccionario.       |
   | 3. Salir                        |
   |=================================|
    -ingrese un numero del (1-3):"""))
            match opcion :
                case 1:
                    os.system('cls')
                    MenuListExercises()
                case 2:
                    os.system('cls')
                    MenuDictExercises()
                case 3:
                    print("\n-Saliendo del programa...")
                    os._exit(0) #Volver al menu principal
                case _: print ("Opcion no valida.")
        except ValueError:
            print("Por favor, ingrese un numero valido.")



#Menu Listas
def MenuListExercises():
    while True:
        try:
            opcion = int(input(f"""
    =================================
   |     Ejercicios de Listas        |
   |=================================|
   | 1. Ejercicio 1.                 |
   | 2. Ejercicio 2.                 |
   | 3. Volver al menu principal     |
   |=================================|
    -ingrese un numero del (1-3):"""))
        
            match opcion :
                case 1:
                    os.system('cls')
                    designOneList()
                case 2:
                    os.system('cls')
                    designTwoList()
                case 3: 
                    os.system('cls')
                    return #Volver al menu principal
                case _: print ("Opcion no valida.")
        except ValueError:
            print("Por favor, ingrese un numero valido.")

#Menu Diccionarios 
def MenuDictExercises():
    while True:
        try:
            opcion = int(input(f"""
    =================================
   |   Ejercicios de Diccionarios    |
   |=================================|
   | 1. Ejercicio 1.                 |
   | 2. Ejercicio 2.                 |
   | 3. Volver al menu principal     |
   |=================================|
    -ingrese un numero del (1-3):"""))
    
        
            match opcion :
                case 1:
                    os.system('cls')
                    designOneDict()
                case 2:
                    os.system('cls')
                    print("Ejercicio 2 no implementado aún.")
                case 3: 
                    os.system('cls')
                    return #Volver al menu principal
                case _: print ("Opcion no valida.")
        except ValueError:
            print("Por favor, ingrese un numero valido.")

Main_menu()