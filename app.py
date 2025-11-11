import csv
import unicodedata
from operator import itemgetter

def normalizar_palabra(palabra):
  return ''.join(c for c in unicodedata.normalize('NFD', palabra)
    if unicodedata.category(c) != 'Mn')


def buscar_pais():
  pais = input("Ingresar el nombre del país que desea buscar: ")
  while True:
    if len(pais.strip()) == 0:
      print("El nombre del país no puede estar vacío. Por favor ingrese un nombre válido.")
      pais = input("Ingresar el nombre del país que desea buscar: ")
    else:
      break
  
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
  while True:
    if len(continente.strip()) == 0:
      print("El nombre del continente no puede estar vacío. Por favor ingrese un nombre válido.")
      continente = input("Por favor ingrese el nombre del continente: ")
    else:
      break
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
  while True:
    if "-" not in rango:
      print("El rango ingresado no es válido. Por favor ingrese un rango numérico.")
      rango = input(f"Por favor ingrese el rango de {param} [min-max]: ")
    else:
      break
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

def ordenar(param: str, paises: list[dict], descendente: bool):
  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)
    for linea in lector:
      [nombre, poblacion, superficie, continente] = linea
      paises.append({"nombre": nombre, "poblacion": int(poblacion), "superficie": int(superficie), "continente": continente})

  if param == "nombre":
    paises.sort(key=itemgetter("nombre"), reverse=descendente)
    print(f"Ordenados por nombre {'de forma descendente' if descendente else 'de forma ascendente'}:")
    for i, pais in enumerate(paises, 1):
      print(f"{i}. Nombre: {pais['nombre']}, Población: {pais['poblacion']}, Superficie(Km2): {pais['superficie']}, Continente: {pais['continente']}")
  elif param == "poblacion":
    paises.sort(key=itemgetter("poblacion"), reverse=descendente)
    print(f"Ordenados por población {'de forma descendente' if descendente else 'de forma ascendente'}:")
    for i, pais in enumerate(paises, 1):
      print(f"{i}. Nombre: {pais['nombre']}, Población: {pais['poblacion']}, Superficie(Km2): {pais['superficie']}, Continente: {pais['continente']}")
  elif param == "superficie":
    paises.sort(key=itemgetter("superficie"), reverse=descendente)
    print(f"Ordenados por superficie {'de forma descendente' if descendente else 'de forma ascendente'}:")
    for i, pais in enumerate(paises, 1):
      print(f"{i}. Nombre: {pais['nombre']}, Población: {pais['poblacion']}, Superficie(Km2): {pais['superficie']}, Continente: {pais['continente']}")

def estadisticas(paises: list[dict]):
  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)
    for linea in lector:
      [nombre, poblacion, superficie, continente] = linea
      paises.append({"nombre": nombre, "poblacion": int(poblacion), "superficie": int(superficie), "continente": continente})

  pais_mayor_poblacion = max(paises, key=itemgetter("poblacion"))
  print(f"El pais con mayor población es {pais_mayor_poblacion['nombre']} con {pais_mayor_poblacion['poblacion']} habitantes.")

  pais_menor_poblacion = min(paises, key=itemgetter("poblacion"))
  print(f"El pais con menor población es {pais_menor_poblacion['nombre']} con {pais_menor_poblacion['poblacion']} habitantes.")

  promedio_poblacion = sum(pais["poblacion"] for pais in paises) / len(paises)
  print(f"El promedio de población por país es de {promedio_poblacion:.2f} habitantes.")

  promedio_superficie = sum(pais["superficie"] for pais in paises) / len(paises)
  print(f"El promedio de superficie por país es de {promedio_superficie:.2f} Km2.")

  paises_x_continente = {}
  for pais in paises:
    continente = pais["continente"]
    if continente not in paises_x_continente:
      paises_x_continente[continente] = []
    paises_x_continente[continente].append(pais)
  
  for continente, paises_continente in paises_x_continente.items():
    print(f"{continente.capitalize()} tiene un total de {len(paises_continente)} paises.")

def agregar_pais():
  nombre = input("Por favor ingrese el nombre del país que desea agregar a la lista: ")
  while True:
    if len(nombre.strip()) == 0:
      print("El nombre del país no puede estar vacío. Por favor ingrese un nombre válido.")
      nombre = input("Por favor ingrese el nombre del país que desea agregar a la lista: ")
    else:
      break

  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)
    for linea in lector:
      if nombre.title() in linea[0].title():
        print("El país ya existe en la lista. Por favor ingrese un nombre diferente.")
        nombre = input("Por favor ingrese el nombre del país que desea agregar a la lista: ")
        continue

  poblacion = input("Por favor ingrese la población del país: ")
  while True:
    if poblacion.isdigit():
      poblacion = int(poblacion)
      break
    else:
      print("La población ingresada no es válida. Por favor ingrese un número entero.")
      poblacion = input("Por favor ingrese la población del país: ")

  superficie = input("Por favor ingrese la superficie del país: ")
  while True:
    if superficie.isdigit() and int(superficie) > 0:
      superficie = int(superficie)
      break
    else:
      print("La superficie ingresada no es válida. Por favor ingrese un número entero.")
      superficie = input("Por favor ingrese la superficie del país: ")

  continentes = ["America", "Asia", "Africa", "Europa", "Oceania", "Antartida"]
  continente = input("Por favor ingrese el continente del país: ")
  while True:
    if len(continente.strip()) == 0 or continente.title() not in continentes:
      print("El continente ingresado no es válido. Por favor ingrese un continente válido.")
      continente = input("Por favor ingrese el continente del país: ")
    else:
      break

  with open("dataset_paises_undata.csv", "a") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([nombre.title(), poblacion, superficie, continente.title()])
  print(f"El país {nombre} ha sido agregado a la lista.")
  return

def actualizar_poblacion_y_superficie(paises: list[dict]):
  pais_encontrado = False

  while not pais_encontrado:
    pais = input("Ingresar el nombre del país que desea actualizar: ")

    while True:
      if len(pais.strip()) == 0:
        print("El nombre del país no puede estar vacío. Por favor ingrese un nombre válido.")
        pais = input("Ingresar el nombre del país que desea actualizar: ")
      else:
        break

    termino_busqueda = normalizar_palabra(pais.strip().lower())

    #verificamos que el pais exista
    with open("dataset_paises_undata.csv", "r") as archivo:
      lector = csv.reader(archivo)
      next(lector, None)
      for linea in lector:
        [nombre, poblacion, superficie, continente] = linea
        if normalizar_palabra(nombre.strip().lower()) == termino_busqueda:
          pais_encontrado = True
          break

    if not pais_encontrado:
      print("No se encontraron países que coincidan con la búsqueda. Intente nuevamente.")
  
  with open("dataset_paises_undata.csv", "r") as archivo:
    lector = csv.reader(archivo)
    next(lector, None)
    for linea in lector:
      [nombre, poblacion, superficie, continente] = linea
      if termino_busqueda not in normalizar_palabra(nombre.strip().lower()):
        paises.append({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente})
      else:
        nueva_poblacion = input("Por favor ingrese la nueva población del país: ")
        while True:
          if nueva_poblacion.isdigit():
            nueva_poblacion = int(nueva_poblacion)
            break
          else:
            print("La población ingresada no es válida. Por favor ingrese un número entero.")
            nueva_poblacion = input("Por favor ingrese la nueva población del país: ")

        nueva_superficie = input("Por favor ingrese la nueva superficie del país: ")
        while True:
          if nueva_superficie.isdigit() and int(nueva_superficie) > 0:
            nueva_superficie = int(nueva_superficie)
            break
          else:
            print("La superficie ingresada no es válida. Por favor ingrese un número entero.")
            nueva_superficie = input("Por favor ingrese la nueva superficie del país: ")
        paises.append({"nombre": nombre, "poblacion": nueva_poblacion, "superficie": nueva_superficie, "continente": continente})
  
  with open("dataset_paises_undata.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
    for pais in paises:
      escritor.writerow([pais["nombre"], pais["poblacion"], pais["superficie"], pais["continente"]])
  print(f"La población y superficie del país {pais} han sido actualizados.")


print("\nTrabajo integrador de Programación I - Gestión de datos en Python.\n")
while True:
  print("Por favor ingrese una opción para continuar: ")
  opcion = input("1. Buscar un país por nombre. \n2. Filtrar países por continente. \n3. Filtrar países por rango de población. \n4. Filtrar países por rango de superficie(Km2). \n5. Ordenar países por nombre. \n6. Ordenar países por población. \n7. Ordenar países por superficie. \n8. Estadísticas. \n9. Agregar un país a la lista. \n10. Actualizar la población y superficie de un país. \n11. Salir del menú.\n")
  match opcion:
    case "1":
      buscar_pais()
    case "2":
      filtrar_x_continente()
    case "3":
      filtrar_x_rango("poblacion")
    case "4":
      filtrar_x_rango("superficie")
    case "5":
      orden = input("¿Desea ordenar de forma ascendente o descendente? (asc/desc): ")
      while True:
        if orden == "desc":
          ordenar("nombre", [], True)
          break
        elif orden == "asc":
          ordenar("nombre", [], False)
          break
        else:
          print("Opción inválida. Por favor ingrese 'asc' o 'desc'.")
          orden = input("¿Desea ordenar de forma ascendente o descendente? (asc/desc): ")
    case "6":
      orden = input("¿Desea ordenar de forma ascendente o descendente? (asc/desc): ")
      while True:
        if orden == "desc":
          ordenar("poblacion", [], True)
          break
        elif orden == "asc":
          ordenar("poblacion", [], False)
          break
        else:
          print("Opción inválida. Por favor ingrese 'asc' o 'desc'.")
          orden = input("¿Desea ordenar de forma ascendente o descendente? (asc/desc): ")
    case "7":
      orden = input("¿Desea ordenar de forma ascendente o descendente? (asc/desc): ")
      while True:
        if orden == "desc":
          ordenar("superficie", [], True)
          break
        elif orden == "asc":
          ordenar("superficie", [], False)
          break
        else:
          print("Opción inválida. Por favor ingrese 'asc' o 'desc'.")
          orden = input("¿Desea ordenar de forma ascendente o descendente? (asc/desc): ")
    case "8":
      estadisticas([])
    case "9":
      agregar_pais()
    case "10":
      actualizar_poblacion_y_superficie([])
    case "11":
      print("Saliendo del menú...")
      exit()
    case _:
      print("\nOpción inválida. Por favor ingrese una opción válida.")
