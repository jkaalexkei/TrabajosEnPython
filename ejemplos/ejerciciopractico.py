# valores = [1,2,3,4,5,6]

# for val in valores:
#     print(val)

# for i in range(10,20):
#     print(i)


# def miFuncion():
#     miLista = ["a","b","c","d"]
#     print(miLista)


# print(miFuncion())

# d = miFuncion()




# print(type(1/2))

cont = 1
res = 0

nros_a_sumar = int(input("Ingrese Numeros: "))
while cont <= nros_a_sumar:
    valor = int(input(f"Ingrese valor {cont}"))
    res = res + valor
    cont+=1

print("el resultado es: " + str(res))

