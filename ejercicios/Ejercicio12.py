def cuadradoper(n, limite, lista):
  numero = n**2
  if numero > limite:
    return lista
  else:
    lista.append(numero)
    return cuadradoper(n+1, limite, lista)

print(cuadradoper(0, 90, []))

def raiz(n, o):
  if o**2 == n:
    return o
  else:
    if o >= n:
      return "Este numero no tiene raíz entera"
    else:
      return raiz(n, o+1)

print(raiz(20, 0))