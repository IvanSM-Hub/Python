#Para declarar que una clase es hija de otra debemos importar la clase y especificar al declarar la clase de quien hereda.
from animal import animal
class perro(animal):
    def ladrar(self):
        print("El perro ladra") 

    def comer(self):
        print("El perro come pienso")