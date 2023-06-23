#Listas
edades=[23,26,24]
nombres=["iván","míriam","salva"]
aprobados=[True,False,True]

lista=["texto",26,2.4,True]

print(lista)

print(lista[0])

#Modificar elementos de una lista

#meter un nuevo elemento
nombres.append("pedro")
edades.append(35)

print(nombres)
print(edades)

#insertar
nombres.insert(1,"pedro")

#eliminar
nombres.remove("salva")

#se eliminan todos los elementos de la lista
#nombres.clear()

#Saber si un elemento de la lista existe
print("iván" in nombres)
print(nombres.index("míriam"))

#Asignar un nuevo valor en una posición ya ocupada
nombres[0]="justo"
print(nombres)
edades[2]+=1
print(edades)

#Funciones habituales en listas
#Número de coincidéncias en una lista
print(edades.count(23))

#Cómo juntar 2 listas
edades2=[26,29,54,34,56,15,25,26]
edades.extend(edades2)
print(edades)

#Eliminar un elemento de una lista pero devolviendolo
print(edades.pop(0))

#Cambia el orden de la lista
nombres.reverse()
print(nombres)

#Ordenar la lista alfabéticamente o númericamente
nombres.sort()
print(nombres)
edades.sort()
print(edades)

#Copiar una lista
edadesCopia=edades.copy()
print(edades)
print(edadesCopia)