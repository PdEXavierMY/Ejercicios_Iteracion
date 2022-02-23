import sys
sys.path.insert(1, './ejercicios')
from ejercicios import Ejercicio6, Ejercicio7, Ejercicio8, Ejercicio9, Ejercicio12, Ejercicio11, Ejercicio10

array_ejercicios = {
  6: 'Ejercicio6.Banco().iniciar()',
  7: 'Ejercicio7.Cambiobase().iniciar()',
  8: 'Ejercicio8.Separatexto().iniciar()',
  9: 'Ejercicio9.Diccionario().iniciar()',
  12: 'Ejercicio12.CuadradosRaices().iniciar()',
  11: 'Ejercicio11.Mcd().iniciar()',
  10: 'Ejercicio10.Familias().crearTabla()'
}

if __name__ == "__main__":
  start = input('Bienvenido a la plataforma de ejercicios desarrollada por Matota Network. Por favor, introduzca el número del ejercicio que quiere probar (6 a 12): ')
  while int(start) >= 6 and int(start) <= 12:
    eval(str(array_ejercicios[int(start)]))
    start = input('Por favor, introduzca el número del ejercicio que quiere probar (6 a 12) o 0 para salir: ')