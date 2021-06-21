
# def palindromo(texto):
#     lista =[]
#     for i in texto:
#         lista.append(i)
#     print(lista)
#     lista_inversa = lista[::-1]#se invierte la lista
#     print(lista_inversa)
    
#     if lista == lista_inversa:
#         print("verdadero")
#     else:
#         print("Falso")   

# palindromo("nodeseoesedon")

def valores (*listado):
    return sum(listado)/len(listado)


total = valores(10,10,10)
print(total)

