def separatexto(texto, separador):
  lista = texto.split(separador)
  return lista

texto = "Hoy comí carne en casa, jugé a la pelota, visité un santuario, me zambullí en la piscina y jugé a los bolos"
print(separatexto(texto, ","))