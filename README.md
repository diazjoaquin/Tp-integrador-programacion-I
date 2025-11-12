# Trabajo Integrador - Programación I

## Gestión de Datos de Países

Sistema de gestión y análisis de datos de países desarrollado en Python como trabajo práctico integrador. Este programa permite realizar operaciones CRUD (Crear, Leer, Actualizar) y análisis estadísticos sobre un conjunto de datos de países almacenados en formato CSV.

---

## Integrantes del Proyecto

- **Joaquin Diaz**
- **Nicolás Naconechney**

**Materia:** Programación I
**Institución:** UTN
**Año:** 2025

---

## Descripción del Proyecto

Este programa es una herramienta de línea de comandos (CLI) desarrollada en Python para la gestión y análisis de información sobre países del mundo. La aplicación permite:

- **Buscar** países por nombre (con coincidencia parcial)
- **Filtrar** países por continente o rangos de población/superficie
- **Ordenar** listados por diferentes criterios (nombre, población, superficie)
- **Analizar** estadísticas generales del conjunto de datos
- **Agregar** nuevos países al dataset
- **Actualizar** información de población y superficie

El programa utiliza un archivo CSV como base de datos y ofrece una interfaz interactiva mediante menú de opciones.

---

## Requisitos del Sistema

### Software Necesario

- **Python 3.10 o superior**
- Módulos estándar de Python:
  - `csv` - Manejo de archivos CSV
  - `unicodedata` - Normalización de caracteres
  - `operator` - Funciones de ordenamiento

### Archivo de Datos

- **Nombre requerido:** `dataset_paises_undata.csv`
- **Ubicación:** Debe estar en el mismo directorio que `app.py`
- **Formato:** CSV con encabezado

#### Estructura del CSV

El archivo debe contener las siguientes columnas en este orden:

| Columna     | Tipo de Dato | Descripción                          |
|------------|--------------|--------------------------------------|
| nombre     | string       | Nombre del país                      |
| poblacion  | integer      | Población total (habitantes)         |
| superficie | integer      | Superficie en kilómetros cuadrados   |
| continente | string       | Continente al que pertenece          |

**Ejemplo de contenido:**

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,214326223,8515767,America
China,1410000000,9596961,Asia
Alemania,83240525,357022,Europa
```

---

## Instalación y Configuración

### 1. Clonar o Descargar el Proyecto

```bash
git clone https://github.com/diazjoaquin/Tp-integrador-programacion-I
cd Tp-integrador-programacion-I
```

### 2. Verificar Instalación de Python

```bash
python --version
# Debe mostrar Python 3.10 o superior
```

### 3. Verificar Archivos Necesarios

Asegurarse de tener los siguientes archivos en el directorio:

```
Tp-integrador-programacion-I/
├── app.py
├── dataset_paises_undata.csv
└── README.md
```

---

## Uso del Programa

### Ejecutar la Aplicación

Abrir una terminal en el directorio del proyecto y ejecutar:

```bash
python app.py
```

### Menú Principal

Al ejecutar el programa, se mostrará el siguiente menú interactivo:

```
Por favor ingrese una opción para continuar:
1. Buscar un país por nombre.
2. Filtrar países por continente.
3. Filtrar países por rango de población.
4. Filtrar países por rango de superficie(Km2).
5. Ordenar países por nombre.
6. Ordenar países por población.
7. Ordenar países por superficie.
8. Estadísticas.
9. Agregar un país a la lista.
10. Actualizar la población y superficie de un país.
11. Salir del menú.
```

---

## Ejemplos de Uso

### 1. Buscar un País por Nombre

**Entrada:**
```
Opción: 1
Ingresar el nombre del país que desea buscar: argentina
```

**Salida esperada:**
```
Se encontraron 1 coincidencias:
1. Nombre: Argentina, Población: 45376763, Superficie(Km2): 2780400, Continente: America
```

**Características:**
- Búsqueda por coincidencia parcial (case-insensitive)
- Normalización de caracteres especiales (ignora tildes)

---

### 2. Filtrar Países por Continente

**Entrada:**
```
Opción: 2
Por favor ingrese el nombre del continente: Europa
```

**Salida esperada:**
```
Paises pertenecientes al contienente de Europa
1. [Continente: Europa]: Nombre: Alemania, Población: 83240525, Superficie(Km2): 357022
2. [Continente: Europa]: Nombre: Francia, Población: 67413000, Superficie(Km2): 643801
...
```

**Continentes válidos:**
- America
- Asia
- Africa
- Europa
- Oceania
- Antartida

---

### 3. Filtrar por Rango de Población

**Entrada:**
```
Opción: 3
Por favor ingrese el rango de poblacion [min-max]: 10000000-50000000
```

**Salida esperada:**
```
Paises con poblacion en el rango [10000000-50000000]
1. Nombre: Argentina, Población: 45376763, Superficie(Km2): 2780400, Continente: America
2. Nombre: España, Población: 47351567, Superficie(Km2): 505990, Continente: Europa
...
```

---

### 4. Ordenar Países

**Entrada:**
```
Opción: 6
¿Desea ordenar de forma ascendente o descendente? (asc/desc): desc
```

**Salida esperada:**
```
Ordenados por población de forma descendente:
1. Nombre: China, Población: 1410000000, Superficie(Km2): 9596961, Continente: Asia
2. Nombre: India, Población: 1380004385, Superficie(Km2): 3287263, Continente: Asia
...
```

---

### 5. Ver Estadísticas

**Entrada:**
```
Opción: 8
```

**Salida esperada:**
```
El pais con mayor población es China con 1410000000 habitantes.
El pais con menor población es Ciudad del Vaticano con 801 habitantes.
El promedio de población por país es de 38755475.50 habitantes.
El promedio de superficie por país es de 598732.25 Km2.
America tiene un total de 56 paises.
Asia tiene un total de 51 paises.
Africa tiene un total de 60 paises.
Europa tiene un total de 53 paises.
Oceania tiene un total de 27 paises.
Antartida tiene un total de 5 paises.
```

---

### 6. Agregar un Nuevo País

**Entrada:**
```
Opción: 9
Por favor ingrese el nombre del país que desea agregar a la lista: Nuevo País
Por favor ingrese la población del país: 1000000
Por favor ingrese la superficie del país: 50000
Por favor ingrese el continente del país: America
```

**Salida esperada:**
```
El país Nuevo País ha sido agregado a la lista.
```

**Validaciones implementadas:**
- El nombre no puede estar vacío
- No se permiten países duplicados
- La población debe ser un número entero positivo
- La superficie debe ser un número entero mayor a 0
- El continente debe ser uno de los 6 continentes válidos

---

### 7. Actualizar Datos de un País

**Entrada:**
```
Opción: 10
Ingresar el nombre del país que desea actualizar: Argentina
Por favor ingrese la nueva población del país: 46000000
Por favor ingrese la nueva superficie del país: 2780400
```

**Salida esperada:**
```
La población y superficie del país Argentina han sido actualizados.
```

---

## Estructura del Código

### Funciones Principales

| Función | Descripción |
|---------|-------------|
| `normalizar_palabra(palabra)` | Elimina acentos y normaliza texto para comparaciones |
| `buscar_pais()` | Busca países por coincidencia parcial de nombre |
| `filtrar_x_continente()` | Filtra países por continente |
| `filtrar_x_rango(param)` | Filtra países por rango de población o superficie |
| `ordenar(param, paises, descendente)` | Ordena países por diferentes criterios |
| `estadisticas(paises)` | Calcula y muestra estadísticas del dataset |
| `agregar_pais()` | Agrega un nuevo país al CSV |
| `actualizar_poblacion_y_superficie(paises)` | Actualiza datos de un país existente |

### Validaciones Implementadas

El programa incluye validaciones exhaustivas:

1. **Entradas vacías:** No se permiten campos en blanco
2. **Tipos de datos:** Validación de enteros para población y superficie
3. **Rangos válidos:** El mínimo no puede ser mayor que el máximo
4. **Continentes válidos:** Solo acepta los 6 continentes predefinidos
5. **Duplicados:** No permite agregar países que ya existen
6. **Existencia:** Verifica que el país exista antes de actualizar

---

## Características Técnicas

### Manejo de Caracteres Especiales

El programa utiliza `unicodedata` para normalizar caracteres, permitiendo búsquedas sin importar acentos:

```python
buscar_pais()  # Entrada: "Mexico" o "México" - Ambas funcionan
```

### Operaciones con CSV

- **Lectura:** Uso de `csv.reader()` para parsear el archivo
- **Escritura:** Uso de `csv.writer()` con modo append (`a`) o write (`w`)
- **Skip de encabezado:** `next(lector, None)` para ignorar la primera línea

### Ordenamiento Eficiente

Utiliza `operator.itemgetter()` para ordenamiento optimizado:

```python
paises.sort(key=itemgetter("poblacion"), reverse=True)
```

---

## Posibles Mejoras Futuras

- [ ] Implementar persistencia con base de datos SQLite
- [ ] Agregar función de eliminación de países
- [ ] Exportar reportes a formatos PDF o Excel
- [ ] Interfaz gráfica (GUI) con Tkinter o PyQt
- [ ] Validación de nombres de países contra API externa
- [ ] Gráficos estadísticos con matplotlib
- [ ] Sistema de backup automático del CSV
- [ ] Logs de operaciones realizadas

---

## Problemas Conocidos

- El programa no valida si el archivo CSV existe antes de ejecutar operaciones
- No hay sistema de confirmación antes de actualizar datos
- La búsqueda de países duplicados en `agregar_pais()` no es completamente confiable

---

## Licencia

Este proyecto es de uso académico y educativo para el curso de Programación I.

---
