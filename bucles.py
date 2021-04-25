lista = [1,2,3,4]
print(type(lista))

for milista in lista:
    print(milista)

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)

datos = {'nombre':'alex', 'apellido':'varela'}

for nom, ape in datos.items():
    print(nom, ' ', ape)


num = input("Ingresa Cedula: ")
while num =="":
    if num == "":
        print("campo vacio")
        num = input("Ingresa Cedula: ")
    else:
        print(num)
        break



    

    





