#Clases
#Hay algunos datos que no se pueden almacenar en una variable simple, como estructuras.
#Las clases se deben definir en un archivo aparte en este caso "alumno.py" en el que montaremos la estructura de dicha clase.
#Posteriormente deberemos importar nuestra clase "alumno.py", al documento desde el que vamos a trabajar los objetos.
from alumno import alumno

#Creación de un objeto de la clase alumno.
alumno1=alumno("Juan",22,"Arquitectura",7.1)
alumno2=alumno("Pablo",22,"Enfermería",4.2)

#Acceder a un elemtno del objeto
print(alumno1.nombre)
print(alumno1.edad)
print(alumno1.nota)
print(alumno2.nota)

#Uso de funciones de Clase, estas funciones deben declarase en su clase
print(alumno1.aprobado())
print(alumno2.aprobado())