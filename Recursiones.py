#Funciones Recursivas:
#Consiste en definir el valor de una variable utilizando esa propia variable (Sucesión de Fibonacci)
def fibonacci(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)

print(fibonacci(4))