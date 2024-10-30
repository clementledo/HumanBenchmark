import pygame

def init_pygame_window(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fenêtre Pygame")
    return screen
