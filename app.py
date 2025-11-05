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
buscar_pais()

def filtrar_x_continente():
  continente = input("Por favor ingrese el nombre del continente: ")
  continentes = ["America", "Asia", "Africa", "Europa", "Oceania", "Antartida"]
  termino_busqueda = normalizar_palabra(continente.strip().lower())
  if termino_busqueda not in [c.lower() for c in continentes]:
    print("El continente ingresado no existe.")
    print("Los continentes disponibles son: America, Asia, Africa, Europa, Oceania, Antartida")
    return

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

filtrar_x_continente()  

def filtrar_x_rango_poblacion():
  pass

def filtrar_x_rango_superficie():
  pass

