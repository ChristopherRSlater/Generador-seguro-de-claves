import random
import hashlib
import tkinter as tk
from tkinter import messagebox

# Lista con tuplas (SE MANTIENE)
caracteres = [
    ("QWERTYUIOPLKJHGFDSAZXCVBNMÑ"),
    ("qwertyuiopasdfghjklzxcvbnmñ".lower()),
    ("*?><][{}]+=&%$#@!")
]

# ---------- FUNCION DE CIFRADO (AÑADIDA) ----------
def cifrar_clave(clave):
    return hashlib.sha256(clave.encode()).hexdigest()

# ---------- FUNCION PRINCIPAL ----------
def generar():
    nombre = entry_nombre.get()
    entrada = entry_cifrado.get().lower()

    if entrada == "si" or entrada == "no":

        longitud = int(entry_longitud.get())
        base = ""

        if var_mayus.get():
            base += caracteres[0]
        if var_minus.get():
            base += caracteres[1]
        if var_simbolos.get():
            base += caracteres[2]

        if base == "":
            messagebox.showerror("Error", "Seleccione al menos un tipo de caracter")
            return

        clave = ""
        for i in range(longitud):
            clave += random.choice(base)

        resultado = f"Su contraseña generada es:\n{clave}"

        # CIFRADO SOLO SI EL CLIENTE DICE "SI"
        if entrada == "si":
            clave_cifrada = cifrar_clave(clave)
            resultado += f"\n\nContraseña cifrada:\n{clave_cifrada}"

        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado)

# ---------- INTERFAZ GRAFICA (AÑADIDA) ----------
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("450x420")

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="¿Desea cifrar la contraseña? (si/no):").pack()
entry_cifrado = tk.Entry(ventana)
entry_cifrado.pack()

tk.Label(ventana, text="Longitud de la contraseña:").pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

var_mayus = tk.BooleanVar()
var_minus = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

tk.Checkbutton(ventana, text="Incluir mayúsculas", variable=var_mayus).pack()
tk.Checkbutton(ventana, text="Incluir minúsculas", variable=var_minus).pack()
tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos).pack()

tk.Button(ventana, text="Generar contraseña", command=generar).pack(pady=10)

text_resultado = tk.Text(ventana, height=10, width=50)
text_resultado.pack()

ventana.mainloop()
