import pygame
from games.reaction_time import reaction_time_game
from games.color_count import color_count_game
from window import init_pygame_window

def display_menu(screen):
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 50)
    text = font.render("1. Jeu de temps de réaction", True, (0, 0, 0))
    screen.blit(text, (50, 200))
    text = font.render("2. Compter les couleurs", True, (0, 0, 0))
    screen.blit(text, (50, 300))
    text = font.render("Appuyez sur 1 ou 2 pour jouer", True, (0, 0, 0))
    screen.blit(text, (50, 400))
    pygame.display.flip()

def main():
    screen = init_pygame_window(800, 600)
    running = True
    while running:
        display_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    reaction_time_game(screen)
                elif event.key == pygame.K_2:
                    color_count_game(screen)
    pygame.quit()

if __name__ == "__main__":
    main()
