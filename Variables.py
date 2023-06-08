#Inicialización de variables en Python, Nombres comprensibles y se inicializan de a-z | _ | key sensitive

numero = 2
a = 3
print(numero)
print(a)

numero = 3
print(numero)

a=2
b=3
c=a+b
print(c)

_numero=2
print(_numero)

numero_2=6
print(numero_2)

numero=7
Numero=5

#Tipos de datos

entero=7
print(type(entero))

decimal=-12.3
print(type(decimal))

complejo=1+3j
print(type(complejo))

texto="Aquí va el texto"
print(type(texto))

booleanTrue=True
booleanFalse=False
print(type(booleanTrue))

#Solicitar variables al usuario
edad = int(input("Introduce una edad: "))
nombre = input("introduce tu nombre: ")
validacion=bool(input("Introduce si es True o False: "))
print("Te llamas "+nombre+" y tienes "+str(edad)+" años"+" esto es: "+str(validacion))