# #se usan para datos que no cambian y nos permite definir un conjunto de datos y son mas rapidas que las listas

# #para crear una tupla de un solo elemento se debe colocar una coma despues del elemento de la tupla

# tupla = (1,2,3,4)
# print(type(tupla))

# y = tuple({2,3,4,5})

# print(type(y))

# #DIFERENCIA ENTRE TUPLA, LISTA, SET, DICCIONARIO
# s = {1,2,3}#SET

# l = [1,2]#LIST

# dc = {"hola":123}#DIICCIONARIO

# print(type(s))
# print(type(l))
# print(type(dc))

#TUPLAS: Lista inimutables no pueden cambiar o modificar

mitupla=("alex",13)

milis = list(mitupla)#convierte a lista una tupla


nombre , edad = mitupla

print(nombre , " " , edad)

print(mitupla.index(13))








