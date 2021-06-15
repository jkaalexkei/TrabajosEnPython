# #INTERFACES GRAFICAS

# from sys import unraisablehook


# libreria tkinter para trabajar con interfaces graficas en python

# denomidas GUI son intermediarios entreel programa y el usuario. formadas por un conjunto de graficos como ventanas, botones, menus, casillas de verificacion

# librerias tkinter,wxpython,pyqt,pygtk

# comando para instalar en linux sudo apt-get install python3-tk

# estructura de una ventana en  python

# 1.- construir la raiz --> ventana
# 2.- frame para aglutinar elementos los cuales se conocen como widgets

# para abrir un archivo de python en modo interfaz grafica al nombre del archivo al final de la extension se le agrega la letra w de la siguiente manera:    archivo.pyw

from tkinter import * #importamos la libreria tkinter
raiz = Tk()# --> creamos la raiz

#modficar caracteristicas de una ventana

raiz.title("ventana de prueba")#titulo a la ventana

raiz.resizable(0,1)#admite dos parametros (width,heigth) pero se trabaja 0 = false, 1 = true para poder redimensionar la ventana

raiz.iconbitmap("../../iconos/pc.ico")#agrega un icono a la ventana (se debe usar archivos con exxtension ico)

raiz.geometry("650x350")#cambiar el tamaño recibe argumentos de ancho y alto

raiz.config(bg="blue")#cambiar el color de la ventana

raiz.mainloop()#el metodo mainloop se utiliza como un bucle infinito para que este a la escucha de las acciones del usuario




