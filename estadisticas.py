from cargar_paises import cargar_paises


def mostrar_estadisticas():
    paises = cargar_paises()

    if not paises:
        print("No hay paises cargados todavia!")
        return

    while True:
        if not paises:
            print("No hay paises cargados todavia!\n")
            return
        # Muestra en pantalla opciones de
        print("Mostrar estadisticas:\n"
        "1. Pais con mayor y menor poblacion:\n"
        "2. Promedio de poblacion:\n"
        "3. Cantidad de países por continente:\n"
        "4. Promedio de superficie:\n")
        # Manejo de errores para verificar numero en rango
        try:
            opcion = int(input("Ingrese una opcion (0 para salir):"))

            if opcion == 1:
                paises.sort(key=lambda p: p["poblacion"])
            # Ordena los paises de menor a mayor en base a su poblacion
                print(f"\nEl pais con menor poblacion es {paises[0]['nombre']} con {paises[0]['poblacion']} habitantes\n")
                print(f"El pais con mayor poblacion es {paises[-1]['nombre']} con {paises[-1]['poblacion']} habitantes\n")
            # busca todos los distintos valor para "continente dentro de la lista de diccionarios"

            elif opcion == 2: # Creo la opcion 2 del promedio de poblacion que faltaba ---> Liam
                suma_poblacion = 0
                for pais in paises:
                    suma_poblacion += pais["poblacion"]
                promedio = suma_poblacion / len(paises)
                print(f"\nPromedio de habitantes: {promedio:.2f}\n")

            elif opcion == 3:
                conteo = {}
                for pais in paises:
                    continente = pais["continente"]

                    if continente in conteo:
                        conteo[continente] += 1
                    else:
                        conteo[continente] = 1

                for continente, cantidad in conteo.items():
                    print(f"\n{continente}: {cantidad}\n")

            elif opcion == 4: # Creo la opcion del promedio de la superficie que faltaba ---> Liam
                suma_superficie = 0
                for pais in paises:
                    suma_superficie += pais["superficie"]
                promedio = suma_superficie / len(paises)
                print(f"\nPromedio de superficie: {promedio:.2f} km²\n")

            elif opcion == 0:
                print("\nVolviendo al menu...")
                break
            else:
                print("\nOpcion no valida!")
        except ValueError:
            print("\nError: No ingreso una opcion valida!\n")
            continue
