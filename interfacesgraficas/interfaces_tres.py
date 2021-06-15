
#USO DE LOS LABEL
#se usan para mostrar texto o imagenes
#tienen la finalidad mostrar texto, no se puede interactuar con el objeto (borrar,arrastrar,click,otros)
#sintaxis:
#variabletipolabel = ClaseLabel(contenedor al que pertenece,opciones adicionales)

from tkinter import * 

raiz = Tk()

miframe = Frame(raiz,width=500, height=400)
miframe.pack()

#label = Label(miframe,text="Hola esto es un Label: ")

#label.pack()#si se usa el metodo pack()la ventana se ajusta al texto en su lugar se debe usar el metodo place y darle dimensiones de (x y)
#label.place(x=100,y=200)

#para agregar una imagen al label antes de empaquetar el label se hace lo siguiente
miImagen = PhotoImage(file="service-3.png")#permite manipular imagenes
#forma abreviada de las dos lineas anteriores
Label(miframe,image=miImagen).place(x=100,y=200)
#Label(miframe,text="Hola esto es un Label: ",fg="red",font=("Comic Sans MS",18)).place(x=100,y=200)

raiz.mainloop()
