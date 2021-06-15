#uso del widget text para textos largos
#uso del widget button para construir botones que interactuen con la interfaz
#para asignar informacion a un cuadro de texto se usa la funcion set
#para obtener informacion de un cuadro de texto se usa la funcion get


from tkinter import *

raiz = Tk()

miframe = Frame()
miframe.pack()
minombre = StringVar()#esto indica que la variable es de tipo string o cadena de caracteres
etiquetaComentarios = Label(miframe,text="comentarios: ")
etiquetaComentarios.grid(row=0,column=0)

txtnombre = Entry(miframe,textvariable=minombre)
txtnombre.grid(row=2,column=1)

textocomentario= Text(miframe,width=16,height=5)
textocomentario.grid(row=0,column=1)

barradenavegacion = Scrollbar(miframe,command=textocomentario.yview)#aca se agrega o se asocia el scrollbars al textocomentario
barradenavegacion.grid(row=0,column=2,sticky="nsew")#colocando todas las letras para el posicionamiento la barra se adapta al textocomenmtario
textocomentario.config(yscrollcommand=barradenavegacion.set)

def funcionsaludo():
    minombre.set("ALEX")

boton = Button(raiz,text="Enviar",command=funcionsaludo)
boton.pack()





raiz.mainloop()