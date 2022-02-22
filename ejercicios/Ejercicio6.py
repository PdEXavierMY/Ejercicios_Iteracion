from datetime import datetime

class Banco():
  def __init__(self):
    self.cuentas = {
      '1':{
        'nombre': 'Marcos Martinez',
        'balance': 173735,
        'tipo': 1,
        'movimientos': []
      },'2':{
        'nombre': 'Alejandro Sanchez',
        'balance': 1342,
        'tipo': 0,
        'movimientos': []
      },'3':{
        'nombre': 'Claudia Plaza',
        'balance': 120984,
        'tipo': 1,
        'movimientos': []
      },
    }
  def movimiento(self):
    cuenta, cuenta_destino, cantidad = input('Introduce el Número de Cuenta de origen: '), input('Introduce el Número de Cuenta de destino: '), input('Introduce la cantidad a Mover: ')
    balance_cuenta = self.cuentas[str(cuenta)]['balance']
    if not self.cuentas[str(cuenta)]:
      return print('La cuenta de origen no está registrada.')
    if not self.cuentas[str(cuenta_destino)]:
      return print('La cuenta de destino no está registrada.')
    if balance_cuenta < int(cantidad):
      return print('La cantidad introducida es superior a la disponible en la cuenta Nº: ' + str(cuenta) + '.')
    movimientos_cuenta_origen = self.cuentas[str(cuenta)]['movimientos']
    movimientos_cuenta_origen.append({
      'cuenta_destino': str(cuenta_destino),
      'cantidad': '-' + str(cantidad),
      'hora': str(datetime.now())
    })
    self.cuentas[str(cuenta)]['balance'] -= int(cantidad)
    movimientos_cuenta_destino = self.cuentas[str(cuenta_destino)]['movimientos']
    movimientos_cuenta_destino.append({
      'cuenta_origen': str(cuenta),
      'cantidad': '+' + str(cantidad),
      'hora': str(datetime.now())
    })
    self.cuentas[str(cuenta_destino)]['balance'] += int(cantidad)
    print(self.cuentas[cuenta]['movimientos'])
    print(self.cuentas[cuenta]['balance'], self.cuentas[cuenta_destino]['balance'])

start = input('Bienvenido a Bancos Ramirez. ¿Quieres realizar algun operación?(S/N): ')
if start.lower() == 's':
  decision = start
  while decision.lower() == 's':
    Banco().movimiento()
    decision = input('¿Quieres seguir haciendo operaciones?(S/N): ')