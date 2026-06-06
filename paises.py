def menu():
    while True:
        print("-------------------------------")
        print("Menu Principal:")
        print("1. Agregar país:")
        print("2. Actualizar país:")
        print("3. Buscar país:")
        print("4. Filtrar países:")
        print("5. Ordenar países por:")
        print("6. Mostrar estadísticas:")
        print("7. Salir:")
        print("-------------------------------")
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion not in range(1, 8):
                print("Error: ingrese un numero del 1 al 7.")
                continue
        except ValueError:
            print("Error: ingrese un numero del 1 al 7.")
            continue

        if opcion == 1:
            agregar_paises()
        if opcion == 2:
            actualizar_paises()
        if opcion == 3:
            buscar_pais()
        if opcion == 4:
            filtrar_paises()
        if opcion == 5:
            ordenar_paises()
        if opcion == 6:
            mostrar_estadisticas()
        if opcion == 7:
            print("Saliendo...")
            break


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


def agregar_paises():
    while True:
        try:
            numero_paises = int(
                input("Ingrese el numero de paises: "))
            if numero_paises <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un número entero mayor que 0.")

    for i in range(numero_paises):
        while True:
            nombre_pais = input(f"Ingresar nombre de pais {i+1}: ")
            if len(nombre_pais) == 0:
                print("Debe agregar un pais")
                continue
            superficie_pais = input(
                f"Ingresar superficie de pais {i+1}: ")
            if len(superficie_pais) == 0:
                print("Debe agregar una superficie")
                continue
            poblacion_pais = input(
                f"Ingresar poblacion de pais {i+1}: ")
            if len(poblacion_pais) == 0:
                print("Debe agregar una poblacion")
                continue
            continente_pais = input(
                f"Ingresar continente de pais {i+1}: ")
            if len(continente_pais) == 0:
                print("Debe agregar un continente")
                continue
            break

        with open("paises.txt", "a") as archivo:
            archivo.write(
                f"{nombre_pais},{superficie_pais},{poblacion_pais},{continente_pais}\n")


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

        nuevo_valor = input("Ingrese nuevo valor: ").strip()

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


def buscar_pais():
    paises = cargar_paises()

    nombre_pais = input("Ingresar nombre del pais: ")
    for pais in paises:
        if pais["nombre"] == nombre_pais:
            print(f"Pais encontrado: {pais['nombre']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Poblacion: {pais['poblacion']}")
            print(f"Continente: {pais['continente']}")
            break
    else:
        print("Pais no encontrado.")


def filtrar_paises():
    paises = cargar_paises()

    print("1. Filtrar por Continente:")
    print("2. Filtrar por Rango de poblacion:")
    print("3. Filtrar por Rango de superficie:")
    opcion = int(input("Ingrese opcion para filtrar:"))

    if opcion == 1:
        nombre = input("Ingrese nombre de continente")
        for pais in paises:
            if pais["continente"] == nombre:
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


def ordenar_paises():
    paises = cargar_paises()
    print("Ordenar países por:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    opcion = int(input("Ingrese opcion para ordenar: "))

    if opcion == 1:
        paises.sort(key=lambda p: p["nombre"])
    elif opcion == 2:
        paises.sort(key=lambda p: p["poblacion"])
    elif opcion == 3:
        ascendente = input("Orden ascendente o descentente ( A ó D ):")
        if ascendente == "a":
            paises.sort(key=lambda p: p["superficie"])
        elif ascendente == "d":
            paises.sort(key=lambda p: p["superficie"], reverse=True)

    else:
        print("Opcion no válida.")
        return

    for pais in paises:
        print(f"{pais['nombre']} - Superficie: {pais['superficie']} - Poblacion: {pais['poblacion']} - Continente: {pais['continente']}")


def mostrar_estadisticas():
    paises = cargar_paises()
    print("Mostrar estadisticas:")
    print("1. Pais con mayor y menor poblacion:")
    print("2. Promedio de poblacion:")
    print("3. Cantidad de países por continente:")

    opcion = int(input("Ingrese una opcion"))
    if opcion == 1:
        paises.sort(key=lambda p: p["poblacion"])
    print(f"Pais con mayor poblacion {paises[0]}")
    print(f"Pais con menoer poblacion {paises[-1]}")

    if opcion == 3:
        conteo = {}
        for pais in paises:
            continente = pais["continente"]

            if continente in conteo:
                conteo[continente] += 1
            else:
                conteo[continente] = 1


for continente, cantidad in conteo.items():
    print(f"{continente}: {cantidad}")

menu()
