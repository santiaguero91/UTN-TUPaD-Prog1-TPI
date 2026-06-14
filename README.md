# Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) de Programación 1 - Tecnicatura Universitaria en Programación (UTN).

## Descripción

Aplicación de consola para gestionar información de países (nombre, superficie, población y continente), utilizando listas, diccionarios y funciones. Los datos se almacenan en el archivo `paises.csv`.

El programa permite:

- **Agregar países**: carga uno o varios países pidiendo nombre, superficie, población y continente (no se permiten campos vacíos).
- **Actualizar país**: busca un país por nombre y permite modificar su superficie, población, nombre o continente.
- **Buscar país**: busca por nombre, admitiendo coincidencia exacta o parcial.
- **Filtrar países**: por continente, por rango de población o por rango de superficie.
- **Ordenar países**: por nombre, por población o por superficie (ascendente o descendente).
- **Mostrar estadísticas**: país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.

## Requisitos

- Python 3.x

## Cómo ejecutarlo

1. Clonar o descargar el repositorio.
2. Asegurarse de que el archivo `paises.csv` se encuentre en la misma carpeta que `main.py`.
3. Ejecutar:

```bash
python main.py
```

4. Seleccionar una opción del menú principal (1 al 7) e ingresar los datos solicitados.

## Estructura del proyecto

- `main.py`: menú principal y flujo del programa.
- `funciones.py`: funciones para agregar, actualizar, buscar, filtrar, ordenar y mostrar estadísticas de países.
- `paises.csv`: archivo de datos donde se guardan los países (formato: `nombre,superficie,poblacion,continente`).
