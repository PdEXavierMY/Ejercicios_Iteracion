class CuadradosRaices():
  def cuadradoper(self, n, limite, lista):
    numero = n**2
    if numero > limite:
      return lista
    else:
      lista.append(numero)
      return CuadradosRaices().cuadradoper(n+1, limite, lista)
  
  def raiz(self, n, o):
    if o**2 == n:
      return o
    else:
      if o >= n:
        return "Este numero no tiene raíz entera"
      else:
        return CuadradosRaices().raiz(n, o+1)
    print(CuadradosRaices().raiz(20, 0))
  def iniciar(self):
    start = input('¿Que quieres hacer? Cuadrado perfecto (1), Raiz (2) o Salir (0): ')
    while int(start) == 1 or int(start) == 2:
      if int(start) == 1:
        print(CuadradosRaices().cuadradoper(0 ,int(input('Introduce un limite: ')), []))
        start = input('¿Que quieres hacer? Cadrado perfecto (1), Raiz (2) o Salir (0): ')
      elif int(start) == 2:
        print(CuadradosRaices().raiz(int(input('Introduce un numero: ')), 0))
        start = input('¿Que quieres hacer? Cadrado perfecto (1), Raiz (2) o Salir (0): ')