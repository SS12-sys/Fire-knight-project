import pygame
import sys
import time

pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fire Knight')

# Colores
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)

# Fuentes
font = pygame.font.Font(None, 36)
loading_font = pygame.font.Font(None, 48)
input_font = pygame.font.Font(None, 28)

# Música
music_path = 'music.mp3'
try:
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen aquí
    pygame.mixer.music.play(-1)  # Reproduce música en bucle
    print(f"Música cargada y reproduciendo desde {music_path}")
except pygame.error as e:
    print(f"No se pudo cargar la música. Error: {e}")

# Definición de botones
buttons = {
    'Multijugador': pygame.Rect(50, 50, 200, 50),
    'Crear Mundo': pygame.Rect(50, 120, 200, 50),
    'Configuración': pygame.Rect(50, 190, 200, 50),
    'Tienda': pygame.Rect(50, 260, 200, 50),
    'Vestimenta': pygame.Rect(50, 330, 200, 50),
    'Jugar': pygame.Rect(50, 400, 200, 50)  # Botón para iniciar el juego
}

# Variables globales
input_text = ""
active_menu = None
game_running = False
player_name = "Nombre del Jugador"
name_rect = pygame.Rect(10, 10, 200, 30)  # Rectángulo para el nombre del jugador
name_speed = 5  # Velocidad del movimiento del nombre
direction = 1  # Dirección del movimiento del nombre (1: derecha, -1: izquierda)
player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)  # Rectángulo para el jugador
cat_dialog_visible = False
world_size = None  # Tamaño del mundo
world_name = ""

# Definición del botón de salir
exit_button = pygame.Rect(WIDTH - 100, HEIGHT - 50, 90, 40)

def draw_loading_screen(progress):
    screen.fill(BLUE)
    # Barra de carga
    pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50))
    pygame.draw.rect(screen, GREEN, (WIDTH // 4, HEIGHT // 2, (WIDTH // 2) * progress, 50))
    
    # Texto superior
    title_text = loading_font.render('Cargando Juego', True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
    
    # Texto de progreso
    progress_text = font.render(f'{int(progress * 100)}%', True, WHITE)
    screen.blit(progress_text, (WIDTH // 2 - progress_text.get_width() // 2, HEIGHT // 2 + 60))
    
    pygame.display.flip()

def draw_menu():
    screen.fill(BLUE)
    for name, rect in buttons.items():
        pygame.draw.rect(screen, WHITE, rect)
        text = font.render(name, True, BLUE)
        screen.blit(text, (rect.x + 10, rect.y + 10))
    pygame.draw.rect(screen, WHITE, exit_button)
    text = font.render('Salir', True, BLUE)
    screen.blit(text, (exit_button.x + 10, exit_button.y + 10))
    pygame.display.flip()

def draw_world_size_menu():
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (50, 50, 300, 50))
    text = font.render('Elige el tamaño del mundo:', True, BLUE)
    screen.blit(text, (60, 60))
    
    pygame.draw.rect(screen, WHITE, (50, 120, 100, 50))
    text = font.render('Grande', True, BLUE)
    screen.blit(text, (60, 130))
    pygame.draw.rect(screen, WHITE, (200, 120, 100, 50))
    text = font.render('Pequeño', True, BLUE)
    screen.blit(text, (210, 130))
    pygame.draw.rect(screen, WHITE, (50, 190, 100, 50))
    text = font.render('Normal', True, BLUE)
    screen.blit(text, (60, 200))
    
    pygame.display.flip()

def draw_name_input_menu():
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (50, 50, 300, 50))
    text = font.render('Ingresa el nombre del mundo:', True, BLUE)
    screen.blit(text, (60, 60))
    
    # Campo de entrada para el nombre del mundo
    input_surface = input_font.render(input_text, True, WHITE)
    screen.blit(input_surface, (60, 100))
    pygame.draw.rect(screen, WHITE, (60, 100, 300, 30), 2)
    
    pygame.draw.rect(screen, WHITE, (50, 150, 100, 50))
    text = font.render('Crear', True, BLUE)
    screen.blit(text, (60, 160))
    pygame.draw.rect(screen, WHITE, (200, 150, 100, 50))
    text = font.render('Volver', True, BLUE)
    screen.blit(text, (210, 160))
    
    pygame.display.flip()

def draw_game():
    global player_rect, name_rect, direction, world_size, world_name
    
    screen.fill(GREEN)
    
    # Dibujar árboles
    for _ in range(10):  # Ajusta el número de árboles según lo necesites
        tree_x = pygame.randint(0, WIDTH - 40)
        tree_y = pygame.randint(0, HEIGHT - 40)
        pygame.draw.rect(screen, DARK_GREEN, (tree_x, tree_y, 40, 40))  # Tronco
        pygame.draw.rect(screen, GREEN, (tree_x - 10, tree_y - 20, 60, 20))  # Hojas
    
    # Dibuja al jugador
    pygame.draw.rect(screen, WHITE, player_rect)  # Puedes usar una imagen en lugar de un rectángulo si lo prefieres
    
    # Mover el nombre del jugador
    name_surface = font.render(player_name, True, WHITE)
    screen.blit(name_surface, name_rect.topleft)
    
    # Actualizar posición del nombre del jugador
    name_rect.x += direction * name_speed
    if name_rect.right > WIDTH or name_rect.left < 0:
        direction *= -1

    if cat_dialog_visible:
        pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 4))  # Cuadro de diálogo
        dialog_text = font.render("Bienvenido aventurero esto es Fire Knight. Aquí tenemos beta, no hay mucho porque lo estamos haciendo, así que disfruta.", True, BLACK)
        screen.blit(dialog_text, (WIDTH // 4 + 10, HEIGHT // 4 + 10))
    
    pygame.display.flip()

def handle_input(event):
    global input_text, active_menu, game_running, player_rect, cat_dialog_visible
    global world_size, world_name
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:  # Salir del menú activo
            active_menu = None
        elif event.key == pygame.K_RETURN:
            if active_menu == 'Crear Mundo' and not game_running:
                active_menu = 'WorldSize'
            elif active_menu == 'WorldSize':
                if world_size:
                    active_menu = 'NameInput'
            elif active_menu == 'NameInput':
                if input_text:
                    world_name = input_text
                    active_menu = None
                    game_running = True
        elif event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]  # Eliminar el último carácter
        elif event.key == pygame.K_TAB:
            active_menu = None  # Volver al menú principal
        elif event.key == pygame.K_c:
            # Mostrar o ocultar el cuadro de diálogo del gato
            cat_dialog_visible = not cat_dialog_visible
        elif event.key == pygame.K_w:
            player_rect.y -= 5  # Mover el jugador hacia arriba
        elif event.key == pygame.K_s:
            player_rect.y += 5  # Mover el jugador hacia abajo
        elif event.key == pygame.K_a:
            player_rect.x -= 5  # Mover el jugador hacia la izquierda
        elif event.key == pygame.K_d:
            player_rect.x += 5  # Mover el jugador hacia la derecha
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if buttons['Jugar'].collidepoint(x, y):
            draw_loading_screen(0.0)
            for i in range(101):
                draw_loading_screen(i / 100.0)
                time.sleep(0.01)  # Simular carga
            active_menu = 'WorldSize'
        elif exit_button.collidepoint(x, y):
            pygame.quit()
            sys.exit()
        elif active_menu == 'WorldSize':
            if pygame.Rect(50, 120, 100, 50).collidepoint(x, y):
                world_size = 'Grande'
                active_menu = 'NameInput'
            elif pygame.Rect(200, 120, 100, 50).collidepoint(x, y):
                world_size = 'Pequeño'
                active_menu = 'NameInput'
            elif pygame.Rect(50, 190, 100, 50).collidepoint(x, y):
                world_size = 'Normal'
                active_menu = 'NameInput'
        elif active_menu == 'NameInput':
            if pygame.Rect(50, 150, 100, 50).collidepoint(x, y):
                if input_text:
                    world_name = input_text
                    active_menu = None
                    game_running = True
            elif pygame.Rect(200, 150, 100, 50).collidepoint(x, y):
                active_menu = None
        elif not active_menu:
            for name, rect in buttons.items():
                if rect.collidepoint(x, y):
                    active_menu = name
                    break

def main():
    global game_running, active_menu

    # Pantalla de carga inicial
    while not game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            handle_input(event)

        if active_menu:
            if active_menu == 'WorldSize':
                draw_world_size_menu()
            elif active_menu == 'NameInput':
                draw_name_input_menu()
            else:
                draw_menu()
        else:
            draw_menu()

    # Juego
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            handle_input(event)
        
        draw_game()

if __name__ == "__main__":
    main()
