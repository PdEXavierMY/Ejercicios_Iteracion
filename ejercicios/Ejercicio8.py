class Separatexto():
  def separatexto(self, texto, separador):
    lista = texto.split(separador)
    return lista

  def iniciar(self):
    texto = str(input("Introduce el texto a separar: "))
    separador = str(input("Introduce un separador para el texto: "))
    print("El texto separado queda así: " + str(Separatexto().separatexto(texto, separador)))