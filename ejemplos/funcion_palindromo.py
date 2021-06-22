
def palindromo(texto):
    lista =[]
    for i in texto:
        lista.append(i)
    print(lista)
    lista_inversa = lista[::-1]#se invierte la lista
    print(lista_inversa)
    
    if lista == lista_inversa:
        print("verdadero, si es palindromo")
    else:
        print("Falso, no es palindromo")   

palindromo("alex")


