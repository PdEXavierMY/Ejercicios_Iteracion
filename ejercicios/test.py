# Ejercicio 9
n1 = 2 
n2 = 3
n3 = 6

media = (n1 + n2 + n3)/3

print(media)

# Ejercicio 10
frase = "Logre ver gol"
frase_split_upper = frase.upper().split()
frase_split_lower = frase.lower().split()

print(''.join(frase_split_upper))
print(''.join(frase_split_lower))

if ''.join(frase_split_upper) == ''.join(frase_split_upper)[::-1]:
  print('Es palíndromo')
else:
  print(''.join(frase_split_upper), ''.join(frase_split_upper)[::-1])
  print('No es palíndromo')