from menu.exercisesOne import designOneList,designOneDict
from menu.exercisesTwo import designTwoList,designTwoDict
from menu.exercisesThree import designThreeList,designThreeDict
from menu.exercisesFour import desingFourList,desingFourDict
from menu.exercisesFive import desingFiveList,desingFiveDict
from menu.exercisesSix import desingSixList,desingSixDict
from menu.exercisesSeven import designSevenList, designSevenDict
from menu.exercisesEigth import designEigthList,designEigthDict
from menu.exercisesNine import designNineList,designNineDict
from menu.exercisesTen import designTenList,designTenDict
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
   | 3. Ejercicio 3.                 |
   | 4. Ejercicio 4.                 |
   | 5. Ejercicio 5.                 |
   | 6. Ejercicio 6.                 |
   | 7. Ejercicio 7.                 |
   | 8. Ejercicio 8.                 |
   | 9. Ejercicio 9.                 |
   | 10. Ejercicio 10.               |
   | 0. Volver al menu principal     |
   |=================================|
    -ingrese un numero del (1-4):"""))
        
            match opcion :
                case 1:
                    os.system('cls')
                    designOneList()
                case 2:
                    os.system('cls')
                    designTwoList()
                case 3:
                    os.system('cls')
                    designThreeList()
                case 4:
                    os.system('cls')
                    desingFourList()
                case 5:
                    os.system('cls')
                    desingFiveList()
                case 6:
                    os.system('cls')
                    desingSixList()
                case 7:
                    os.system('cls')
                    designSevenList()
                case 8:
                    os.system('cls')
                    designEigthList()
                case 9: 
                    os.system('cls')
                    designNineList()
                case 10:
                    os.system('cls')
                    designTenList()
                case 0: 
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
   |    Ejercicios de Diccionarios   |
   |=================================|
   | 1. Ejercicio 1.                 |
   | 2. Ejercicio 2.                 |
   | 3. Ejercicio 3.                 |
   | 4. Ejercicio 4.                 |
   | 5. Ejercicio 5.                 |
   | 6. Ejercicio 6.                 |
   | 7. Ejercicio 7.                 |
   | 8. Ejercicio 8.                 |
   | 9. Ejercicio 9.                 |
   | 10. Ejercicio 10.               |
   | 0. Volver al menu principal     |
   |=================================|
    -ingrese un numero del (1-4):"""))
        
            match opcion :
                case 1:
                    os.system('cls')
                    designOneDict()
                case 2:
                    os.system('cls')
                    designTwoDict()
                case 3:
                    os.system('cls')
                    designThreeDict()
                case 4:
                    os.system('cls')
                    desingFourDict()
                case 5:
                    os.system('cls')
                    desingFiveDict()
                case 6:
                    os.system('cls')
                    desingSixDict()
                case 7:
                    os.system('cls')
                    designSevenDict()
                case 8:
                    os.system('cls')
                    designEigthDict()
                case 9: 
                    os.system('cls')
                    designNineDict()
                case 10:
                    os.system('cls')
                    designTenDict()
                case 0: 
                    os.system('cls')
                    return #Volver al menu principal
                case _: print ("Opcion no valida.")
        except ValueError:
            print("Por favor, ingrese un numero valido.")