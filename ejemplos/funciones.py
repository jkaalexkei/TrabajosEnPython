
#sintaxis de funciones

def mensaje():#declaracion de la funcion
    print("hola")#-> cuerpo de la funcion

mensaje()#lllamada de la funcion

#########################################
# PASO DE PARAMETROS A FUNCIONES

def suma(a,b):
    c = a + b
    return c #develve el resultado de la suma

print(suma(1,1))

var = suma(2,2)#le asignamos a una variable el valor que devuelve la funcion suma

print(var)

def funcion_suma(a,b):
    c = a+b
    return c

def funcion_multiplicar(a,b):
    c = a * b
    return c

print("operacion a realizar")
print("presione a para suma")
print("presione b para multiplicar")
val = input()

if val == "a":
    print("inigrese valor 1: "); val1 = int(input())
    print("inigrese valor 2: "); val2 = int(input())
    print("El resultado es: ", funcion_suma(val1,val2))
elif val == "b":
    print("inigrese valor 1: "); val1 = int(input())
    print("inigrese valor 2: "); val2 = int(input())
    print("El resultado es: ", funcion_multiplicar(val1,val2))
else:
    print("Operacion no especificada")






