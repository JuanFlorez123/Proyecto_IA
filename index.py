import numpy as np
import tkinter as tk
from tkinter import E, ttk

ventana = tk.Tk()
ventana.geometry("1000x900")
ventana.title("Algoritmos de búsqueda")

etiquetaSelect = tk.Label(ventana, text = "Selecciona el algoritmo de búsqueda que desees: ")
etiquetaSelect.place(x = 10, y= 20)
etiquetaSelect.configure(font=("Arial", 12, "italic"))

etiquetaTablero = tk.Label(ventana, text = "Tablero inicial - animación")
etiquetaTablero.place(x=20, y=80)

botonBNI = tk.Button(ventana, text = "NO INFORMADA", padx= 20, bg="blue")
botonBNI.place(x=380, y=10)
botonBNI.configure(font=("Courier", 16, "italic"))

botonBI = tk.Button(ventana, text = "INFORMADA", padx= 20, bg = "green")
botonBI.place(x=600, y=10)
botonBI.configure(font=("Courier", 16, "italic"))

combo = ttk.Combobox(ventana)
combo.place (x=800, y=10)

A = np.loadtxt('matriz.txt',dtype=int)
print(A)

interfaz = tk.Canvas(ventana)
interfaz.place (x=20, y=100)

for i in range(10):
    for j in range(10):
        print(i)
        print(j)
        if(i+j) % 2 == 0:
            interfaz.create_rectangle(i*30, j*30, (i+1)*30, (j+1)*30, fill = "#FFFFFF")
        else:
            interfaz.create_rectangle(i*30, j*30, (i+1)*30, (j+1)*30, fill = "#FF0000")

ventana.mainloop()