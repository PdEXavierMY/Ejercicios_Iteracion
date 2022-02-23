import names
import random
import os

class Familias():
  def __init__(self):
    self.personas = []
    self.i_ = 0
    self.ai = 0
    self.padres = []
    self.madres = []
  def crearTabla(self):
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
      print(self.personas[i])

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
    print(self.personas)
    for i in range(100):
      if self.personas[i]['edad'] <= 20 and self.personas[i]['edad'] <= 30:
        print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + '. Edad: ' + str(self.personas[i]['edad']))
  def añadirUnAño(self):
    for i in range(100):
      self.personas[i]['edad'] += 1
    print('Ahora todas las personas tienen 1 año más.')
  def encontrarHuerfanos(self):
    for i in range(100):
      if self.personas[i]['edad'] <= 15 and self.personas[i]['madre'] == 'Huérfano':
        print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + '. Edad: ' + str(self.personas[i]['edad']) + '. Estado: ' + str(self.personas[i]['madre']))
  def hijosJaime(self):
    for i in range(100):
      if self.personas[i]['padre'] == 'Jaime Martin':
        print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + '. Edad: ' + str(self.personas[i]['edad']) + '. Padre: ' + str(self.personas[i]['padre']))
  def hermanosJaime(self):
    for i in range(100):
      if self.personas[i]['padre'] == self.personas[100]['padre'] or self.personas[i]['madre'] == self.personas[100]['madre']:
        print(str(self.personas[i]['identidad']['nombre']) + ' ' + str(self.personas[i]['identidad']['apellido']) + ' es herman@ de Jaime Martin.')



Familias().crearTabla()

Familias().encontrarEdades()