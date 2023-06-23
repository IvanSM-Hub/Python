#Trabajar con ficheros externos a Python
#Función: open() -> Sirve para trabajar con Archivos externos.
#variable=open("nombreArchivo.extensión","r(leer)|w(sobre/escribir)|a(anexar)")
#El archivo debe cerrarse siempre -> variable.close()

#Leer
archivo=open("alumnos.txt","r")
#Comprobar que el archivo es leible -> Devuelve booleano 
#print(archivo.readable())

#Leer el archivo
print(archivo.read())

#Leer una línea del archivo
print(archivo.readLine())

#Aparecen todos los elementos del archivo contenido en un array
print(archivo.readLines())
#Podemos acceder a la posición de los contenidos
print(archivo.readLines()[1])
#Recorrer los contenidos del array
for alumno in archivo.readlines():
    print(alumno)

archivo.close()

#Anexar
archivo=open("alumnos.txt","a")

#Añadir elementos a un archivo
archivo.write("\nPedro")

archivo.close()

#Escribir
archivo=open("alumnos.txt","w")

#Añadir elementos a un archivo
archivo.write("Pedro")

archivo.close()

#Crear un archivo
archivo=open("alumnos2.txt","w")

#Añadir elementos a un archivo
archivo.write("Ivan\nMiriam\nSalva")

archivo.close()