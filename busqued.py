from cargar_paises import cargar_paises


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
            print("\nDebe ingresar un nombre valido\n")
            continue
        elif nombre_pais == "0": # Agrego un elif para poder volver al menu ya que entra en un bucle y no se puede salir. ---> Liam
            print("Volviendo al menu...")
            break
        for pais in paises:
            if pais["nombre"].capitalize() == nombre_pais: #Cambio lower() por capitalize() ---> Liam.
                print(f"\nPais encontrado: {pais['nombre']}")
                print(f"Superficie: {pais['superficie']}")
                print(f"Poblacion: {pais['poblacion']}")
                print(f"Continente: {pais['continente']}\n")
                break
        else:
            # En caso de no encontrar nombre exacto realiza busqueda parcial---> Santi.
            encontrados = [p for p in paises if nombre_pais.lower() in p["nombre"].lower()]
            if encontrados:
                print(f"\nNo se encontro una coincidencia exacta. Resultados parciales para '{nombre_pais}':\n")
                for p in encontrados:
                    print(f"Pais encontrado: {p['nombre']}")
                    print(f"Superficie: {p['superficie']}")
                    print(f"Poblacion: {p['poblacion']}")
                    print(f"Continente: {p['continente']}\n")
            else:
                print("Pais no encontrado.\n")
