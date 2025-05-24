import pygame
import os
from time import sleep

from random import randint,choice 
pygame.init()
size_window=(500, 400) 
zoom = 1.5
size_background = (int(size_window[0] / zoom),int(size_window[1] / zoom))
surface_background = pygame.Surface(size_background)
size_hero = (12, 23)
size_menu = (500,400)
size_button = (80,50)
size_tower = (29,60)
size_bot = (15,13)
size_tree = (15,24)
size_hp = (11,11)

FPS = 60
BLACK = (5,5,5)
YELLOW = (300,300)
RED= (128,0,0)
bot_list = list()
atack_list = list()
decorations = []




abs_path=os.path.abspath(__file__ + "/..") 
hero_image_list_right =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero2.png")), size_hero)
]

hero_image_list_left =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")), size_hero)
]

bot_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime1.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime2.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime3.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime4.png")), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime5.png")), size_bot)


]

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "background.png")), size_background)

tower_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "tower.png")), size_tower)
tree_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "tree.png")), size_tree)
menu_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "menu.png")), size_menu)
play_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "button_play.png")), size_button)
exit_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "button_exit.png")), size_button)
atack_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "atack.png")), size_hero)
hp_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hp.png")), size_hp)
sk_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "sk.png")), size_hp)