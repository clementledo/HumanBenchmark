import pygame
import random
import time

def display_color(screen, color):
    screen.fill(color)
    pygame.display.flip()

def wait_random_time(min_time, max_time):
    wait_time = random.uniform(min_time, max_time)
    time.sleep(wait_time)

def get_reaction_time():
    start_time = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                reaction_time = time.time() - start_time
                if reaction_time < 0:  # Appui avant que l'écran ne devienne vert
                    return 2.0  # Pénalité de 2 secondes
                return reaction_time

def display_score(screen, average_reaction_time):
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 50)
    text = font.render(f"Moyenne: {average_reaction_time:.3f} sec", True, (0, 0, 0))
    screen.blit(text, (50, 200))
    pygame.display.flip()

def ask_replay(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Rejouer? (O/N)", True, (0, 0, 0))
    screen.blit(text, (50, 300))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    return True
                elif event.key == pygame.K_n:
                    return False

def ask_menu_or_quit(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Menu (M) / Quitter (Q)", True, (0, 0, 0))
    screen.blit(text, (500, 50))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    return False
