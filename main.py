from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("hhhhh")

clock = pygame.time.Clock()
font = pygame.font.Font(None,40)

hero = Hero(
    238,
    184,
    size_hero[0],
    size_hero[1],
    hero_image_list,
    2,
    5
)

tower = Tower(
    230,
    150,
    size_tower[0],
    size_tower[1],
    tower_image
)



game = True
wich_window = 0
start_time_bot = 0
end_time_bot = 0
while game:

    if wich_window == 0:

        window.blit(menu_image,(0,0)) 
        button_play = window.blit(play_image,(225,150))
        button_exit = window.blit(exit_image,(225,235))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x , y = event.pos
                if button_play.collidepoint(x,y):
                    wich_window = 1                   
                if button_exit.collidepoint(x,y):           
                    game = False



    if wich_window == 1:

        size_window = (500,200)

        events = pygame.event.get()
        window.blit(background_image,(0,0)) 
        tower.blit(window)
        hero.move(window)

        for atack in atack_list:
            window.blit(atack.image,(atack.x,atack.y))
            time_atack = pygame.time.get_ticks()
            if time_atack - hero.start_time > 1000:
                hero.start_time = time_atack
                atack_list.remove(atack)

        for bot in bot_list:
            bot.move(window)


        

        end_time_bot = pygame.time.get_ticks()
        if end_time_bot - start_time_bot > 2000:
            start_time_bot = end_time_bot
            bot_list.append(Bot(
                300,
                randint(145,200),
                size_bot[0],
                size_bot[1],
                bot_image_list,
                0.5
             ))
            


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
                if event.key == pygame.K_SPACE and hero.can_shoot:
                    atack_list.append(Atack(hero.centerx +5, hero.y, 10, 20, atack_image))
                    hero.can_shoot = False
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