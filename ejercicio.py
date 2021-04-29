print("********************************")
print("")
print("""Programa para calcular el promedio de los numeros
guardados en una lista""")
print("")
print("********************************")
print("")

numero = input("Ingrese la cantidad de numeros que desea guardar: ")

while numero == "":
    print("No ingreso un valor correcto")
    numero = input("Ingrese el numero nuevamente: ")

if int(numero) > 0:
    valores = []
    for i in range(int(numero)):
        dato = input(f"Ingrese dato {i+1}: ")
        while dato =="":
            print("No ingreso un dato")
            dato = input(f"Ingrese otra vez el dato {i+1}: ")
        
        if int(dato)>0:
            
            valores.insert(i,int(dato))
        else:
            print("Ingreso un dato incorrecto")
    
    suma = sum(valores)
    promedio = sum(valores)/int(numero)
    print(f"La suma de los numeros guardados es: {suma}")
    print(f"El promedio de los valores es: {promedio}")
            
else:
    print("Ingreso un valor Invalido")