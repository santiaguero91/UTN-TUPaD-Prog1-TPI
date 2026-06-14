from cargar_paises import cargar_paises


# Pregunta cuantos paises a agregar
# En base a la cantidad ingresada crear un loop para
# preguntar nombre, superficie, poblacion y continente ---> Santiago
def agregar_paises(cant):
    if cant <= 0:  # Caso base para la recursividad. ---> Liam
        return
    while True:
        try:  # Meto todo el codigo en un try/except para evitar errores a la hora de ingresar numeros enteros. ---> Liam
            nombre_pais = input(
                # Cambio lower por Capitalize por prolijidad ---> Liam
                f"Ingresar nombre del pais: ").strip().capitalize()
            # Requisito minimo 1
            # Cambio los "len(variable)" de tipo str por un strip() para evitar que puedan ingresar espacios en blanco.
            if nombre_pais.strip() == "":
                print("Debe agregar un pais al menos")
                continue
            superficie_pais = int(input(  # Convierto a enteros los valores numericos como superficie y poblacion ya que dejaba ingresar texto. ---> Liam
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

    with open("paises.csv", "a") as archivo:
        archivo.write(
            f"{nombre_pais},{superficie_pais},{poblacion_pais},{continente_pais}\n")
    print("\nPaises cargados correctamente!")
    agregar_paises(cant -1) # Recursividad ---> Liam


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
                print("\nOpcion no válida.")
                continue
        except ValueError: # Utilizo el try anterior y lo aplico al resto del codigo para evitar que falle al intear. ---> Liam
            print("Error, ingreso un valor incorrecto.\n")
            continue


        with open("paises.csv", "w") as archivo:
            for p in paises:
                archivo.write(
                    f"{p['nombre']},{p['superficie']},{p['poblacion']},{p['continente']}\n")

        print("\nPais actualizado correctamente.")
        break
