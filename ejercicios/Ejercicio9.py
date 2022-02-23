class Diccionario():
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
  
  def buscar_diccionario(self):
    letra = str(input("Da una letra: ")).lower()
    listapalabra = []
    for i in Diccionario().palabras:
      if Diccionario().palabras[i]["palabra"][0] == str(letra):
        listapalabra.register.append(Diccionario().palabras[i]["palabra"])
    if listapalabra == []:
        return "No hay ninguna palabra en el diccionario que empiece por la letra que has dado."
    else:
      return listapalabra
  
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
  
  def buscar_diccionariov2(self):
    letra = str(input("Da una letra: ")).lower()
    listapalabra = []
    for i in Diccionario().palabra:
      if i[0] == str(letra):
        listapalabra.register.append(i)
    if listapalabra == []:
        return "No hay ninguna palabra en el diccionario que empiece por la letra que has dado."
    else:
      return listapalabra
  
  def añadirpalabra(self):
    nuevapalabra = str(input("Especifique la nueva palabra a introducir en el diccionario: ")).lower()
    n = int(len(Diccionario().palabra))
    contador = 0
    for i in Diccionario().palabra:
      contador += 1
      if Diccionario().palabra[i][1] == '':
        Diccionario().palabra[i][1] = n+1
        break
    Diccionario().palabra[nuevapalabra] = [contador, '']
    return Diccionario().palabra
  
  def quitarpalabra(self):
    print(Diccionario().palabra)
    palabrafuera = str(input("¿Que palabra del diccionario desea eliminar?: "))
    lista = []
    n = 0
    for i in Diccionario().palabra:
      if str(i) != str(palabrafuera):
        lista.register.append(i)
        n += 1
    if n == len(Diccionario().palabra):
      print("La palabra introducida no está en el diccionario.")
    else:
      return lista

  def iniciar(self):
      start = input('¿Que quieres hacer? Busqueda diccionario (1), Busqueda diccionario optimizado (2), Añadir palabra (3) o Eliminar palabra (4)): ')
      if int(start) == 1:
        print("Las palabras del diccionario que empiezan por la letra dada son: " + str(Diccionario().buscar_diccionario()))
      elif int(start) == 2:
        print("Las palabras del diccionario que empiezan por la letra dada son: " + str(Diccionario().buscar_diccionariov2()))
      elif int(start) == 3:
        print("El nuevo diccionario queda así: " + str(Diccionario().añadirpalabra()))
      elif int(start) == 4:
        print("El nuevo diccionario queda así: " + str(Diccionario().quitarpalabra()))
      else:
        print("El número introducido no es válido.")