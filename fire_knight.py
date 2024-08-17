import tkinter as tk
from tkinter import messagebox
import random

# Simulación de almacenamiento de cuentas (10 slots)
cuentas = {}

def guardar_cuenta(usuario, contrasena):
    if len(cuentas) < 10:
        cuentas[usuario] = contrasena
        return True
    else:
        return False

def verificar_cuenta(usuario, contrasena):
    return cuentas.get(usuario) == contrasena

def iniciar_juego():
    ventana = tk.Tk()
    ventana.title("Fire Knight - Registro/Login")

    usuario = tk.StringVar()
    contrasena = tk.StringVar()

    tk.Label(ventana, text="Usuario").pack()
    tk.Entry(ventana, textvariable=usuario).pack()

    tk.Label(ventana, text="Contraseña").pack()
    tk.Entry(ventana, textvariable=contrasena, show="*").pack()

    def registrar():
        nombre_usuario = usuario.get()
        clave = contrasena.get()
        if guardar_cuenta(nombre_usuario, clave):
            messagebox.showinfo("Registro", "¡Cuenta registrada con éxito!")
        else:
            messagebox.showerror("Error", "No se pueden registrar más cuentas. Límite alcanzado.")

    def iniciar_sesion():
        nombre_usuario = usuario.get()
        clave = contrasena.get()
        if verificar_cuenta(nombre_usuario, clave):
            messagebox.showinfo("Bienvenido", f"¡Bienvenido {nombre_usuario}!")
            ventana.destroy()
            abrir_menu_inicio()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    tk.Button(ventana, text="Registrar", command=registrar).pack()
    tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion).pack()

    ventana.mainloop()

def abrir_menu_inicio():
    menu_ventana = tk.Tk()
    menu_ventana.title("Fire Knight")

    frases_version = ["beta", "1.2.2", "1.0.0", "Early Access", "Demo"]
    frase_actual = random.choice(frases_version)

    tk.Label(menu_ventana, text="Fire Knight", font=("Arial", 20)).pack(pady=10)
    tk.Label(menu_ventana, text=frase_actual, font=("Arial", 10)).pack(pady=5)
    
    opciones = ["Jugar", "Configuraciones", "Salir"]
    for opcion in opciones:
        tk.Button(menu_ventana, text=opcion, command=lambda o=opcion: seleccionar_opcion(o, menu_ventana)).pack(pady=5)

    menu_ventana.mainloop()

def seleccionar_opcion(opcion, ventana):
    if opcion == "Jugar":
        messagebox.showinfo("Información", "Funcionalidad no implementada aún.")
    elif opcion == "Configuraciones":
        messagebox.showinfo("Información", "Funcionalidad no implementada aún.")
    elif opcion == "Salir":
        ventana.destroy()

# Iniciar la aplicación
iniciar_juego()
