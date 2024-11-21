from logica.exercisesOne import guardar_curso
from logica.exercisesOne import buscar_moneda

def designOneList():
    asignatura=input("Cual es el nombre de la asignatura? ")
    resultado=guardar_curso(asignatura)
    print(resultado)

def designOneDict():
    moneda=input("Cual es el nombre de la moneda?  ")
    print(buscar_moneda(moneda))