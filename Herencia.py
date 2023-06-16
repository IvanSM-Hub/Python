#Herencia
#Podemos crear una clase padre que tenga viertos atributos y funciones, que además otras clases "hijas" hereden para poder utilizar.
from animal import animal
from perro import perro

animal1=animal()
perro1=perro()

animal1.dormir()
animal1.come()

perro1.come()
perro1.ladra()