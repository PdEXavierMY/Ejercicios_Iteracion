def separatexto(texto, separador):
  lista = texto.split(separador)
  return lista

texto = str(input("Introduce el texto a separar"))
separador = str(input("Introduce un separador del texto"))
print(separatexto(texto, separador))