from logica.exercisesFour import loteria,formato_fecha

def desingFourList():
    numero = int (input("Cual es el numero ganador de la loteria?:' "))
    print(loteria(numero))

def desingFourDict():
    fecha = input("Cual es la fecha? ejemplo: 'dd/mm/aa, day/month/year, 01/01/2024' ")
    print(formato_fecha(fecha))
    return 0