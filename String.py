#Acceder a elementos de un string
texto="Estamos programando en Python"
print(texto[0])
print(texto[0:7])
print(texto[:19])
print(texto[8:])
print(texto[0:29:2])
print(texto[::-1])

#Funciones habituales con strings
print(len(texto))
print(texto.capitalize())
print(texto.replace("Python","JavaScript"))
print(texto.index("P"))
print(texto.index("programando"))
print(texto.lower())
print(texto.upper())
print(texto.islower())
print(texto.isupper())
print(texto.isalnum())
print(dir(texto))