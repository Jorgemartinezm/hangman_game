string = "aloha jamón andaluz"

# Creamos una lista llamada posiciones para almacenarlas
posiciones = []

# Buscar la primera ocurrencia de por ejemplo la letra "a" en el string
pos = string.find("a")

# Mientras se encuentre la letra "a" en el string...
while pos != -1:
  #  Añadimos la posicion a la lista.
  posiciones.append(pos)
  
  # Buscar la siguiente ocurrencia de la letra "a" en el string
  pos = string.find("a", pos + 1)


print(posiciones)