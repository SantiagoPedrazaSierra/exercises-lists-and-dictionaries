import json

#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

def leer_archivo(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        converList = json.loads(data)
        return converList

def escribir_archivo(data, path):
    with open(f"databases/{path}", "wb+") as file:
        convertirJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close

def loteria(numero):
    data = leer_archivo("exercisesFourList.json")
    data.append(numero)
    escribir_archivo(data, "exercisesFourList.json")
    return data


#Escribir un programa que pregunte una fecha en formato `dd/mm/aaaa` y muestre por pantalla 
# la misma fecha en formato `dd de <mes> de aaaa` donde `<mes>` es el nombre del mes.

def formato_fecha(fecha):
    if not fecha or len(fecha.split("/")) != 3:
        raise ValueError("La fecha debe tener el formato DD/MM/AAAA")

    lista = fecha.split("/")
    mes_num = int(lista[1])
    
    if mes_num < 1 or mes_num > 12:
        raise ValueError("El número del mes debe estar entre 1 y 12")
    
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # Asegurar que dato sea una lista
    dato = leer_archivo("exercisesFourDict.json") or []
    if not isinstance(dato, list):
        raise ValueError("El archivo JSON no contiene una lista válida")

    formato = {
        "dia": lista[0],
        "mes": meses[mes_num - 1],
        "anio": lista[2],
        "mensaje": f"{lista[0]} de {meses[mes_num - 1]} de {lista[2]}"
    }

    dato.append(formato)
    escribir_archivo(dato, "exercisesFourDict.json")
    return formato.get("mensaje")
