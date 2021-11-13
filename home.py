import pygame
import pygame_menu

pygame.init()

surface = pygame.display.set_mode((0,0,), pygame.FULLSCREEN, pygame.RESIZABLE)
pygame.display.set_caption("Minigames Player")

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)

#Work in progress