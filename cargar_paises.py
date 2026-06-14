# funcion auxiliar para leer los paises del archivo de texto#
# y guardarlos a una lista de diccionarios ---> Santiago


def cargar_paises():
    paises = []
    try: #Agrego un try/except para evitar que falle si no existe el archivo previamente. ---> Liam
        with open("paises.csv", "r") as archivo:
            for linea in archivo:
                if not linea.strip():
                    continue
                datos = linea.strip().split(",")
                paises.append({
                    "nombre": datos[0],
                    "superficie": int(datos[1]),
                    "poblacion": int(datos[2]),
                    "continente": datos[3]
                })
    except FileNotFoundError:
        return False
    return paises
