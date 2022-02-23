def mcd(n, m):
  if n < m:
    return mcd(m, n)
  elif m == 0:
    return n
  else:
    return mcd(m, n%m)
n = int(input("Introducza el primer número del mcd por metodo euclides"))
m = int(input("Introducza el segundo número del mcd por metodo euclides"))
print("El mcd de " + m + " y " + n + " por euclides es " + str(mcd(n, m)))

def mcdresta(n, m): 
    if n < m:
      return mcdresta(m, n)
    if m == 0: 
        return n 
    if n == m: 
        return n 
    if n > m: 
        return mcdresta(n-m, m) 
    return mcdresta(n, m-n)
nr = int(input("Introducza el primer número del mcd por metodo sumas y restas"))
mr = int(input("Introducza el segundo número del mcd por metodo sumas y restas"))
print("El mcd de " + mr + " y " + nr + " por sumas y restas es " + str(mcdresta(nr, mr)))