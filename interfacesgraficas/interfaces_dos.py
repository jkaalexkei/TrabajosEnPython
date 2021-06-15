

from tkinter import *

raiz = Tk()

raiz.title("ventana de prueba")
#raiz.resizable(0,1)
raiz.iconbitmap("../../iconos/pc.ico")
raiz.geometry("650x350")
raiz.config(bg="blue")


frame = Frame()#creamos un frame y luego se debe empaquetar detro de la raiz

# frame.pack(side="left",anchor="n")#empaqueta un frame dentro de la raiz y puede recibiir varios parametros (ver documentacion) usando las propiedades side y anchor se posicionar el frame

# frame.pack(fill="x")#redimensiona un frame (ver documentacion para ver las otras propidades) fill="y" se debe usar con la propidad expand="True"
frame.pack()
frame.config(bg="green")#le da color al frame
#para darle tamaño a un frame se le debe quitar las dimensiones del tamaño a la raiz y darselas al frame en vista que la raiz se adapta al tamaño del frame o contenedor interno
frame.config(width="650",height="350")#esto le da tamaño al frame
frame.config(bd="30")#grueso del borde
frame.config(relief="sunken")#estilo del borde
frame.config(cursor="pirate")#cambia el tipo de cursor



raiz.mainloop()