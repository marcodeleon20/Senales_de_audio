#Librerías para interfaz
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

#Funcion para abrir archivo
def abrirArchivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
    if file_path:
        label.configure(text = "Archivo selecionado: " + file_path)

#Iniciando Interfaz para lectura
root = tk.Tk()
root.title("Prueba de leer archivos")

#Redimensionar
root.geometry("800x500")

#Color
root.configure(background= "yellow")

#Combobox

combo = ttk.Combobox(root, values=["filtro1", "filtro2", "filtro3", "filtro4"])
combo.place(x = 10, y=100)



#Boton para cargar archivo
boton = tk.Button(root, text = "Cargar Archivo", command= abrirArchivo)
boton.place(x=10, y=10)
#boton.pack(side = "right")

#Label para colocar nombre o ruta del archivo
label = tk.Label(root, text= "Este fue tu archivo: ")
label.place(x = 10, y = 50)
#label.pack(pady = 12)

root.mainloop()




