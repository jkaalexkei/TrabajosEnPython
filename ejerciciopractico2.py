# milista = [1,2,3,4]
# dato = int(input("ingrese el numero a indagar: "))

# if dato in milista:
#     print("El numero se encuentra en la posicion: " + str(milista.index(dato)))
# else:
#     print("el numero no esta en la lista")
 
# user = "usuario"
# clave =1234

# usuario = input("Ingrese usuario: ").lower()
# password = int(input("Ingrese clave: "))

# if user == usuario and clave == password:
#      print("Acceso permitido")
# else:
#     print("Acceso denegado, Intente de nuevo")
    
valida = False

email = input("Ingresa su email: ")

for i in range(len(email)):
    if email[i] == "@":
        valida = True

if valida == True:
    print("Email Correcto")
else:
    print("Email Incorrecto")
        



