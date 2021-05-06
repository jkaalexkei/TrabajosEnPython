print("********************************")
print("")
print("""Programa para calcular el promedio de los numeros
guardados en una lista""")
print("")
print("********************************")
print("")

numero = input("Ingrese la cantidad de numeros que desea guardar: ")#Asignamos el valor ingresado a la variable numero

while numero == "":#comprobamos que el valor ingresado no sea vacio
    print("No ingreso un valor correcto")
    numero = input("Ingrese el numero nuevamente: ")

if int(numero) > 0:#validamos que el valor ingresado sea mayor que cero
    valores = [] #creamos una lista para almacenar los valores que el usuario iingresara para sumar y promediar
    for i in range(int(numero)):#ejecutamos un bucle para recorrer los valores ingresados por el usuario
        dato = input(f"Ingrese dato {i+1}: ")#asignamos a la variable dato el valor ingresado por el usuario
        while dato =="":#ejecutamos un bucle mientras el valor ingresado sea vacio
            print("No ingreso un dato")
            dato = input(f"Ingrese otra vez el dato {i+1}: ")
        
        if int(dato)>0:#si el dato es mayor que cero
            
            valores.insert(i,int(dato))#asignamos a la lista los datos ingresados por el usuario mediante la variable dato
        else:
            print("Ingreso un dato incorrecto")
    
    suma = sum(valores)#sumamos los valores de la lista
    promedio = sum(valores)/int(numero)#sumamos y promediamos los valores
    print(f"La suma de los numeros guardados es: {suma}")#Mostramos en pantalla la suma de los valores de la lista
    print(f"El promedio de los valores es: {promedio}")#promediamos los valores guardados en la lista
            

else:
    print("Ingreso un valor Invalido")