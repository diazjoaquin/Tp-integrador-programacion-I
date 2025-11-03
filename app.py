import csv

paises: list[dict] = []

def buscar_pais():
  pais = input("Ingresar el nombre del país que desea buscar: ")
  termino_busqueda = pais.strip().lower()
  paises_encontrados = []
  
  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    # Saltamos la primera línea que contiene los títulos para evitar que aparezca en el filtrado parcial.
    next(lector, None)
    for linea in lector:
      for col in linea:
        if termino_busqueda in col.strip().lower():
          [nombre, poblacion, superficie, continente] = linea
          paises_encontrados.append([nombre, poblacion, superficie, continente])
          break
  
  if paises_encontrados:
    print(f"Se encontraron {len(paises_encontrados)} coincidencias:")
    for i, pais in enumerate(paises_encontrados, 1):
      [nombre, poblacion, superficie, continente] = pais
      print(f"{i}. Nombre: {nombre}, Población: {poblacion}, Superficie: {superficie}, Continente: {continente}")
  else:
    print("No se encontraron países que coincidan con la búsqueda")

buscar_pais()