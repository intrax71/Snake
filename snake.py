#serpiente.py

import pygame
import sys
import random

pygame.init()

# Configuración de la pantalla  3
width = 250
height = 250
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de la Serpiente")

# Definir una función para mostrar la pantalla de "Game Over"
def game_over_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, red)
    text_rect = text.get_rect()
    text_rect.center = (width // 2, height // 2)
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Puntuación: {score}", True, green)
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (width // 2, height // 2 + 50)
    screen.blit(score_text, score_text_rect)

    font = pygame.font.Font(None, 24)
    restart_text = font.render("Presiona R para reiniciar", True, green)
    restart_text_rect = restart_text.get_rect()
    restart_text_rect.center = (width // 2, height // 2 + 100)
    screen.blit(restart_text, restart_text_rect)


# Inicializa el mezclador de audio de Pygame
pygame.mixer.init()

# Carga la música de fondo (ajusta la ruta al archivo de música)
pygame.mixer.music.load('C:\\Users\\isanz\\Downloads\\SaveTube.App - cancion mario kart (128 kbps).mp3')
# Reproduce la música en bucle continuo
pygame.mixer.music.play(-1)

#volumen musica 
pygame.mixer.music.set_volume(0.5)



# Colores
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Inicialización de la serpiente
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"
# Variable para controlar si el juego ha comenzado
game_started = False

# Puntuación inicial
score = 0

# Posición inicial de la comida
food = (random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10)
food_size = 10  # Tamaño de la comida


# Velocidad de la serpiente
snake_speed = 15
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, green, [segment[0], segment[1], 10, 10])

def main():
    global snake_direction, score, food, snake_speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                if event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Mueve la serpiente
        head = list(snake[0])
        if snake_direction == "UP":
            head[1] -= 10
        if snake_direction == "DOWN":
            head[1] += 10
        if snake_direction == "LEFT":
            head[0] -= 10
        if snake_direction == "RIGHT":
            head[0] += 10
        snake.insert(0, head)

        # Verifica colisión con la comida
        if (
            snake[0][0] == food[0]
            and snake[0][1] == food[1]
        ):
            score += 1
            # Hacer que la serpiente crezca un poco más
            new_segment = tuple(snake[-1])
            snake.append(new_segment)
            # Aumentar la velocidad gradualmente
            snake_speed += 1
            food = (random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10)

        else:
            snake.pop()

        # Verifica colisión con los bordes o consigo misma
        if (
            snake[0][0] < 0
            or snake[0][0] >= width
            or snake[0][1] < 0
            or snake[0][1] >= height
            or snake[0] in snake[1:]
        ):
            print("Juego terminado. Puntuación:", score)
            pygame.quit()
            sys.exit()

        # Dibuja la pantalla
        screen.fill(black)
        draw_snake(snake)
        pygame.draw.rect(screen, red, [food[0], food[1], food_size, food_size])  # Dibuja la comida
        
        pygame.display.update()

        # Control de velocidad
        clock.tick(snake_speed)

if __name__ == "__main__":
    main()
