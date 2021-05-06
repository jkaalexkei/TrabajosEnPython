
#Ejercicio N° 1: Enunciado
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

dinerodepositado = input("Ingrese el dinero a depositar: ")

dinero = round(float(dinerodepositado),2)

cant_agno = 3

interesagno = 0.04


totalahorrado = (float(dinero) + (interesagno * int(cant_agno)))

print("Total interes por año 4%")
print(f"El total ahorrado es: {round(totalahorrado,2)}")


#Ejercicio N° 2:
#Segundo ejercicio para "Cadenas"
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


nombre_prod = input("Ingrese Nombre del Producto: ")
precio_prod = float(input("Ingrese Precio del Producto: "))

numero_und_prod = input("Ingrese numero de unidades: ")

precio_total = float(precio_prod) * int(numero_und_prod)

print(f"""Nombre del Producto: {nombre_prod}
          Precio del Producto: {str(round(precio_prod,2))}
          Cantidad del producto: {numero_und_prod}
          Precio Total: {str(round(precio_total,2))}""")


# tercer ejercicio: 

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.



pizzaVegetariana = ["Pimiento","Tofu","Mozarella","tomate"]
pizzaNoVegetariana = ["Peperoni","Jamón","Salmón","Mozarella","tomate"]

print("""Introduzca la Letra correspondiente a su elección:
    A Para Pizza Vegetariana
    B Para Pizza No Vegetariana""")

tipoPizza = input("¿Que tipo de pizza desea?: ").lower()

contador = 1

while tipoPizza == "":

    print("No se registro una elección, Intente de Nuevo")
    tipoPizza = input("¿Que tipo de pizza desea?: ").lower()

    if contador >= 3:
        print("Muchos Intentos")
        break
    else:
        contador += 1


if tipoPizza == "a":
    print("La pizza elegida es Vegetariana, sus Ingredientes son:")

    for i in pizzaVegetariana:
        print(i,end=" ")

    adicional=input("¿Desea Agregar un ingrediente adicional? introduzca si o no: ").lower()

    if adicional == "si":
        ing_adicional = input("¿Que ingrediente adicional desea?: ")
        pizzaVegetariana.append(ing_adicional)
        print("Su orden final es: ")
        print("Pizza Vegetariana con: ")

        for a in pizzaVegetariana:
            print(a,end=" ")
        
        print("Fin del pedido")
        print("disfrute la pizza!!")

    elif adicional == "no":
        print("Su orden final es: ")
        print("Pizza Vegetariana con: ")
        for b in pizzaVegetariana:
            print(b,end=" ")
        
        print("Fin del pedido")
        print("disfrute la pizza!!")
    else:
        print("fin del pedido")
    
elif tipoPizza == "b":
    print("La pizza elegida es No Vegetariana, sus ingredientes son:")
    for j in pizzaNoVegetariana:
        print(j, end=" ")
    
    adicional=input("¿Desea Agregar un ingrediente adicional? introduzca si o no: ").lower()

    if adicional == "si":
        ing_adicional = input("¿Que ingrediente adicional desea?: ")
        pizzaNoVegetariana.append(ing_adicional)
        print("Su orden final es: ")
        print("Pizza No Vegetariana con: ")

        for a in pizzaNoVegetariana:
            print(a,end=" ")
        
        print("Fin del pedido")
        print("disfrute la pizza!!")

    elif adicional == "no":
        print("Su orden final es: ")
        print("Pizza No Vegetariana con: ")
        for b in pizzaNoVegetariana:
            print(b,end=" ")
        print("Fin del pedido")
        print("disfrute la pizza!!")
    else:
        print("fin del pedido")
else:
    print("Ese tipo de pizza no esta en el Menú del día")





















