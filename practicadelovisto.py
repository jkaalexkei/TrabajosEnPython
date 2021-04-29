import math

#calcular el promediio de numeros ingresados

numero = input("Ingrese cantidad de numeros a promediar: ")

cont = 1

while numero == "":
    print("no ingreso un numero")
    numero = input("Intente de nuevo: ")
    if numero == "":
        print("no ingreso un numero")
        numero = input("Intente de otra vez: ")
    else:
        cont+=1
        valores = []
        
        for i in range(int(numero)):
            dato = input(f"Ingrese valor {i+1}: ")
            if dato == "":
                print("no ingreso un numero")
                dato = input(f"Ingrese valor {i+1} otra vez: ")
            else:
                valores.insert(i,int(dato))
                
valores = []
        
for i in range(int(numero)):
    dato = input(f"Ingrese valor {i+1}: ")
    if dato == "":
        print("no ingreso un numero")
        dato = input(f"Ingrese valor {i+1} otra vez: ")
    else:
        valores.insert(i,int(dato))

promedio = sum(valores)/int(numero)
print(f"El resultado del promedio es: {promedio}")
print("continuamos con la ejecucion")

    


    

    




# import math
# lista = []
# precios = []

# elementos = 2

#for i in range(elementos):

#     valores = input("ingrese info: ")
#     costo = float(input("Costo: "))

#     lista.insert(i,valores)
#     precios.insert(i,costo)

# for i in lista:
#     print(i)

# print(precios)
# print(sum(precios))
# milista = []#creamos un lisra

# cant = int(input("Cantidad de productos: "))#creamos una variable para almacenar el numero de elementos a ingresar en la lista

# for i in range(cant):#este bucle for se ejecutara en un rango establecido en la variable cantidad

#     productos = input("Ingrese Productos: ")#en cada vuelta del bucle asignamos a la variable producto el alimento ingresado por el usuario

#     milista.insert(i,productos)#aqui insertamos en la lista los elementos almacenados en la variable producto

# for j in milista:#en este bucle recorremos la lista para mostrar en pantalla sus elementos
#     item = milista.index(j) + 1 #en la variable item alamacenamos la numeracion de la lista
#     print(f"{item}.-usted pidio--> " + str(j))#en este mensaje mostramos los elementos ordenados de la lista


# domicilio = []

# cantidad = int(input("Ingrese numero de productos a facturar: "))

# for i in range(cantidad):

#     pedido = input("Nombre del Producto: ")
#     domicilio.insert(i,pedido)
    
        
# for j in domicilio:
#     num=domicilio.index(j)+1
#     print(f"{num}.-Productos pedidos: " + str(j))





