
from tkinter import *

import parser #importamos la libreria parser para el manejo de expresiones

raiz = Tk()
contenedor = Frame()
contenedor.pack()

nombre1 = StringVar()
nombre2 = StringVar()
numeroPantalla = StringVar(value="0")


cajadetexto2 = Entry(contenedor,textvariable=numeroPantalla,width=50,font=("Arial Black",14),bg="Black",foreground="white", justify="right")
cajadetexto2.grid(row=0,column=0,columnspan=4)

i = 0 #declaramos una variable de uso global para el manejo de los indices de los strings
def numeroPulsado(n):#con esta funcion agregamos los numeros a la pantalla
    
    global i #usamos la variable global i para trabajar con los indices de los strings
    if numeroPantalla.get() == "0":#validamos si hay un cero en la pantalla
        
        numeroPantalla.set(numeroPantalla.get()[:-1])#en caso de haber un cero en pantalla lo reemplazamos por el nuevo numero
        
    else:
        cajadetexto2.insert(i,n)#concatenamos los numeros que se van introduciendo uno a uno
        i+=1#iincrementamos el indice por cada vez que se presione el boton de algun número

def numeroCero(n):#con esta funcion validamos el cero a la izquierda
    global i
    if numeroPantalla.get() == "0":#validamos que en la pantalla haya un cero
        numeroPantalla.set("0")#asignamos cero solamente para que no aparezcan ceros a la izquierda
    else:
        
        cajadetexto2.insert(i,n)#en caso contrario que exista un numero diferente a cero, el cero se va concatenando a la derecha del numero 
        i+=1


def operacion(operador):#funcion para evaluar el operador matematico ingresado
    global i

    if numeroPantalla.get() == "0":#en caso de existir un cero en pantalla
        limpiarPantalla()#llamamos a la funcion limpiar pantalla
        
    else:#en caso contrario
        ope = operador#a la variable ope le asignamos lo que viene en el paramentro operador
        cajadetexto2.insert(i,ope)#aca vamos agregando los numeros a la pantalla de manera consecutiva
        i+=1


def totalizar():#funcion para realizar el calculo de las operaciones

    valor = numeroPantalla.get()#a la variable valor le asignamos lo que tiene la pantalla
    try:#intenta
        total = parser.expr(valor).compile()#a la variable total le asignamos la expresion obtenida
        resultado = eval(total)#en la variable resultado almacenamos el resultado generado por la evaluacion de la expresion
        limpiarPantalla()#limpiamos la pantalla
        cajadetexto2.insert(0,resultado)#en la posicion cero de la pantalla asignamos o mostramos el nuevo valor
    except:#en caso de producirse una excepcion limpiamos la pantalla
        limpiarPantalla()


def limpiarPantalla():
    cajadetexto2.delete(0,END)#instruccion para borrar pantalla


def retroceder():
    global i
    expresion = numeroPantalla.get()#en la variable expresion guardamos lo que exista en la pantalla
    if len(expresion) > 0:#comprobamos que se haya ingresado un dato en pantalla
        nuevaexpresion = expresion[:-1]#con esta linea eliminamos uno a uno los numeros en pantalla
        numeroPantalla.set(nuevaexpresion)#le asignamos el nuevo valor a la pantalla
    elif len(expresion) == 0:#y si la expresion es igual o llega a cero simplemente le asignamos a la pantalla el cero
        numeroPantalla.set("0")
    else:
        numeroPantalla.set("0")


botonlimpiar = Button(contenedor,text="C",command=lambda:limpiarPantalla(),width=3,height=3,font=("Arial Black",13),bg="#1D2869",foreground="yellow")
botonlimpiar.grid(row=1,column=2, sticky="we",padx=4,pady=4)
botonretroceder = Button(contenedor,text="<--",command=lambda:retroceder(),width=3,height=3,font=("Arial Black",13),bg="#1D2869",foreground="yellow")
botonretroceder.grid(row=1,column=3, sticky="we",padx=4,pady=4)  

botonparentesis_a = Button(contenedor,text="(",command=lambda:operacion("("),width=3,height=3,font=("Arial Black",13),bg="#1D2869",foreground="yellow")
botonparentesis_a.grid(row=1,column=0, sticky="we",padx=4,pady=4)
botonparentesis_c = Button(contenedor,text=")",command=lambda:operacion(")"),width=3,height=3,font=("Arial Black",13),bg="#1D2869",foreground="yellow")
botonparentesis_c.grid(row=1,column=1, sticky="we",padx=4,pady=4)    
   


boton1 = Button(contenedor,text="1",command=lambda:numeroPulsado("1"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton1.grid(row=2,column=0,sticky="we",padx=4,pady=4)
boton2 = Button(contenedor,text="2",command=lambda:numeroPulsado("2"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton2.grid(row=2,column=1,sticky="we",padx=4,pady=4)
boton3 = Button(contenedor,text="3",command=lambda:numeroPulsado("3"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton3.grid(row=2,column=2,sticky="we",padx=4,pady=4)
#------------------SUMA-------------------------
botonsuma = Button(contenedor,text="+",command=lambda:operacion("+"),width=3,height=3,font=("Arial Black",13),bg="#281EF5",foreground="yellow")
botonsuma.grid(row=2,column=3,sticky="we",padx=4,pady=4)
#---------------------------------------

boton4 = Button(contenedor,text="4",command=lambda:numeroPulsado("4"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton4.grid(row=3,column=0,sticky="we",padx=4,pady=4)
boton5 = Button(contenedor,text="5",command=lambda:numeroPulsado("5"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton5.grid(row=3,column=1,sticky="we",padx=4,pady=4)
boton6 = Button(contenedor,text="6",command=lambda:numeroPulsado("6"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton6.grid(row=3,column=2,sticky="we",padx=4,pady=4)

#------------------RESTA-------------------------
botonresta = Button(contenedor,text="-",command=lambda:operacion("-"),width=3,height=3,font=("Arial Black",13),bg="#281EF5",foreground="yellow")
botonresta.grid(row=3,column=3,sticky="we",padx=4,pady=4)
#---------------------------------------

boton7 = Button(contenedor,text="7",command=lambda:numeroPulsado("7"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton7.grid(row=4,column=0,sticky="we",padx=4,pady=4)
boton8 = Button(contenedor,text="8",command=lambda:numeroPulsado("8"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton8.grid(row=4,column=1,sticky="we",padx=4,pady=4)
boton9 = Button(contenedor,text="9",command=lambda:numeroPulsado("9"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
boton9.grid(row=4,column=2,sticky="we",padx=4,pady=4)

#------------------MULTIPLICACION-------------------------
botonmultiplicar = Button(contenedor,text="*",command=lambda:operacion("*"),width=3,height=3,font=("Arial Black",13),bg="#281EF5",foreground="yellow")
botonmultiplicar.grid(row=4,column=3,sticky="we",padx=4,pady=4)
#---------------------------------------------------
#------------------IGUAL-------------------------
botonigual = Button(contenedor,text="=",command=lambda:totalizar(),width=3,height=3,font=("Arial Black",13),bg="#281EF5",foreground="yellow")
botonigual.grid(row=5,column=0,sticky="we",padx=4,pady=4)
#---------------------------------------
botoncero = Button(contenedor,text="0",command=lambda:numeroCero("0"),width=3,height=3,font=("Arial Black",12),bg="#281EF5",foreground="yellow")
botoncero.grid(row=5,column=1,sticky="we")
#------------------MODULO-------------------------
botonmodulo = Button(contenedor,text="%",command=lambda:operacion("%"),width=3,height=3,font=("Arial Black",13),bg="#281EF5",foreground="yellow")
botonmodulo.grid(row=5,column=2,sticky="we",padx=4,pady=4)
#---------------------------------------
#------------------DIVISION-------------------------
botondivision = Button(contenedor,text="/",command=lambda:operacion("/"),width=3,height=3,font=("Arial Black",13),bg="#281EF5",foreground="yellow")
botondivision.grid(row=5,column=3,sticky="we",padx=4,pady=4)
#---------------------------------------






raiz.mainloop()