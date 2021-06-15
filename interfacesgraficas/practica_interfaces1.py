
from tkinter import *

raiz = Tk()

contenedor = Frame()
contenedor.pack()
#-----------------variables-------------------------------

numeroPantalla = StringVar()
#------------------Pantalla-----------------------

pantalla = Entry(contenedor,bg="black",foreground="white",font=("Arial Black",14),justify="right")
pantalla.grid(row=1,column=1,columnspan=4)

#------------------botones----------------------------

Boton0 = Button(contenedor,text="0",bg="blue",font=("Arial",14),width=4)
Boton0.grid(row=2,column=1,padx=3,pady=3)
Boton1 = Button(contenedor,text="1",bg="blue",font=("Arial",14),width=4)
Boton1.grid(row=2,column=2,padx=3,pady=3)
Boton2 = Button(contenedor,text="2",bg="blue",font=("Arial",14),width=4)
Boton2.grid(row=2,column=3,padx=3,pady=3)
Boton3 = Button(contenedor,text="3",bg="blue",font=("Arial",14),width=4)
Boton3.grid(row=2,column=4,padx=3,pady=3)

#-----------------------operaciones---------------------

Botonsuma = Button(contenedor,text="+",bg="blue",font=("Arial",14),width=4)
Botonsuma.grid(row=3,column=1,padx=3,pady=3)
Botonigual = Button(contenedor,text="=",bg="blue",font=("Arial",14),width=4)
Botonigual.grid(row=3,column=2,padx=3,pady=3)

#-------------------------------------------------------------



raiz.mainloop()