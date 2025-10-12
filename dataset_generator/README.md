# README — `genera_dataset_undata.py`

**Generado por:** ChatGPT (script generado por el asistente para procesar datos de UNdata)

---

## 1. Resumen

Este README describe el script `genera_dataset_undata.py` y explica cómo se ha utilizado para formatear y normalizar los datos del fichero **UNdata — "Population, surface area and density"** (Statistical Yearbook, actualizado el 27-Nov-2024). El objetivo del script es producir un archivo CSV llamado `dataset_paises_undata.csv` con los campos:

```
nombre,poblacion,superficie,continente
```

* `nombre`: Nombre corto del país/territorio (string)
* `poblacion`: Población (int, número entero de personas)
* `superficie`: Superficie total en km² (int)
* `continente`: Continente asignado (string)

El script fue generado por ChatGPT y diseñado para ser ejecutado localmente por el usuario, tomando como entrada el CSV oficial de UNdata descargado previamente.

---

## 2. Archivos incluidos / generados

* `SYB67_1_202411_Population, Surface Area and Density.csv` — **(entrada)** CSV original descargado desde UNdata (Statistical Yearbook). **No** está incluido en este repositorio; debés descargarlo desde la web de UNdata y colocarlo en la misma carpeta que el script.

* `genera_dataset_undata.py` — **(script)** Python que procesa el CSV de UNdata y genera `dataset_paises_undata.csv`.

* `dataset_paises_undata.csv` — **(salida)** CSV resultante con columnas `nombre,poblacion,superficie,continente`.

---

## 3. Fuentes y atribuciones

* **Fuente de los datos:** UNdata — *Population, surface area and density* (UN Statistical Yearbook). Versión consultada: actualizada el **27-Nov-2024**. El archivo original debe descargarse desde el portal de datos de la ONU (data.un.org).

* **Generado por:** ChatGPT (asistente), script y documentación producidos automáticamente por el asistente a petición del usuario.

---

## 4. Descripción del procesamiento

1. **Lectura del CSV oficial:** el script abre el CSV descargado de UNdata. El fichero del Statistical Yearbook suele tener una cabecera/estructura con varias filas de metadatos; el script normaliza las columnas relevantes.

2. **Filtrado de series relevantes:** se seleccionan las filas que contienen la serie de "Population mid-year estimates (millions)" y la serie de "Surface area". Estas series contienen, respectivamente, la población (en millones) y la superficie (habitualmente expresada en *000 km²*).

3. **Selección del año más reciente:** para cada código `Region/Country/Area` (en el CSV aparece como el código numérico M49 en muchas versiones), se selecciona la observación del año más reciente disponible (por ejemplo 2024 si existe).

4. **Normalización de unidades:**

   * Población: la serie viene en millones — por eso se multiplica por `1_000_000` y se guarda como entero.
   * Superficie: la tabla frecuentemente muestra el área en *000 km²* (por ejemplo `2,780` = 2,780,000 km²). Se multiplica por `1000` cuando corresponde y se guarda como entero en km².

5. **Mapeo de códigos a nombres:** las filas del CSV original usan frecuentemente el código numérico UN M49. El script usa la librería `country_converter` para convertir esos códigos M49 (`UNnumeric3`) al nombre corto del país (por ejemplo `Argentina`).

6. **Asignación de continente:** se utiliza la funcionalidad de `country_converter` para asignar un continente a cada nombre de país.

7. **Salida:** se guardan las columnas `nombre`, `poblacion`, `superficie`, `continente` en `dataset_paises_undata.csv`.

---

## 5. Dependencias

Asegurate de tener Python 3.8+ y los siguientes paquetes instalados:

```bash
pip install pandas country_converter pycountry
```

* `pandas`: manipulación y procesamiento de datos.
* `country_converter` (abreviado `coco`): mapeo de nombres/códigos de países y asignación de continente. Dependencia interna: `pycountry`.

---

## 6. Instrucciones de uso

1. Descargá el CSV oficial desde UNdata y colocalo en la misma carpeta que el script. El nombre de archivo esperado en el script es exactamente:

```
SYB67_1_202411_Population, Surface Area and Density.csv
```

> Nota: si el archivo tiene otro nombre, renombralo o modifica la constante `INPUT_FILE` al inicio del script.

2. Instalá dependencias (si no están instaladas):

```bash
pip install pandas country_converter pycountry
```

3. Ejecutá el script:

```bash
python genera_dataset_undata.py
```

4. Resultado: se generará `dataset_paises_undata.csv` en la misma carpeta.

---

## 7. Ejemplo de uso y salida esperada

Ejecutando el script se generará un CSV con el encabezado y filas como estas (ejemplo):

```
nombre,poblacion,superficie,continente
China,1416099758,9596960,Asia
India,1424837200,3287263,Asia
Estados Unidos,341963000,9833517,América del Norte
Argentina,47225000,2780400,América del Sur
```

* `poblacion` es un número entero (personas).
* `superficie` es un número entero (km²).

---

## 8. Consideraciones y advertencias

* **Unidades y formatos:** el script usa heurísticas basadas en el formato estándar del fichero del Statistical Yearbook (población en millones; superficie en *000 km²*). Si UNdata cambia su formato, podría ser necesario ajustar la lógica de conversión.

* **Mapeos no encontrados:** `country_converter` no siempre encontrará una coincidencia (por ejemplo, nombres muy específicos, territorios con nombres alternativos o entradas agregadas del año). El script filtra entradas `not found`. Si necesitás conservar entradas que no se mapearon automáticamente, podés:

  * revisar manualmente las filas que quedaron sin mapeo y añadir un diccionario de traducción,
  * o modificar el script para extraer y mantener el texto directo del CSV en vez de usar los códigos M49.

* **Cobertura:** el número de filas resultante dependerá de la versión del fichero UNdata descargado. El Statistical Yearbook puede incluir regiones agregadas y subregiones además de países; el script intenta mapear y devolver únicamente países/territorios con nombre corto reconocido.

* **Actualizaciones:** los datos provienen del UN Statistical Yearbook actualizado el 27-Nov-2024. Para obtener cifras más recientes, deberás descargar una versión más reciente del CSV y volver a ejecutar el script.

---

## 9. Verificación y control de calidad sugerido

Después de generar `dataset_paises_undata.csv`:

1. Comprobar el número de filas:

   * Contar cuántos registros se generaron (ej. `wc -l dataset_paises_undata.csv`).
2. Verificar valores extremos:

   * `poblacion` debe ser > 0.
   * `superficie` debe ser > 0.
3. Revisar entradas con `continente == 'not found'` o `continente == 'Unknown'` y corregir manualmente si corresponde.
4. Comparar una muestra (10–20 países) contra las cifras en UNdata para garantizar consistencia.

---

## 10. Ejemplos de problemas frecuentes y soluciones

* **Error de lectura del CSV**: si pandas falla porque la cabecera es multilínea, asegurate de usar `low_memory=False` y que el archivo no esté parcialmente descargado.
* **`country_converter` devuelve `not found`**: podés intentar normalizar nombres (eliminar acentos, paréntesis) o usar `src='UNnumeric3'` para convertir desde códigos M49 directamente.
* **Problema con comillas/encoding**: abrir el archivo con `encoding='utf-8'` suele resolver la mayoría de problemas; si no, probá `encoding='latin1'`.

---

## 11. Licencia y atribución

El script y este README fueron generados por ChatGPT a solicitud del usuario. Los datos de entrada (`SYB67_1_202411_Population, Surface Area and Density.csv`) provienen de la ONU (UNdata) y están sujetos a los términos de uso de la fuente original. Revisá las condiciones de UNdata si tenés dudas sobre redistribución.

---

## 12. Contacto y soporte

Si querés que:

* adapte el script para incluir regiones/subregiones,
* incorpore enlaces a las filas originales (por ejemplo, año exacto por país),
* guarde metadata adicional (fuente y fecha) en el CSV o en un archivo README adjunto,

decime qué preferís y lo ajusto.

¡Listo! Si querés, puedo también generar el archivo README en formato `.md` y subirlo directamente para que lo descargues — decime si lo querés así y lo creo.
