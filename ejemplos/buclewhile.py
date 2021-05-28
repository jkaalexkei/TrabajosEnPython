# lista = ["jkaalex"]

# for i in lista[0]:
#     print(i)

# def getSuma(n):
#     suma = 0
#     for digit in str(n):
#         suma += int(digit)
    
#     return suma

# n = 12345
# print(getSuma(n))


# i = 1

# while i <= 3:
#     print(i)
#     i+=1

# print("termino la ejecucion")


texto = input("Ingrese un texto: ")#se ingresa un texto

contador = 1 #inicializamos el contador en 1

while texto == "":#bucle para comprar lo ingresado en la variable texto
    texto = input("Ingrese de nuevo el  texto " + f"llevas {contador} intento: ")#informamos el numero de intentos ingresados en caso de ser vacio
    if contador >= 3:#validamos si el contador ha alcanzado el numero maximo de 3
        print("Alcanzo el limite de intentos " + str(contador))#informamos que alcanzo el numero de maximo de intentos permitidos
        break#rompemos el flujo de ejecucion
    else:#en caso contrario
        contador+=1#incrementamos la variable contador
    
if texto =="":#validamo si el texto es vacio
    print("Ingreso un texto vacio")#informamos que ha ingresado un texto vacio
else:#en caso contrario que haya iingresado un texto
    print("El texto ingresado es: " + str(texto) + " En " + str(contador) + " Intentos")#informamos el texto que ha ingresado y el numero de intentos en los que se ha hecho










    






