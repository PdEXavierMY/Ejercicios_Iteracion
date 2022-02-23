class Mcd():
  def mcd(self, n, m):
    if n < m:
      return Mcd().mcd(m, n)
    elif m == 0:
      return n
    else:
      return Mcd().mcd(m, n%m)
  
  def mcdresta(self, n, m): 
      if n < m:
        return Mcd().mcdresta(m, n)
      if m == 0: 
          return n 
      if n == m: 
          return n 
      if n > m: 
          return Mcd().mcdresta(n-m, m) 
      return Mcd().mcdresta(n, m-n)

  def iniciar(self):
    n = int(input("Introducza el primer número del mcd por metodo euclides: "))
    m = int(input("Introducza el segundo número del mcd por metodo euclides: "))
    print("El mcd de " + str(m) + " y " + str(n) + " por euclides es " + str(Mcd().mcd(n, m)))
    nr = int(input("Introducza el primer número del mcd por metodo sumas y restas: "))
    mr = int(input("Introducza el segundo número del mcd por metodo sumas y restas: "))
    print("El mcd de " + str(mr) + " y " + str(nr) + " por sumas y restas es " + str(Mcd().mcdresta(nr, mr)))