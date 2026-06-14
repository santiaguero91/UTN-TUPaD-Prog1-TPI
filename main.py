from funciones import agregar_paises, actualizar_paises, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas


def menu():
    while True:
        print("-------------------------------\n"  # Cambio el usar tantos prints en uno solo con saltos de Linea para no llamar tantas funciones. --> Liam
              "Menu Principal:\n"
              "1. Agregar país:\n"
              "2. Actualizar país:\n"
              "3. Buscar país:\n"
              "4. Filtrar países:\n"
              "5. Ordenar países por:\n"
              "6. Mostrar estadísticas:\n"
              "7. Salir:\n"
              "-------------------------------")
        try:
            opcion = int(input("Seleccione una opcion: "))
            print("")
            if opcion not in range(1, 8):
                raise ValueError  # Cambio el print por un raise que genere el ValueError y asi no repetir el print.
        except ValueError:
            print("Error: ingrese un numero del 1 al 7.")
            continue

        if opcion == 1:
            while True:
                try:
                    numero_paises = int(  # Decidi pedir la cantidad de paises fuera de la funcion para aprovechar la recursividad.
                        input("Ingrese el numero de paises: "))
                    if numero_paises <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Error: Ingrese un número entero mayor que 0.")
            agregar_paises(numero_paises) # Le paso la cantidad de paises a la funcion para utilizar la recursividad. ---> Liam
        elif opcion == 2:
            actualizar_paises()
        elif opcion == 3:
            buscar_pais()
        elif opcion == 4:
            filtrar_paises()
        elif opcion == 5:
            ordenar_paises()
        elif opcion == 6:
            mostrar_estadisticas()
        else:
            print("Saliendo...")
            break


menu()
