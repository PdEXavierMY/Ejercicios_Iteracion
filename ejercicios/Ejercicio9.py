palabras={
  1:{
    'palabra': 'avion',
    'anterior': 11,
    'siguiente': 9
  },
  2:{
    'palabra': 'coche',
    'anterior': 7,
    'siguiente': 11
  },
  3:{
    'palabra': 'gorro',
    'anterior': '',
    'siguiente': 6
  },
  4:{
    'palabra': 'pan',
    'anterior': 8,
    'siguiente': ''
  },
  5:{
    'palabra': 'iglesia',
    'anterior': 9,
    'siguiente': 10
  },
  6:{
    'palabra': 'pagina',
    'anterior': 3,
    'siguiente': 7
  },
  7:{
    'palabra': 'orar',
    'anterior': 6,
    'siguiente': 2
  },
  8:{
    'palabra': 'anaconda',
    'anterior': 10,
    'siguiente': 4
  },
  9:{
    'palabra': 'programar',
    'anterior': 1,
    'siguiente': 5
  },
  10:{
    'palabra': 'cuaderno',
    'anterior': 5,
    'siguiente': 8
  },
  11:{
    'palabra': 'zapato',
    'anterior': 2,
    'siguiente': 1
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

palabra={
  'avion': [11, 9], #1
  'coche':[7, 11], #2
  'gorro':['', 6], #3
  'pan':[8, ''], #4
  'iglesia':[9, 10], #5
  'pagina':[3, 7], #6
  'orar':[6, 2], #7
  'anaconda':[10, 4], #8
  'programar':[1, 5], #9
  'cuaderno':[5, 8], #10
  'zapato':[2, 1], #11
}

def buscar_diccionariov2():
  letra = str(input("Da una letra: ")).lower()
  listapalabra = []
  for i in palabra:
    if i[0] == str(letra):
      listapalabra.append(i)
  if listapalabra == []:
      return "No hay ninguna palabra en el diccionario que empiece por la letra que has dado."
  else:
    return listapalabra

print("Las palabras del diccionario que empiezan por la letra dada son: " + str(buscar_diccionariov2()))

def añadirpalabra():
  nuevapalabra = str(input("Especifique la nueva palabra a introducir en el diccionario: ")).lower()
  n = int(len(palabra))
  contador = 0
  for i in palabra:
    contador += 1
    if palabra[i][1] == '':
      palabra[i][1] = n+1
      break
  palabra[nuevapalabra] = [contador, '']
  return palabra

print("El nuevo diccionario queda así: " + str(añadirpalabra()))

def quitarpalabra():
  print(palabra)
  palabrafuera = str(input("¿Que palabra del diccionario desea eliminar?: "))
  lista = []
  n = 0
  for i in palabra:
    if i == str(palabrafuera):
      del palabra[str(palabrafuera)]
    else:
      n += 1
    lista.append(i)
  if n == len(lista):
    print("La palabra introducida no está en el diccionario.")
  else:
    return lista

print("El nuevo diccionario queda así: " + str(quitarpalabra()))