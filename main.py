from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("hhhhh")

clock = pygame.time.Clock()
font = pygame.font.Font(None,40)

hero = Hero(
    0,
    0,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    5,
    5
)

tower = Tower(
    230,
    315,
    size_tower[0],
    size_tower[1],
    tower_image
)

game = True
what_window = "menu"
while game:
    events = pygame.event.get()
    tower.blit(window)
    window.blit(background_image,(0,0)) 
    hero.move(window)

    #if what_window == "menu":
    #    window.fill(BLACK)
    #    pygame.draw.rect(window,YELLOW,rest_start)
    #    pygame.draw.rect(window,YELLOW,rest_start)
   

    for event in events:
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.walk["up"] = True
            if event.key == pygame.K_s:
                hero.walk["down"] = True
            if event.key == pygame.K_a:
                hero.walk["left"] = True
            if event.key == pygame.K_d:
                hero.walk["right"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.walk["up"] = False
            if event.key == pygame.K_s:
                hero.walk["down"] = False
            if event.key == pygame.K_a:
                hero.walk["left"] = False
            if event.key == pygame.K_d:
                hero.walk["right"] = False


    clock.tick(FPS)
    pygame.display.flip()
