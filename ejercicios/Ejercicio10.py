import names
import random
import os

class Familias():
  def __init__(self):
    global personas
    self.personas = []
    self.i_ = 0
    self.ai = 0
    global padres
    self.padres = []
    global madres
    self.madres = []
  def crearTabla(self):
    global personas
    global padres
    global madres
    self.padres.append('Jaime Martin')
    for i in range(20):
      self.padres.append(str(names.get_full_name(gender='male')))
    for i in range(20):
      self.madres.append(str(names.get_full_name(gender='female')))
    for i in range(99):
      nombre = names.get_full_name()
      if random.randint(0, 15) == 1:
        padre = 'Huérfano'
        madre = 'Huérfano'
      else:
        padre = self.padres[random.randint(0, 20)]
        madre = self.madres[random.randint(0, 19)]
      self.personas.append({
      'id': i,
      'identidad':{
        'nombre': nombre.split()[0],
        'apellido': nombre.split()[1]
      },
      'edad': random.randint(0, 99),
      'padre': padre,
      'madre': madre
      })
      self.ai += 1
      if self.ai == 10:
        self.ai = 0
        os.system('clear')
        puntos = ['', '.', '..', '...']
        if self.i_ == 3:
          self.i_ = 0
        else:
          self.i_ += 1
        print('Creando tabla "personas". Por favor, espere' + puntos[self.i_])

    self.personas.append({
      'id': 100,
      'identidad':{
        'nombre': 'Jaime',
        'apellido': 'Martin'
      },
      'edad': random.randint(0, 99),
      'padre': self.padres[random.randint(1, 20)],
      'madre': self.madres[random.randint(0, 19)]
    })
    print('Tabla personas creada exitosamente (' + str(len(self.personas)) + ' entradas)')
    def encontrarEdades(self):
      global personas
      print(self.personas)
      for i in range(100):
        if self.personas[i]['edad'] <= 20 and self.personas[i]['edad'] <= 30:
          print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + '. Edad: ' + str(self.personas[i]['edad']))
    def añadirUnAño(self):
      global personas
      for i in range(100):
        self.personas[i]['edad'] += 1
      print('Ahora todas las personas tienen 1 año más.')
    def encontrarHuerfanos(self):
      global personas
      global padres
      global madres
      for i in range(100):
        if self.personas[i]['edad'] <= 15 and self.personas[i]['madre'] == 'Huérfano':
          print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + '. Edad: ' + str(self.personas[i]['edad']) + '. Estado: ' + str(self.personas[i]['madre']))
    def hijosJaime(self):
      global personas
      global padres
      global madres
      for i in range(100):
        if self.personas[i]['padre'] == 'Jaime Martin':
          print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + '. Edad: ' + str(self.personas[i]['edad']) + '. Padre: ' + str(self.personas[i]['padre']))
    def hermanosJaime(self):
      global personas
      global padres
      global madres
      for i in range(100):
        if self.personas[i]['padre'] == self.personas[100]['padre'] or self.personas[i]['madre'] == self.personas[100]['madre']:
          print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + ' es herman@ de Jaime Martin.')
        
    array_ejercicios = {
      1: 'Familias().crearTabla().añadirUnAño()',
      2: 'Familias().crearTabla().encontrarHuerfanos()',
      3: 'Familias().crearTabla().hijosJaime()',
      4: 'Familias().crearTabla().hermanosJaime()',
      5: 'Familias().crearTabla().encontrarEdades()',
    }
    decision = input('Bienvenido al organizador de Familias. ¿Que quieres hacer?: Añadir 1 año a todas las personas (1), Establecer una lista con los menores de 15 años (2), Encontrar los hijos de Jaime Martin (3), Encontrar los hemanos de Jaime Martin (4), Dar una lista con las personas con edades comprendidas entre 20 y 30 años (5) o Salir (0)')
    while int(decision) > 0 and int(decision) <= 5:
      eval(str(array_ejercicios[int(decision)]))
      decision = input('¿Que quieres hacer?: Añadir 1 año a todas las personas (1), Establecer una lista con los menores de 15 años (2), Encontrar los hijos de Jaime Martin (3), Encontrar los hemanos de Jaime Martin (4), Dar una lista con las personas con edades comprendidas entre 20 y 30 años (5) o Salir (0)')