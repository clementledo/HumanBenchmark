import pygame
import random
import time
from utils import display_color, ask_menu_or_quit

def get_player_input(screen, prompt):
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 50)
    text = font.render(prompt, True, (0, 0, 0))
    screen.blit(text, (50, 200))
    pygame.display.flip()
    
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
        screen.fill((255, 255, 255))  # Blanc
        screen.blit(text, (50, 200))
        input_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(input_surface, (50, 300))
        pygame.display.flip()

def choose_difficulty(screen):
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 50)
    text = font.render("Choisissez la difficulté:", True, (0, 0, 0))
    screen.blit(text, (50, 200))
    text = font.render("1. Facile", True, (0, 0, 0))
    screen.blit(text, (50, 300))
    text = font.render("2. Difficile", True, (0, 0, 0))
    screen.blit(text, (50, 400))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "easy"
                elif event.key == pygame.K_2:
                    return "hard"

def display_two_colors(screen, color1, color2):
    screen.fill((255, 255, 255))  # Blanc
    pygame.draw.rect(screen, color1, (0, 0, screen.get_width() // 2, screen.get_height()))
    pygame.draw.rect(screen, color2, (screen.get_width() // 2, 0, screen.get_width() // 2, screen.get_height()))
    pygame.display.flip()

def color_count_game(screen):
    difficulty = choose_difficulty(screen)
    if difficulty is None:
        return
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_counts = {color: 0 for color in colors}
    for _ in range(30):
        if difficulty == "easy":
            color = random.choice(colors)
            display_color(screen, color)
            color_counts[color] += 1
        elif difficulty == "hard":
            color1, color2 = random.sample(colors, 2)
            display_two_colors(screen, color1, color2)
            color_counts[color1] += 1
            color_counts[color2] += 1
        time.sleep(0.5)
    
    player_counts = {}
    for color in colors:
        color_name = "Rouge" if color == (255, 0, 0) else "Vert" if color == (0, 255, 0) else "Bleu"
        player_input = get_player_input(screen, f"Combien de fois {color_name} est apparu?")
        if player_input is not None:
            player_counts[color] = int(player_input)
        else:
            return
    
    screen.fill((255, 255, 255))  # Blanc
    font = pygame.font.Font(None, 50)
    y_offset = 200
    won = True
    for color, count in color_counts.items():
        color_name = "Rouge" if color == (255, 0, 0) else "Vert" if color == (0, 255, 0) else "Bleu"
        player_count = player_counts.get(color, 0)
        result_text = f"{color_name}: {count} (Vous: {player_count})"
        text = font.render(result_text, True, (0, 0, 0))
        screen.blit(text, (50, y_offset))
        y_offset += 100
        if count != player_count:
            won = False
    
    result_text = "Gagné!" if won else "Perdu!"
    text = font.render(result_text, True, (0, 0, 0))
    screen.blit(text, (50, y_offset))
    pygame.display.flip()
    
    ask_menu_or_quit(screen)
