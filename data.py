import pygame
import os

from random import randint,choice 
pygame.init()
size_window=(500, 600) 
size_background = (1000,1000)
size_hero = (10, 10)
size_tower = (25,50)
FPS = 60
BLACK = (5,5,5)
YELLOW = (300,300)
wall_list = list()



abs_path=os.path.abspath(__file__ + "/..") 
hero_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")), size_hero)
]

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "background.png")), size_background)
tower_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "tower.png")), size_tower)
