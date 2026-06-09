# Pregunta cuantos paises a agregar
# En base a la cantidad ingresada crear un loop para
# preguntar nombre, superficie, poblacion y continente ---> Santiago
def agregar_paises(cant):
    if cant <= 0: # Caso base para la recursividad. ---> Liam
        return
    while True:
        try: #Meto todo el codigo en un try/except para evitar errores a la hora de ingresar numeros enteros. ---> Liam
            nombre_pais = input(
                f"Ingresar nombre del pais: ").strip().capitalize() #Cambio lower por Capitalize por prolijidad ---> Liam
            # Requisito minimo 1
            if nombre_pais.strip() == "": #Cambio los "len(variable)" de tipo str por un strip() para evitar que puedan ingresar espacios en blanco.
                print("Debe agregar un pais al menos")
                continue
            superficie_pais = int(input( #Convierto a enteros los valores numericos como superficie y poblacion ya que dejaba ingresar texto. ---> Liam
                f"Ingresar superficie del pais: "))
            # Requisito ingresar algun caracter ---> Santiago
            if superficie_pais <= 0:
                print("Debe agregar una superficie")
                continue
            poblacion_pais = int(input(
                f"Ingresar poblacion del pais: "))
            # Requisito ingresar algun caracter
            if poblacion_pais <= 0:
                print("Debe agregar una poblacion")
                continue
            # Requisito ingresar algun caracter
            continente_pais = input(
                f"Ingresar continente del pais: ").strip().capitalize()
            if len(continente_pais) == 0:
                print("Debe agregar un continente")
                continue
            print("-------------------------------")
            break
        except ValueError:
            print("Error, no ingreso un dato valido. Por favor intente cargar el pais nuevamente\n"
            "-------------------------------"
                )
            continue

    with open("paises.txt", "a") as archivo:
        archivo.write(
            f"{nombre_pais},{superficie_pais},{poblacion_pais},{continente_pais}\n")
    agregar_paises(cant -1) # Recursividad ---> Liam


# funcion auxiliar para leer los paises del archivo de texto#
# y guardarlos a una lista de diccionarios ---> Santiago


def cargar_paises():
    paises = []
    try: #Agrego un try/except para evitar que falle si no existe el archivo previamente. ---> Liam
        with open("paises.txt", "r") as archivo:
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


# Pregunta nombre de pais a actualizar y lo busca dentro de la lista paises
# luego muestra menu por que propiedad se desea combiar
# y pide ingresar valor a cambiar ---> Santiago


def actualizar_paises():
    paises = cargar_paises()

    if not paises: #Verifico que haya caragado paises previamente y evitar que entre en un bucle. ---> Liam
        print("No hay paises cargados todavia.")
        return

    while True:
        nombre = input(
            "Nombre del pais que desea actualizar: ").strip().capitalize() # ---> Liam
        print("")
        for pais in paises:
            if pais["nombre"] == nombre:
                print(f"Pais encontrado: {pais['nombre']}")
                print(f"Superficie: {pais['superficie']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Continente: {pais['continente']}\n")
                break
        else:
            print("Pais no encontrado.")
            break # Cambio continue por break para salir de la funcion y volver al menu y no entrar en bucle si no quiere seguir ----> Liam

        print("1. Nombre\n"
        "2. Superficie\n"
        "3. Poblacion\n"
        "4. Continente\n")

        try:
            opcion = int(input("Que caracteristica desea actualizar?: "))

            nuevo_valor = input("Ingrese nuevo valor: ").strip().capitalize()

            if opcion == 1:
                pais["nombre"] = nuevo_valor
            elif opcion == 2:
                pais["superficie"] = int(nuevo_valor)
            elif opcion == 3:
                pais["poblacion"] = int(nuevo_valor)
            elif opcion == 4:
                pais["continente"] = nuevo_valor
            else:
                print("Opcion no válida.")
                continue
        except ValueError: # Utilizo el try anterior y lo aplico al resto del codigo para evitar que falle al intear. ---> Liam
            print("Error, ingreso un valor incorrecto.")
            continue


        with open("paises.txt", "w") as archivo:
            for p in paises:
                archivo.write(
                    f"{p['nombre']},{p['superficie']},{p['poblacion']},{p['continente']}\n")

        print("Pais actualizado correctamente.")
        break

# Pregunta nombre de pais y lo busca dentro de la lista paises
# muestra en consola la informacion de dicho pais ---> Santiago
def buscar_pais():
    paises = cargar_paises()
    if not paises:
        print("No hay paises cargados todavia.")
        return
    
    while True:
        nombre_pais = input("Ingresar nombre del pais (0 para volver al menu): ").strip().capitalize()
        # Manejo de errores para ingresos nulos
        if nombre_pais.strip() == "": #Cambio len() por strip() para evitar que ingrese espacios en blanco. ---> Liam.
            print("Debe ingresar un nombre valido")
            continue
        elif nombre_pais == "0": # Agrego un elif para poder volver al menu ya que entra en un bucle y no se puede salir.
            print("Volviendo al menu...")
            break
        for pais in paises:
            if pais["nombre"].capitalize() == nombre_pais: #Cambio lower() por capitalize() ---> Liam.
                print(f"Pais encontrado: {pais['nombre']}")
                print(f"Superficie: {pais['superficie']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Continente: {pais['continente']}")
                break
        else:
            print("Pais no encontrado.")


# Muestra en pantalla opciones de filtrado
# en base a la opcion ingresada pide inputs correspondientes
# busca en la lista los items correspondiente a esas propiedades ingresadas ---> Santiago


def filtrar_paises():
    paises = cargar_paises()
    if not paises:
        print("No hay paises cargados todavia.") # Verificador ---> Liam
        return
    while True:
        print("1. Filtrar por Continente:\n"
        "2. Filtrar por Rango de poblacion:\n"
        "3. Filtrar por Rango de superficie:\n") # correcion prints ---> Liam
        try:
            opcion = int(input("Ingrese opcion para filtrar: "))
            if opcion not in range(1, 4):
                raise ValueError # Genero la excepcion para aprovechar el mismo try en todo el codigo ---> Liam

            elif opcion == 1:
                nombre = input("Ingrese nombre de continente: ").strip().capitalize() # lower > capitalize ---> Liam
                print("Lista de paises en el continente ingresado:\n") # Agregado por prolijidad ---> Liam
                for pais in paises:
                    if pais["continente"].capitalize() == nombre:
                        print(pais['nombre']) # Correcion, ahora muestra el pais en vez del diccionario completo. ---> Liam
                break

            elif opcion == 2:
                rango_minimo = int(input("Ingrese rango minimo: "))
                rango_maximo = int(input("Ingrese rango maximo: "))
                print("Paises dentro del rango de poblacion ingresado:\n")
                for pais in paises:
                    if pais["poblacion"] >= rango_minimo and pais["poblacion"] <= rango_maximo: # Correji el <> agregando = para que aplique el numero ingresado inclusive. ---> Liam
                        print(pais['nombre'])
                break

            elif opcion == 3:
                rango_minimo = int(input("Ingrese rango minimo: "))
                rango_maximo = int(input("Ingrese rango maximo: "))
                print("Paises dentro del rango de superficie ingresado:\n")
                for pais in paises:
                    if pais["superficie"] >= rango_minimo and pais["superficie"] <= rango_maximo:
                        print(pais['nombre'])
                break
        except ValueError: # Corrijo el try/except ---> Liam
            print("Error: no ingreso un numero valido.")
            continue

# Muestra en pantalla opciones de ordenado
# en base a la opcion ingresada mostrara en orden deseado los paises interesado. ---> Santiago

def paises_ordenados(paises): # Creo esta funcion para no repetir el for por cada opcion y printear correctamente ---> Liam
    for pais in paises:
                print(
                    f"{pais['nombre']} - Superficie: {pais['superficie']} - Poblacion: {pais['poblacion']} - Continente: {pais['continente']}\n")

def ordenar_paises():
    paises = cargar_paises()
    if not paises:
        print("No hay paises cargados todavia!")
        return
    while True:
        print("Ordenar países por:\n"
        "1. Nombre\n"
        "2. Población\n"
        "3. Superficie\n")
        # Manejo de errores para verificar numero en rango
        try:
            opcion = int(input("Ingrese opcion para ordenar: "))
            if opcion not in range(1, 4):
                print("Error: ingrese un numero del 1 al 3.\n")
                continue
            if opcion == 1:
                paises.sort(key=lambda p: p["nombre"])
                paises_ordenados(paises) # Llamo a la funcion que cree en vez de repetir todo el rato el for ---> Liam
            elif opcion == 2:
                paises.sort(key=lambda p: p["poblacion"])
                paises_ordenados(paises)
            elif opcion == 3:
                ascendente = input(
                    "Orden ascendente o descentente ( A ó D ):").strip().lower()
                if ascendente == "a":
                    paises.sort(key=lambda p: p["superficie"])
                    paises_ordenados(paises)
                elif ascendente == "d":
                    paises.sort(key=lambda p: p["superficie"], reverse=True)
                    paises_ordenados(paises)
                else:
                    print("Opcion no valida!\n")
            return
        
        except ValueError:
            print("Error: no ingreso un numero valido.\n") # Corrijo el try/except ---> Liam
            continue


def mostrar_estadisticas():
    paises = cargar_paises()
    
    while True:
        # Muestra en pantalla opciones de
        print("Mostrar estadisticas:")
        print("1. Pais con mayor y menor poblacion:")
        print("2. Promedio de poblacion:")
        print("3. Cantidad de países por continente:")
        # Manejo de errores para verificar numero en rango
        try:
            opcion = int(input("Ingrese una opcion:"))
            if opcion not in range(1, 4):
                print("Error: ingrese un numero del 1 al 3.")
                continue
        except ValueError:
            print("Error: ingrese un numero del 1 al 3.")
            continue

        if opcion == 1:
            paises.sort(key=lambda p: p["poblacion"])
        # Ordena los paises de menor a mayor en base a su poblacion
            print(f"Pais con menor poblacion {paises[0]}")
            print(f"Pais con mayor poblacion {paises[-1]}")

        # busca todos los distintos valor para "continente dentro de la lista de diccionarios"
        elif opcion == 3:
            conteo = {}
            for pais in paises:
                continente = pais["continente"]

                if continente in conteo:
                    conteo[continente] += 1
                else:
                    conteo[continente] = 1

            for continente, cantidad in conteo.items():
                print(f"{continente}: {cantidad}")
