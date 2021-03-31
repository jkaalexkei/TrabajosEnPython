
# lista = [10,"texto",10.2,True,[1,2,3]]

colores = ['rojo','verde','azul']


# numero_de_lista = list({1,2,3,4})#contructor para crear listas
# #PARA VISUALIZAR LA LISTA DE LA LINEA ANTERIOR LO PODEMOS HACER MEDIANTE UNA TUPLA
# print(numero_de_lista)


# rango = list(range(1, 10))# muestra una lista en un rango de valores 

# print(rango)

# print(colores[2])#aca mostramos un elemento en particular de una lista

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

