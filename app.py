import csv
import unicodedata

paises: list[dict] = []

def normalizar_palabra(palabra):
  return ''.join(c for c in unicodedata.normalize('NFD', palabra)
    if unicodedata.category(c) != 'Mn')


def buscar_pais():
  pais = input("Ingresar el nombre del país que desea buscar: ")
  termino_busqueda = normalizar_palabra(pais.strip().lower())
  paises_encontrados = []
  
  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    # Saltamos la primera línea que contiene los títulos para evitar que aparezca en el filtrado parcial.
    next(lector, None)
    for linea in lector:
      if termino_busqueda in linea[0].strip().lower():
        [nombre, poblacion, superficie, continente] = linea
        paises_encontrados.append([nombre, poblacion, superficie, continente])
  
  if paises_encontrados:
    print(f"Se encontraron {len(paises_encontrados)} coincidencias:")
    for i, pais in enumerate(paises_encontrados, 1):
      [nombre, poblacion, superficie, continente] = pais
      print(f"{i}. Nombre: {nombre}, Población: {poblacion}, Superficie(Km2): {superficie}, Continente: {continente}")
  else:
    print("No se encontraron países que coincidan con la búsqueda")

def filtrar_x_continente():
  continente = input("Por favor ingrese el nombre del continente: ")
  continentes = ["America", "Asia", "Africa", "Europa", "Oceania", "Antartida"]
  termino_busqueda = normalizar_palabra(continente.strip().lower())
  while True:
    if termino_busqueda in [c.lower() for c in continentes]:
      break
    else:
      print("El continente ingresado no existe. Por favor ingrese un continente válido.")
      continente = input("Por favor ingrese el nombre del continente: ")
      termino_busqueda = normalizar_palabra(continente.strip().lower())

  filtrados_x_continente = []

  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)
    for linea in lector:
      if termino_busqueda in linea[3].strip().lower():
        [nombre, poblacion, superficie, continente] = linea
        filtrados_x_continente.append([nombre, poblacion, superficie, continente])
        
  if filtrados_x_continente:
    print(f"Paises pertenecientes al contienente de {continente}")
    for i, pais in enumerate(filtrados_x_continente, 1):
      [nombre, poblacion, superficie, continente] = pais
      print(f"{i}. [Continente: {continente}]: Nombre: {nombre}, Población: {poblacion}, Superficie(Km2): {superficie}")
  else:
    print("No se encontraron paises que coincidan con la búsqueda")

def filtrar_x_rango(param: str):
  rango = input(f"Por favor ingrese el rango de {param} [min-max]: ")
  [min, max] = rango.split("-")
  while True:
    if min.isdigit() and max.isdigit():
      min = int(min)
      max = int(max)
      if min > max:
        print("El valor mínimo no puede ser mayor que el valor máximo. Por favor ingrese un rango válido.")
        rango = input(f"Por favor ingrese el rango de {param} [min-max]: ")
        [min, max] = rango.split("-")
      else:
        break
    else:
      print("El rango ingresado no es válido. Por favor ingrese un rango numérico.")
      rango = input(f"Por favor ingrese el rango de {param} [min-max]: ")
      [min, max] = rango.split("-")
  
  filtrados_x_rango = []

  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)
    for linea in lector:
      if param == "poblacion":
        if min <= int(linea[1]) <= max:
          filtrados_x_rango.append(linea)
      elif param == "superficie":
        if min <= int(linea[2]) <= max:
          filtrados_x_rango.append(linea)

  if filtrados_x_rango:
    print(f"Paises con {param} en el rango [{min}-{max}]")
    for i, pais in enumerate(filtrados_x_rango, 1):
      [nombre, poblacion, superficie, continente] = pais
      print(f"{i}. Nombre: {nombre}, Población: {poblacion}, Superficie(Km2): {superficie}, Continente: {continente}")
  else:
    print("No se encontraron paises que coincidan con la búsqueda")
