import sys
sys.path.insert(1, './ejercicios')
from ejercicios import Ejercicio6, Ejercicio12

array_ejercicios = {
  6: 'Ejercicio6.Banco().iniciar()',
  12: 'Ejercicio12.CuadradosRaices().iniciar()'
}

if __name__ == "__main__":
  start = input('Bienvenido a la plataforma de ejercicios desarrollada por Matota Network. Por favor, introduzca el número del ejercicio que quiere probar (6 a 12): ')
  while int(start) >= 6 and int(start) <= 12:
    eval(str(array_ejercicios[int(start)]))
    start = input('Por favor, introduzca el número del ejercicio que quiere probar (6 a 12) o 0 para salir: ')