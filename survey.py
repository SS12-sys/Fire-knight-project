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
    # Crear ventana de registro/inicio de sesión
    ventana = tk.Tk()
    ventana.title("Fire Knight - Registro/Login")

    # Variables de usuario y contraseña
    usuario = tk.StringVar()
    contrasena = tk.StringVar()

    # Etiquetas y entradas para registro/inicio de sesión
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

    # Botones para registro e inicio de sesión
    tk.Button(ventana, text="Registrar", command=registrar).pack()
    tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion).pack()

    ventana.mainloop()

def abrir_menu_inicio():
    # Crear nueva ventana para el menú de inicio
    menu_ventana = tk.Tk()
    menu_ventana.title("Fire Knight")

    # Frases aleatorias para la versión
    frases_version = ["beta", "1.2.2", "1.0.0", "Early Access", "Demo"]
    frase_actual = random.choice(frases_version)

    # Opciones del menú
    tk.Label(menu_ventana, text="Fire Knight", font=("Arial", 20)).pack(pady=10)
    tk.Label(menu_ventana, text=frase_actual, font=("Arial", 10)).pack(pady=5)
    
    opciones = ["Jugar", "Configuraciones", "Salir"]
    for opcion in opciones:
        tk.Button(menu_ventana, text=opcion, command=lambda o=opcion: seleccionar_opcion(o, menu_ventana)).pack(pady=5)

    menu_ventana.mainloop()

def seleccionar_opcion(opcion, ventana):
    if opcion == "Configuraciones":
        abrir_configuraciones()
    elif opcion == "Salir":
        salir_del_juego(ventana)
    else:
        print(f"Seleccionaste: {opcion}")

def abrir_configuraciones():
    # Crear nueva ventana para las configuraciones
    config_ventana = tk.Toplevel()
    config_ventana.title("Configuraciones")

    # Volumen
    tk.Label(config_ventana, text="Volumen").pack()
    volumen = tk.Scale(config_ventana, from_=0, to=100, orient="horizontal")
    volumen.set(50)  # Valor por defecto
    volumen.pack()

    # Configuración de gráficos
    tk.Label(config_ventana, text="Gráficos").pack()
    graficos = tk.StringVar(value="Medio")
    tk.OptionMenu(config_ventana, graficos, "Bajo", "Medio", "Alto").pack()

    # Modo de pantalla
    pantalla_completa = tk.BooleanVar()
    tk.Checkbutton(config_ventana, text="Pantalla completa", variable=pantalla_completa).pack()

    # Modificación de teclas (simulación simple)
    tk.Label(config_ventana, text="Modificar teclas").pack()
    tk.Label(config_ventana, text="Mover Arriba: W").pack()
    tk.Label(config_ventana, text="Mover Abajo: S").pack()
    tk.Label(config_ventana, text="Mover Izquierda: A").pack()
    tk.Label(config_ventana, text="Mover Derecha: D").pack()

    # Botón para aplicar cambios y cerrar
    tk.Button(config_ventana, text="Aplicar", command=config_ventana.destroy).pack(pady=10)

def salir_del_juego(ventana):
    if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir del juego?"):
        ventana.destroy()

# Iniciar la aplicación
iniciar_juego()
