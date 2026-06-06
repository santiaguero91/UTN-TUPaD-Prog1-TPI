def menu():
    paises = []
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
            agregar_paises(paises)

        if opcion == 2:
            actualizar_paises(paises)
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


def agregar_paises(paises):
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


def actualizar_paises(paises):
    print("hola")


def buscar_pais():
    paises = []
    with open("paises.txt", "r") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            datos = linea.strip().split(",")
            paises.append({
                "nombre": datos[0],
                "superficie": float(datos[1]),
                "poblacion": int(datos[2]),
                "continente": datos[3]
            })

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
    print("hola")


def ordenar_paises():
    print("hola")


def mostrar_estadisticas():
    print("hola")


menu()
