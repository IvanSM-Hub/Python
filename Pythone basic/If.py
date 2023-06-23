#If:
#Nos va a permitir ejecutar una serie de instrucciones en el caso que se cumpla o no una condición.
num1=10
num2=8
num3=12
if num1>=num2 and num1>=num3:
    print("El número "+str(num1)+" es el mayor")
elif num2>=num1 and num2>=num3:
    print("El número "+str(num2)+" es el mayor")
elif num3>=num1 and num3>=num2:
    print("El número "+str(num3)+" es el mayor")

#Viendo la siguiente condición elif entendemos que todas las condiciones se cumplen, pero solo se mostrará la primera condición ya que el programa lee de manera consecutiva.
num4=2
if num4<10:
    print("El número es menor que 10")
elif num<20:
    print("El número es menor que 20")
elif num<30:
    print("El número es menor que 30")
else:
    print("El número es mayor que 30")