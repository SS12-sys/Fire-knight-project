import tkinter as tk
from tkinter import messagebox
import random
import subprocess

# Simulación de almacenamiento de cuentas (10 slots)
cuentas = {}

# Variables globales para configuraciones
config = {
    "volumen": 50,
    "pantalla_completa": False,
    "teclas": {
        "saltar": "space",
        "abrir_inventario": "i",
        "atacar": "a",
        "poner_bloque": "b",
        "quitar_bloque": "q",
        "mover_izquierda": "a",
        "mover_derecha": "d",
        "mover_arriba": "w",
        "mover_abajo": "s"
    }
}

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

    # Asegúrate de que frases_version no esté vacío
    if frases_version:
        frase_actual = random.choice(frases_version)
    else:
        frase_actual = "Desconocido"

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
        ventana.destroy()
        abrir_ventana_configuracion()
    elif opcion == "Salir":
        ventana.destroy()

def abrir_ventana_configuracion():
    config_ventana = tk.Tk()
    config_ventana.title("Configuración")

    def guardar_configuracion():
        try:
            config["volumen"] = volumen_var.get()
            config["pantalla_completa"] = pantalla_completa_var.get()
            config["teclas"]["saltar"] = tecla_saltar_var.get()
            config["teclas"]["abrir_inventario"] = tecla_abrir_inventario_var.get()
            config["teclas"]["atacar"] = tecla_atacar_var.get()
            config["teclas"]["poner_bloque"] = tecla_poner_bloque_var.get()
            config["teclas"]["quitar_bloque"] = tecla_quitar_bloque_var.get()
            config["teclas"]["mover_izquierda"] = tecla_mover_izquierda_var.get()
            config["teclas"]["mover_derecha"] = tecla_mover_derecha_var.get()
            config["teclas"]["mover_arriba"] = tecla_mover_arriba_var.get()
            config["teclas"]["mover_abajo"] = tecla_mover_abajo_var.get()
            messagebox.showinfo("Configuración", "Configuraciones guardadas con éxito!")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la configuración: {e}")

    def volver_al_menu():
        config_ventana.destroy()
        abrir_menu_inicio()

    # Volumen
    tk.Label(config_ventana, text="Volumen").pack(pady=5)
    volumen_var = tk.IntVar(value=config["volumen"])
    tk.Scale(config_ventana, from_=0, to=100, orient="horizontal", variable=volumen_var).pack(pady=5)

    # Pantalla Completa
    tk.Label(config_ventana, text="Pantalla Completa").pack(pady=5)
    pantalla_completa_var = tk.BooleanVar(value=config["pantalla_completa"])
    tk.Checkbutton(config_ventana, variable=pantalla_completa_var, text="Activar Pantalla Completa").pack(pady=5)

    # Teclas de Control
    tk.Label(config_ventana, text="Teclas de Control").pack(pady=10)
    
    def crear_control(texto, variable):
        tk.Label(config_ventana, text=texto).pack(pady=2)
        tk.Entry(config_ventana, textvariable=variable).pack(pady=2)

    tecla_saltar_var = tk.StringVar(value=config["teclas"]["saltar"])
    tecla_abrir_inventario_var = tk.StringVar(value=config["teclas"]["abrir_inventario"])
    tecla_atacar_var = tk.StringVar(value=config["teclas"]["atacar"])
    tecla_poner_bloque_var = tk.StringVar(value=config["teclas"]["poner_bloque"])
    tecla_quitar_bloque_var = tk.StringVar(value=config["teclas"]["quitar_bloque"])
    tecla_mover_izquierda_var = tk.StringVar(value=config["teclas"]["mover_izquierda"])
    tecla_mover_derecha_var = tk.StringVar(value=config["teclas"]["mover_derecha"])
    tecla_mover_arriba_var = tk.StringVar(value=config["teclas"]["mover_arriba"])
    tecla_mover_abajo_var = tk.StringVar(value=config["teclas"]["mover_abajo"])

    crear_control("Saltar", tecla_saltar_var)
    crear_control("Abrir Inventario", tecla_abrir_inventario_var)
    crear_control("Atacar", tecla_atacar_var)
    crear_control("Poner Bloque", tecla_poner_bloque_var)
    crear_control("Quitar Bloque", tecla_quitar_bloque_var)
    crear_control("Mover Izquierda", tecla_mover_izquierda_var)
    crear_control("Mover Derecha", tecla_mover_derecha_var)
    crear_control("Mover Arriba", tecla_mover_arriba_var)
    crear_control("Mover Abajo", tecla_mover_abajo_var)

    tk.Button(config_ventana, text="Guardar Configuración", command=guardar_configuracion).pack(pady=10)
    tk.Button(config_ventana, text="Volver al Menú", command=volver_al_menu).pack(pady=10)

    config_ventana.mainloop()

# Iniciar la aplicación
iniciar_juego()
