from aux import cargar_paises


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
            opcion = int(input("Ingrese opcion para filtrar (0 para salir): "))

            if opcion == 1:
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

            elif opcion == 0:
                print("Volviendo al menu...")
                break
            else:
                print("Error: No ingreso una opcion valida")

        except ValueError: # Corrijo el try/except ---> Liam
            print("Error: no ingreso un numero valido.")
            continue
