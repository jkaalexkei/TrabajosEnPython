from tkinter import *   


raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("calc.ico")
#------CONTENEDOR PRINCIPAL------------------------------------

contenedor = Frame(raiz,bg="#E5E8E8")
contenedor.pack()

#-----Variable global para almacenar la operacion a realizar
operacion = "" #esta variable se usa para almacenar la operacion a realizar
resultado = 0 #esta variable se usa para ir almacenando los valores que se van almacenando o procesando segun la funcion a realizar

numeroPantalla = StringVar()#esta variable almacena el valor que haya en la pantalla de la calculadora


#------DISEÑO DE LA PANTALLA-------------------------------------

pantalla = Entry(contenedor, textvariable=numeroPantalla, font=("Arial Black",14),bg="#2C3E50",foreground="#FDFEFE",justify="right")
pantalla.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

#---Funcion para ingresar texto en pantalla------------

def numeroPulsado(num):#funcion que procesa el numero que se va pulsando mediante los botones de la calculadora
    global operacion#uso de la variable global para emplear la operacion a realizar



    if operacion != "": #si la operacion es vacio 
        numeroPantalla.set(num)#a la variable numeroPantalla se le asigna el numero pulsado
        operacion=""#se vuelve asignar vacio para almacenar un nuevo valor y concatene los nuevos valores
    
    else:#en caso contrario
        numeroPantalla.set(numeroPantalla.get() + num)#usamos el metodo get para verificar lo que haya en pantalla y se concatena con el valor que se quiere agregar mediante el uso del metodo set

#-------Funcion para la operacion suma

def suma(num):
    global operacion#se usa la palabra reservada global para trabajar con una variable de ambito global
    global resultado

    resultado += int(num)
    operacion = "suma"

    numeroPantalla.set(resultado)
#-----


#----------fila 1--------------------

boton7 = Button(contenedor,text="7",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("7"))
boton7.grid(row=1,column=0)

boton8 = Button(contenedor,text="8",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("8"))
boton8.grid(row=1,column=1)

boton9 = Button(contenedor,text="9",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("9"))
boton9.grid(row=1,column=2)

botondividir = Button(contenedor,text="/",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("4"))
botondividir.grid(row=1,column=3)

#--------FILA 2----------------------------------------

boton4 = Button(contenedor,text="4",font=("Arial Black",12),width=5, command=lambda:numeroPulsado("4"))#funcion lambda funcion anonima para evitar que la funcion se ejecute de manera automatica
boton4.grid(row=2,column=0)

boton5 = Button(contenedor,text="5",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("5"))
boton5.grid(row=2,column=1)

boton6  = Button(contenedor,text="5",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("6"))
boton6.grid(row=2,column=2)

botonmultiplicar = Button(contenedor,text="x",font=("Arial Black",12),width=5)
botonmultiplicar.grid(row=2,column=3)

#-----------fila 3 ------------------------------------

boton1 = Button(contenedor,text="1",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("1"))
boton1.grid(row=3,column=0)

boton2 = Button(contenedor,text="2",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("2"))
boton2.grid(row=3,column=1)

boton3  = Button(contenedor,text="3",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("3"))
boton3.grid(row=3,column=2)

botonrestar = Button(contenedor,text="-",font=("Arial Black",12),width=5)
botonrestar.grid(row=3,column=3)

#-----------fila 4 ------------------------------------

boton0 = Button(contenedor,text="0",font=("Arial Black",12),width=5,command=lambda:numeroPulsado("0"))
boton0.grid(row=4,column=0)

botoncoma = Button(contenedor,text=",",font=("Arial Black",12),width=5,command=lambda:numeroPulsado(","))
botoncoma.grid(row=4,column=1)

botonigual  = Button(contenedor,text="=",font=("Arial Black",12),width=5)
botonigual.grid(row=4,column=2)

botonsumar = Button(contenedor,text="+",font=("Arial Black",12),width=5,command=lambda:suma(numeroPantalla.get()))
botonsumar.grid(row=4,column=3)



raiz.mainloop()

