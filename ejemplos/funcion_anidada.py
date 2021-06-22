def operacion(a,b,ope='resta'):

    def suma(a=a,b=b):
        return a + b


    def resta(a=a,b=b):
        return a - b
    

    if ope == 'suma':
        print("La suma es: " + str(suma(a,b)))
    elif ope == 'resta':
        print("La resta es: " + str(resta(a,b)))


operacion(10,40)