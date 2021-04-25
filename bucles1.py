#tpos de bucles

# determinados: ejecutan un numero determinado de veces se sabe cuantas veces se va a ejecutar el codigo del interior del bucle

# indeterminados
# se ejecutan un numero indeterminado de veces, no se sabe cantas veces se va a ejecutar, el numero de veces que se va a ejecutar dependera de las circunstancias durante la ejecucion del programa.

# sintaxis

#partes del bucle:

#declaracion del bucle:
    # cuerpo del bucle

#BUCLES DETERMINADOS

#sintaxis
#for variable in elemento a recorrer:
    # cuerpo del bucle

# el elemento a recorrer puede ser una lista, tupla, diccionario, otro

for i in [1,2,3]:#declaracion del bucles
     print(i)#cuerpo del bucle

#RECORRIENDO STRING
for i in ["curso","python"]:#La variable i va tomando a cada vuelta del bucle el valor de los elementos
    print("hola", end=' ')#el argumento end va especificar la salida de lo que vamos a mostrar es decir sin salto de lineas


email = False
mi_email = input("Ingrese su correo")
for i in mi_email:#recorre tantas veces como caracteres haya en el string
    if (i == "@") or (i =="."):
        email=True

if email == True:
    print("email correcto")
else:
    print("email no correcto")

mi_lista = [1,2,3]
print(type(mi_lista))

mi_lista.append(4)
print(mi_lista)




    


#TIPO RANGE
#NOTACIONES ESPECIALES CON PRINT







