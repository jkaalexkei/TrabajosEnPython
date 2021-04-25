
# valor1 = 1000
# valor2 = -7
# valor3 = 3000

# if 0 < valor2 < 100:#aca se evaluan dos condiciones a la vez (operadores de comparacion concatenados)
#     print ("todo anda bien")
# else:
#     print("los datos no se corresponde")

# #CONDICIONALES Y OPERADORES DE COMPARACION

# edad = 37
# print ("edad: " + str(edad))#para concatenar un string con un dato de tipo entero se debe convertir a un string para poder concatenar

# #****CONDICIONAL CON OPERADOR DE COMPARACION AND Y OR

# #and ---> y si no
# #or ----> o si no

# #CONDICIONALES
# #distancia > 40kmk
# # numeros hermanos > 2
# # sueldo familiar <= 20000

# print("Programa de becas")

# distancia = int(input("Introduce la distancia a la escuela en Km: "))
# print(distancia)
# nro_hnos = int(input("numero de hermanos: "))
# print(nro_hnos)
# sueldo = int(input("ingrese salario: "))
# print(sueldo)

# if distancia > 40 and nro_hnos > 2 or sueldo <= 20000:#uso del operador and para evaluar tres condiciones (esta manera de comparar necesita que se cumplan todas las condiciones)
#     print("tienes derecho a beca")
# else:
#     print("no tienes derecho a beca")

#USO OPERADOR in

print("Ingrese la asignatura elegida")
asignatura = input("Asignaturas disponibles: Castellano, Ingles: ").lower()#SE CONVIERTE A MINISCULAS LO QUE INGRESA EL USUARIO

if asignatura in ("castellano","ingles"):
    print("La asignatura seleccionada es: " + asignatura)
else:
    print("la asgnatura no existe")




