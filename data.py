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
size_sk = (12,12)
window = pygame.display.set_mode(size_window)
FPS = 60
BLACK = (5,5,5)
YELLOW = (300,300)
RED= (128,0,0)
bot_list = list()
atack_list = list()
decorations = []




abs_path=os.path.abspath(__file__ + "/..") 
hero_image_list_right =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")).convert_alpha(), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero2.png")).convert_alpha(), size_hero)
]

hero_image_list_left =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero1.png")).convert_alpha(), size_hero),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hero2.png")).convert_alpha(), size_hero)
]

bot_image_list =[
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime1.png")).convert_alpha(), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime2.png")).convert_alpha(), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime3.png")).convert_alpha(), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime4.png")).convert_alpha(), size_bot),
    pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "slime5.png")).convert_alpha(), size_bot)


]

background_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "background.png")).convert(), size_background)
background_image2 = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "background2.png")).convert(), size_background)

tower_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "tower.png")).convert_alpha(), size_tower)
tree_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "tree.png")).convert_alpha(), size_tree)
menu_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "menu.png")).convert(), size_menu)
play_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "button_play.png")).convert_alpha(), size_button)
exit_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "button_exit.png")).convert_alpha(), size_button)
atack_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "atack.png")).convert_alpha(), size_hero)
hp_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "hp.png")).convert_alpha(), size_hp)
sk_image = pygame.transform.scale(pygame.image.load(os.path.join(abs_path, "image", "sk.png")).convert_alpha(), size_sk)