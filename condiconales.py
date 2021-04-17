#estructuras de control de flujo

#condicional IF

#Operadores de comparacion
# mayor que >
# menor que <
# igual que ==
# mayor e igual que >=
# menor e igual que <=
# diferente que !=

def evaluacion(nota):#creamos una funcion 
    valoracion = "aprobado"
    if nota < 5:#condicional if
        valoracion = "reprobrado"
    return valoracion

print(evaluacion(6))

x= list(range(1,8,3))
res = x[-1] + x[1]
print(x)

# clave = input("Igrese la clave: ")

# valores_diccionario = {"clave":"1234"}


# def validacion_clave(valores,password):
#     if valores["clave"] == password:
#         # print(type(valores))
#         print("acceso concedido")
#     else:
#         print("acceso denegado")


# validacion_clave(valores_diccionario,clave)

#----------------------------------------------
# nota = int(input("Ingresa la nota: "))

# if nota < 5:
#     print("aplazado")
# elif nota > 6:
#     print("bien")
# elif nota > 10:
#     print("sobresaliente")
# else:
#     print(" No es una nota")

#----CALCULO DEL NUMERO MAS ALTO DE DOS NUMEROS

# num1 = int(input("Ingrese Numero 1: "))
# num2 = int(input("Ingrese Numero 2: "))

# def NumeroAlto(a,b):
#     if a < b:
#         print(f"El numero {b} es mas alto que {a}")
#     elif a > b:
#         print(f"El numero {a} es mas alto que {b}")
#     else:
#         print("los numeros son iguales")

# NumeroAlto(num1,num2)

# nombre = input("Ingresa nombre: ")
# apellido = input("ingresa apellido: ")
# direccion = input("ingresa direccion: ")

# lista = [nombre,apellido,direccion]
# print(type(lista))
# print(f"su nombre es: {lista[0]}, su apellido es: {lista[1]}, su direccion es: {lista[2]}")


num = int(input("ingresa numeros: "))
contador = 1
resul = 0

while contador <= num:
    valor = int(input(f"valor {contador}: "))
    resul = (resul + valor)
    contador+=1

print("el promedio es: ", float(resul/num))
















