#Funciones:
#Bloque de código que realiza una tarea específica definienda, cada vez que deseemos realizar dicha función solamente deberemos llamar a la función.
def saludo(nombre, edad):
    print("Te llamas "+str(nombre)+" y tienes "+str(edad)+" años")

saludo("Iván",27)
saludo("Míriam",30)
saludo("Salva",29)

nombre="Juan"
edad=21
saludo(nombre,edad)

def fuerza(peso):
    g=9.8
    print(peso*g)

#Cuando se ejecute la sentencia return la función quedará por finalizada y todo lo que haya después quedará como perdido
def valor_medio(num1,num2):
    media=(num1+num2)/2
    return media

valorMedio=valor_medio(8,4)
print(valorMedio)