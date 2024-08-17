import tkinter as tk
from tkinter import messagebox
import random

from Game.survey import salir_del_juego

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
            abrir_encuesta()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    # Botones para registro e inicio de sesión
    tk.Button(ventana, text="Registrar", command=registrar).pack()
    tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion).pack()

    ventana.mainloop()

def abrir_encuesta():
    # Crear ventana de encuesta
    encuesta_ventana = tk.Tk()
    encuesta_ventana.title("Encuesta - Configuración del Mundo")

    # Variables para las opciones de la encuesta
    tamaño_mundo = tk.StringVar(value="Medio")
    dificultad = tk.StringVar(value="Media")
    colores = {
        "pasto": tk.StringVar(value="Verde"),
        "tierra": tk.StringVar(value="Café"),
        "piedra": tk.StringVar(value="Gris"),
        "cielo": tk.StringVar(value="Azul"),
        "nubes": tk.StringVar(value="Blanco")
    }

    # Preguntas de la encuesta
    tk.Label(encuesta_ventana, text="Tamaño del Mundo").pack()
    tk.OptionMenu(encuesta_ventana, tamaño_mundo, "Pequeño", "Medio", "Grande").pack()

    tk.Label(encuesta_ventana, text="Dificultad").pack()
    tk.OptionMenu(encuesta_ventana, dificultad, "Fácil", "Media", "Difícil").pack()

    tk.Label(encuesta_ventana, text="Color del Pasto").pack()
    tk.OptionMenu(encuesta_ventana, colores["pasto"], "Verde", "Amarillo", "Rojo").pack()

    tk.Label(encuesta_ventana, text="Color de la Tierra").pack()
    tk.OptionMenu(encuesta_ventana, colores["tierra"], "Café", "Gris", "Negro").pack()

    tk.Label(encuesta_ventana, text="Color de la Piedra").pack()
    tk.OptionMenu(encuesta_ventana, colores["piedra"], "Gris", "Blanco", "Negro").pack()

    tk.Label(encuesta_ventana, text="Color del Cielo").pack()
    tk.OptionMenu(encuesta_ventana, colores["cielo"], "Azul", "Naranja", "Rosa").pack()

    tk.Label(encuesta_ventana, text="Color de las Nubes").pack()
    tk.OptionMenu(encuesta_ventana, colores["nubes"], "Blanco", "Gris", "Negro").pack()

    def comenzar_juego():
        encuesta_ventana.destroy()
        abrir_ventana_juego(tamaño_mundo.get(), dificultad.get(), colores)

    tk.Button(encuesta_ventana, text="Comenzar Juego", command=comenzar_juego).pack(pady=10)

    encuesta_ventana.mainloop()

def abrir_ventana_juego(tamaño_mundo, dificultad, colores):
    # Crear ventana del juego
    juego_ventana = tk.Tk()
    juego_ventana.title("Fire Knight - Juego")

    # Establecer colores según la encuesta
    colores_texto = f"Pasto: {colores['pasto'].get()}, Tierra: {colores['tierra'].get()}, Piedra: {colores['piedra'].get()}, Cielo: {colores['cielo'].get()}, Nubes: {colores['nubes'].get()}"
    tk.Label(juego_ventana, text=f"Tamaño del Mundo: {tamaño_mundo}").pack()
    tk.Label(juego_ventana, text=f"Dificultad: {dificultad}").pack()
    tk.Label(juego_ventana, text=f"Colores - {colores_texto}").pack()

    # Crear un área para el movimiento (simulación simple)
    canvas = tk.Canvas(juego_ventana, width=800, height=600, bg=colores['cielo'].get())
    canvas.pack()

    # Crear un cuadrado representando al jugador
    jugador = canvas.create_rectangle(390, 290, 410, 310, fill="red")

    def mover_jugador(event):
        if event.keysym == 'w':
            canvas.move(jugador, 0, -10)
        elif event.keysym == 's':
            canvas.move(jugador, 0, 10)
        elif event.keysym == 'a':
            canvas.move(jugador, -10, 0)
        elif event.keysym == 'd':
            canvas.move(jugador, 10, 0)

    juego_ventana.bind("<KeyPress>", mover_jugador)

    juego_ventana.mainloop()

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

    # Botón
