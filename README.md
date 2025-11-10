# README del proyecto

# Gestión de Datos de Países

Este programa en Python es una herramienta de consola para la **gestión y análisis de datos de países** a partir de un archivo CSV. Permite a los usuarios buscar, filtrar, ordenar, obtener estadísticas y modificar los datos de población y superficie de los países.


## Requisitos

* **Python 3.x**
* **Archivo de datos CSV**: El programa requiere un archivo llamado `dataset_paises_undata.csv` en la misma carpeta que el script de Python.
* **Formato del CSV**: El archivo CSV debe tener un encabezado y sus filas deben seguir el siguiente orden de columnas:
    1.  Nombre del país
    2.  Población (número entero)
    3.  Superficie en Km² (número entero)
    4.  Continente

    **Ejemplo de encabezado:**
    ```csv
    nombre,poblacion,superficie,continente
    ```

## Instalación

1.  Asegúrate de tener **Python 3** instalado.
2.  Guarda el código fuente (`app.py`) y el archivo de datos (`dataset_paises_undata.csv`) en la misma carpeta.

---

## Uso

Para ejecutar el programa, abre tu terminal o línea de comandos, navega hasta la carpeta donde guardaste el archivo y ejecuta:

python app.py