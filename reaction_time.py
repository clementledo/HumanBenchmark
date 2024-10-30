import pygame
import random
import time
from utils import display_color, wait_random_time, get_reaction_time, display_score, ask_menu_or_quit

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
            return
    
    average_reaction_time = sum(reaction_times) / len(reaction_times)
    display_score(screen, average_reaction_time)
    ask_menu_or_quit(screen)
