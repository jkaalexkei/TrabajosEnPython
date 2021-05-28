
# lista = [10,"texto",10.2,True,[1,2,3]]

colores = ['rojo','verde','azul']


# numero_de_lista = list({1,2,3,4})#contructor para crear listas
# #PARA VISUALIZAR LA LISTA DE LA LINEA ANTERIOR LO PODEMOS HACER MEDIANTE UNA TUPLA
# print(numero_de_lista)


# rango = list(range(1, 10))# muestra una lista en un rango de valores 

# print(rango)

# print(colores[2])aca mostramos un elemento en particular de una lista

# print('marron' in colores)#con esta instruccion sabemos si un elemento se encuentra en una lista

# #editar elementos de una lista

# # print(colores)
# # colores[2] = 'negro'
# # print(colores)

# # colores.append('violeta')#AGREGA UN ELEMENTO A LA LISTA
# # print(colores)

# # colores.extend({'naranja','amarillo'})#CON ESTE METODO PODEMOS AGREGAR VARIOS ELEMENTOS A LA LISTA MEDIANTE UNA TUPLA
# print(colores)

# colores.insert(2,'negro')#Agrega elementos a una lista en una posicion determinada
# print(colores)

colores.insert(len(colores),'naranja')# aca se evalua la longitud de la lista colores y en funcion de eso agrega al final el elemento naranja mediante el metodo insert

print(colores)

colores.pop()#Elimina el ultimo elemento de una lista

#print(colores)

#colores.remove('azul')#Remueve o quita un elemento en particular
#print(colores)

#colores.clear()#elimina todos los elementos de una lista

print(colores)

colores.sort()#ordena los elementos de una lista
print(colores)

colores.sort(reverse=True)#ordena los elementos de una lista de manera inversa
print(colores)


print(colores.index('rojo'))#Obtenemos el indice de un elemento
print(colores.count('rojo'))#cuenta el numero de elementos segun el parametro establecido

##################LISTAS######################################

lista = [1,1.2,"a"]

o = type(lista)

miLista = ["maria","pepe","marta","antonio"]

print(miLista)

print(miLista[-2])#Cuenta del ultimo al primer elemento

#acceder a una parte de la lista [inicio:fin]

#print(miLista[2:])

#agregar elementos a la lista

miLista.append("alex")#agrega elementos al final de la lista
miLista.insert(1,"keidy")#agrega un elemento en una posicion especificada de la lista

miLista.extend(["pablo","pedro","luis"])#agrega varias elementos a la lista

print(miLista.index("marta"))#devuelve la posicion del elemento establecido

#print(miLista)

print("alex" in miLista)#la funcion in verifica si un elemento esta una lista

miLista.remove("alex")#Elimina un elemento de la lista

miLista.pop()#elimmina el ultimo elemento de una lista

















