from logica.exercisesOne import guardar_curso
from logica.exercisesOne import buscar_moneda
def designOneList():
    curso=input("¿Cuál es el nombre del curso?")
    resultado=guardar_curso(curso)
    print(resultado)

def designOneDict():
    moneda=input("Cual es el nombre de la moneda? ")
    print (buscar_moneda(moneda))