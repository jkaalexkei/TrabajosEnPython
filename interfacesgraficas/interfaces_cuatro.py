#uso del widget entry para ingresar textos
#usa las mismas propiedades de los label
#para cambiar los atributos de un elemento se utiliza el metodo config

from tkinter import *

raiz = Tk()
miframe= Frame(raiz,width=1200,height=600)
miframe.pack()
cuadrotexto = Entry(miframe)

cuadrotexto.grid(row=0,column=1)#metodo grid(row,column) se empleoa para posicionar los elementos en un frame

cuadrotexto2 = Entry(miframe)

cuadrotexto2.grid(row=1,column=1)
cuadrotexto2.config(show="*")#la propiedad show del metodo config oculta la informacion para el caso de un password

nombreLabel = Label(miframe,text="nombre: ")#al construir un elemento se debe agregar al frame o contenedor al que pertenece
nombreLabel.grid(row=0,column=0,sticky="w")
#metodo sticky se usa para alinear los elementos, usa los puntos cardinales para la alineacion del texto(n,s,e,w, ne,nw,se,sw). este metodo se pasa como tercer argumento en el metodo grid
apellidoLabel = Label(miframe,text="direccion de residencia: ")
apellidoLabel.grid(row=1,column=0,sticky="e")


raiz.mainloop()