
class CuadradosRaices():
  def cuadradoper(n, limite, lista):
    numero = n**2
    if numero > limite:
      return lista
    else:
      lista.append(numero)
      return CuadradosRaices().cuadradoper(n+1, limite, lista)
  print(cuadradoper(0, 90, []))
  
  def raiz(n, o):
    if o**2 == n:
      return o
    else:
      if o >= n:
        return "Este numero no tiene raíz entera"
      else:
        return CuadradosRaices().raiz(n, o+1)
  print(raiz(20, 0))
  def iniciar():
    start = input('¿Que quieres hacer? Cadrado perfecto (1), Raiz (2) o Salir (0): ')
    while start == 1 or start == 2:
      if int(start) == 1:
        CuadradosRaices().cuadradoper(int(input('Introduce un limite: ')), int(input('Introduce una lista: ')))
        start = input('¿Que quieres hacer? Cadrado perfecto (1), Raiz (2) o Salir (0): ')
      elif int(start) == 2:
        CuadradosRaices().raiz(int(input('Introduce un numero: ')))
        start = input('¿Que quieres hacer? Cadrado perfecto (1), Raiz (2) o Salir (0): ')