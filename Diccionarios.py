#Diccionario:
#Tipo de estructura de datos que contiene parejas de claves y valores, por lo que va a relacionar dos elementos diferentes
#que van a ser una clave y un valor para definir un diccionario.

alumnos = {"Juan":23,"Pedro":26,"Laura":24}
print(alumnos)

#para acceder a un elemento solo se podrá a través de la clave
print(alumnos["Pedro"])
print(alumnos.get("pablo","No aparece"))

#asociar un nuevo valor a una clave
alumnos["Juan"]=24
print(alumnos)

#añadir un elemento
alumnos["Pablo"]=21
print(alumnos)

#eliminar un elemento
del alumnos["Pablo"]
print(alumnos)

#buscar un elemento
print("Juan" in alumnos)
print("Francisco" in alumnos)
