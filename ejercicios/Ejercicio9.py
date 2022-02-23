palabras={
  1:{
    'palabra': 'avion',
    'siguiente': 2,
    'anterior': 8
  },
  2:{
    'palabra': 'coche',
    'siguiente': 10,
    'anterior': 1
  },
  3:{
    'palabra': 'gorro',
    'siguiente': 7,
    'anterior': 10
  },
  4:{
    'palabra': 'pan',
    'siguiente': 9,
    'anterior': 6
  },
  5:{
    'palabra': 'iglesia',
    'siguiente': 1,
    'anterior': 2
  },
  6:{
    'palabra': 'pagina',
    'siguiente': 4,
    'anterior': 7
  },
  7:{
    'palabra': 'orar',
    'siguiente': 6,
    'anterior': 3
  },
  8:{
    'palabra': 'anaconda',
    'siguiente': 1,
    'anterior': 0
  },
  9:{
    'palabra': 'programar',
    'siguiente': 11,
    'anterior': 4
  },
  10:{
    'palabra': 'cuaderno',
    'siguiente': 3,
    'anterior': 2
  },
  11:{
    'palabra': 'zapato',
    'siguiente': 12,
    'anterior': 9
  },
}

def buscar_diccionario():
  letra = str(input("Da una letra: ")).lower()
  listapalabra = []
  for i in palabras:
    if palabras[i]["palabra"][0] == str(letra):
      listapalabra.append(palabras[i]["palabra"])
  if listapalabra == []:
      return "No hay ninguna palabra en el diccionario que empiece por la letra que has dado."
  else:
    return listapalabra

print("Las palabras del diccionario que empiezan por la letra dada son: " + str(buscar_diccionario()))