import pygame
import random
import time
from utils import display_color, wait_random_time, get_reaction_time

def display_score(screen, average_reaction_time):
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 74)
    text = font.render(f"Moyenne: {average_reaction_time:.3f} sec", True, (0, 0, 0))
    screen.blit(text, (50, 250))
    pygame.display.flip()

def ask_replay(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("Rejouer? (O/N)", True, (0, 0, 0))
    screen.blit(text, (50, 350))
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

def reaction_time_game(screen):
    reaction_times = []
    for _ in range(10):
        display_color(screen, (255, 0, 0))  # Rouge
        wait_random_time(2, 5)
        display_color(screen, (0, 255, 0))  # Vert
        reaction_time = get_reaction_time()
        if reaction_time is not None:
            reaction_times.append(reaction_time)
        else:
            return False
    
    average_reaction_time = sum(reaction_times) / len(reaction_times)
    display_score(screen, average_reaction_time)
    return ask_replay(screen)

def color_count_game(screen):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_counts = {color: 0 for color in colors}
    for _ in range(30):
        color = random.choice(colors)
        display_color(screen, color)
        color_counts[color] += 1
        time.sleep(0.5)
    
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 74)
    y_offset = 250
    for color, count in color_counts.items():
        color_name = "Rouge" if color == (255, 0, 0) else "Vert" if color == (0, 255, 0) else "Bleu"
        text = font.render(f"{color_name}: {count}", True, (0, 0, 0))
        screen.blit(text, (50, y_offset))
        y_offset += 100
    pygame.display.flip()
    
    return ask_replay(screen)
