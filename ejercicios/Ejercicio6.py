from datetime import datetime
import pygame
import sys

class Banco():
  def __init__(self):
    self.cuentas = {
      '9084639567':{
        'nombre': 'Marcos Martinez',
        'balance': 173735,
        'tipo': 1,
        'movimientos': []
      },'9103947823':{
        'nombre': 'Alejandro Sanchez',
        'balance': 1342,
        'tipo': 0,
        'movimientos': []
      },'1932098546':{
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
    movimientos_cuenta = self.cuentas[str(cuenta)]['movimientos']
    movimientos_cuenta.append({
      'cuenta_origen': str(cuenta),
      'cantidad': int(cantidad),
      'hora': str(datetime.now())
    })
    print(self.cuentas['9084639567']['movimientos'])

print('Bienvenido a Bancos Ramirez. ¿Quieres realizar algun operación?(S/N): ')
decision = input('¿Quieres sefuir haciendo opraciones?(S/N): ')