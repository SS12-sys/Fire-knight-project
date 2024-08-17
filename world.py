import tkinter as tk

def iniciar_mundo(tamaño_mundo, dificultad, colores):
    # Crear ventana del juego
    juego_ventana = tk.Tk()
    juego_ventana.title("Fire Knight - Mundo")

    # Configurar el tamaño del mundo
    tamaño_mapas = {
        "Pequeño": (400, 300),
        "Medio": (800, 600),
        "Grande": (1200, 900)
    }
    tamaño = tamaño_mapas.get(tamaño_mundo, (800, 600))
    canvas = tk.Canvas(juego_ventana, width=tamaño[0], height=tamaño[1], bg=colores['cielo'])
    canvas.pack()

    # Dibujar el mundo
    canvas.create_rectangle(0, 0, tamaño[0], tamaño[1], fill=colores['tierra'])

    # Crear un área para el movimiento (simulación simple)
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

    # Configuración del texto del mundo
    tk.Label(juego_ventana, text=f"Tamaño del Mundo: {tamaño_mundo}", font=("Arial", 16)).pack()
    tk.Label(juego_ventana, text=f"Dificultad: {dificultad}", font=("Arial", 16)).pack()
    tk.Label(juego_ventana, text=f"Colores - Pasto: {colores['pasto']}, Tierra: {colores['tierra']}, Piedra: {colores['piedra']}, Cielo: {colores['cielo']}, Nubes: {colores['nubes']}", font=("Arial", 16)).pack()

    juego_ventana.mainloop()
