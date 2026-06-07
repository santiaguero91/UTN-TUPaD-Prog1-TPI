from funciones import agregar_paises, actualizar_paises, buscar_pais, filtrar_paises, ordenar_paises, mostrar_estadisticas

def menu():
    while True:
        print("-------------------------------\n" #Cambio el usar tantos prints en uno solo con saltos de Linea para no llamar tantas funciones. --> Liam
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
            if opcion not in range(1, 8):
                raise ValueError #Cambio el print por un raise que genere el ValueError y asi no repetir el print. --> Liam
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

menu()