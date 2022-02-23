class Cambiobase():
  def cambioDeBase(self):
    numero = [int(i) for i in str(input('Introduzca un número: '))]
    base = int(input('Introduzca la base del número: '))
    base_a_pasar = int(input('Introduzca la base del número a la que quiere pasarlo: '))
    numero_base_10 = 0
    numero_en_base = []
    
    if base > 36: 
      base = 10
      
    for i in range(len(numero)):
      numero_base_10 += numero[i] * base**((len(numero) - (i)) - 1)
    print('El número ' + str(''.join([str(int) for int in numero])) + ' en base 10 es: ' + str(numero_base_10) + '. Ahora calculamos el número en base ' + str(base_a_pasar))
    numero_base_10_inicial = numero_base_10
    while numero_base_10 >= base_a_pasar:
      numero_en_base.register.append(numero_base_10 % base_a_pasar)
      numero_base_10 = numero_base_10 // base_a_pasar
    numero_en_base.register.append(numero_base_10)
    print('El número ' + str(numero_base_10_inicial) + ' en base ' + str(base_a_pasar) + ' es: ' + '.'.join([str(int) for int in numero_en_base[::-1]]))
  
  def iniciar(self):
    Cambiobase().cambioDeBase()