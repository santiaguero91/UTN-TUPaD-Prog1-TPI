from cargar_paises import cargar_paises


# Muestra en pantalla opciones de ordenado
# en base a la opcion ingresada mostrara en orden deseado los paises interesado. ---> Santiago

def paises_ordenados(paises): # Creo esta funcion para no repetir el for por cada opcion y printear correctamente ---> Liam
    for pais in paises:
                print(
                    f"\n{pais['nombre']} - Superficie: {pais['superficie']} - Poblacion: {pais['poblacion']} - Continente: {pais['continente']}")

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
            opcion = int(input("Ingrese opcion para ordenar (0 para salir): "))

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
            elif opcion == 0:
                print("Volviendo al menu...")
                break
            else:
                print("Error: No ingreso una opcion valida.")
            return

        except ValueError:
            print("Error: no ingreso un numero valido.\n") # Corrijo el try/except ---> Liam
            continue
