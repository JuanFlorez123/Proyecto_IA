import numpy as np
import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Algoritmos de búsqueda")

etiquetaSeleccion = tk.Label(ventana, text = "Seleccione el tipo de algoritmo de búsqueda a aplicar")
etiquetaSeleccion.pack(fill = tk.X)
etiquetaSeleccion.configure(font=("Arial", 12, "italic"))

botonBNI = tk.Button(ventana, text = "NO INFORMADA", pady = 10, bg="blue")
botonBNI.pack(fill = tk.X)
botonBNI.configure(font=("Courier", 16, "italic"))
botonBI = tk.Button(ventana, text = "INFORMADA", pady = 10, bg = "green")
botonBI.pack(fill = tk.X)
botonBI.configure(font=("Courier", 16, "italic"))

A = np.loadtxt('matriz.txt',dtype=int)
print(A)


ventana.mainloop()