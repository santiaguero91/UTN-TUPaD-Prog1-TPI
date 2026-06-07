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
    return paises


# Pregunta nombre de pais a actualizar y lo busca dentro de la lista paises
# luego muestra menu por que propiedad se desea combiar
# y pide ingresar valor a cambiar ---> Santiago


def actualizar_paises():
    paises = cargar_paises()

    while True:
        nombre = input(
            "Nombre del pais que desea actualizar: ").strip().lower()

        for pais in paises:
            if pais["nombre"].lower() == nombre:
                print(f"Pais encontrado: {pais['nombre']}")
                print(f"Superficie: {pais['superficie']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Continente: {pais['continente']}")
                break
        else:
            print("Pais no encontrado.")
            continue

        print("1. Nombre")
        print("2. Superficie")
        print("3. Poblacion")
        print("4. Continente")

        try:
            opcion = int(input("Que caracteristica desea actualizar?: "))
        except ValueError:
            print("Opcion no válida.")
            continue

        nuevo_valor = input("Ingrese nuevo valor: ").strip().lower()

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
    while True:
        nombre_pais = input("Ingresar nombre del pais: ").strip().lower()
        # Manejo de errores para inggresos nulos
        if len(nombre_pais) == 0:
            print("Debe ingresar un nombre valido")
            continue
        for pais in paises:
            if pais["nombre"].lower() == nombre_pais:
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
    while True:
        print("1. Filtrar por Continente:")
        print("2. Filtrar por Rango de poblacion:")
        print("3. Filtrar por Rango de superficie:")
        try:
            opcion = int(input("Ingrese opcion para filtrar:"))
            if opcion not in range(1, 4):
                print("Error: ingrese un numero del 1 al 3.")
                continue
        except ValueError:
            print("Error: ingrese un numero del 1 al 3.")
            continue

        if opcion == 1:
            nombre = input("Ingrese nombre de continente").strip().lower()
            for pais in paises:
                if pais["continente"].lower() == nombre:
                    print(pais)

        if opcion != 1:
            rango_minimo = int(input("Ingrese rango minimo"))
            rango_maximo = int(input("Ingrese rango maximo"))

        if opcion == 2:
            for pais in paises:
                if pais["poblacion"] > rango_minimo and pais["poblacion"] < rango_maximo:
                    print(pais)

        if opcion == 3:
            for pais in paises:
                if pais["superficie"] > rango_minimo and pais["superficie"] < rango_maximo:
                    print(pais)

# Muestra en pantalla opciones de ordenado
# en base a la opcion ingresada mostrara en orden deseado los paises interesado. ---> Santiago


def ordenar_paises():
    paises = cargar_paises()
    while True:
        print("Ordenar países por:")
        print("1. Nombre")
        print("2. Población")
        print("3. Superficie")
        # Manejo de errores para verificar numero en rango
        try:
            opcion = int(input("Ingrese opcion para ordenar: "))
            if opcion not in range(1, 4):
                print("Error: ingrese un numero del 1 al 3.")
                continue
        except ValueError:
            print("Error: ingrese un numero del 1 al 3.")
            continue
        if opcion == 1:
            paises.sort(key=lambda p: p["nombre"])
        elif opcion == 2:
            paises.sort(key=lambda p: p["poblacion"])
        elif opcion == 3:
            ascendente = input(
                "Orden ascendente o descentente ( A ó D ):").strip().lower()
            if ascendente == "a":
                paises.sort(key=lambda p: p["superficie"])
            elif ascendente == "d":
                paises.sort(key=lambda p: p["superficie"], reverse=True)

        else:
            print("Opcion no válida.")
            return

        for pais in paises:
            print(
                f"{pais['nombre']} - Superficie: {pais['superficie']} - Poblacion: {pais['poblacion']} - Continente: {pais['continente']}")


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
