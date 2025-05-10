import pygame
import os
from time import sleep

from random import randint,choice 
pygame.init()
size_window=(500, 400) 
size_background = (500,400)
size_hero = (10, 10)
size_menu = (500,400)
size_button = (80,50)
size_tower = (27,57)
size_bot = (10,10)
FPS = 60
BLACK = (5,5,5)
YELLOW = (300,300)
bot_list = list()
bullet_list = list()



abs_path=os.path.abspath(__file__ + "/..") 
hero_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")), size_hero)
]

bot_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_bot)
]

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "background.png")), size_background)

tower_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "tower.png")), size_tower)
menu_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "menu.png")), size_menu)
play_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "button_play.png")), size_button)
exit_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "button_exit.png")), size_button)
atack_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "test.png")), size_hero)
