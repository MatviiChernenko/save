from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("hhhhh")

clock = pygame.time.Clock()
font = pygame.font.Font(None,40)

hero = Hero(
    238,
    184,
    12,
    23,
    hero_image_list_right,
    2,
    500
)

tower = Tower(
    230,
    150,
    size_tower[0],
    size_tower[1],
    tower_image
)



def fade_out(window, step=10):
    fade = pygame.Surface(size_window)
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, step):
        fade.set_alpha(alpha)
        window.blit(menu_image, (0, 0))  # фон меню
        window.blit(play_image, (225, 150))
        window.blit(exit_image, (225, 235))
        window.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(20)
        
def generate_decorations():
    decorations.clear()
    for i in range(100):
        kind = 0
        x = randint(-50,800 - tree_image.get_width())
        y = randint(0,600 - tree_image.get_height())
        if kind == 0 and x != tower.x and y != tower.y:
            decorations.append(("tree",x,y))



generate_decorations()

game = True
wich_window = 0
start_time_bot = 0
end_time_bot = 0
camera_x = 0
camera_y = 0
spawn_left = True
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
                    fade_out(window)
                    wich_window = 1 
                    pygame.event.clear()                     
                if button_exit.collidepoint(x,y):           
                    game = False



    if wich_window == 1:

        #size_window = (500,400)

        events = pygame.event.get()
        #tower.blit(window)
        #hero.move(window)

        camera_x = hero.centerx - size_background[0] // 2 
        camera_y = hero.centery - size_background[1] // 2

        #camera_x = max(0, min(camera_x, size_background[0] - size_window[0]))
        #camera_y = max(0, min(camera_y, size_background[1] - size_window[1]))
        
        scaled_background = pygame.transform.scale(background_image,surface_background.get_size())
        surface_background.blit(scaled_background,(0,0)) 
        tower.blit(surface_background,camera_x,camera_y)
        #ugh.blit(surface_background,camera_x,camera_y)
        hero.move(surface_background,camera_x,camera_y)


        for kind,x,y in decorations:
            img = tree_image
            if kind == "tree":
                surface_background.blit(img,(x - camera_x,y - camera_y))

        #surface_background.fill((0,0,0))

        if not hero.can_shoot and pygame.time.get_ticks() - hero.start_time > hero.shoot_limit:
            hero.can_shoot = True


        for atack in atack_list:
            atack.blit(surface_background,camera_x,camera_y)
            time_atack = pygame.time.get_ticks()
            if time_atack - hero.start_time > 1000:
                hero.start_time = time_atack
                atack_list.remove(atack)

        current_time = pygame.time.get_ticks()
        for bot in bot_list:
            bot.move(surface_background,camera_x,camera_y)
            if hero.colliderect(bot) and current_time - hero.last_hit_time > 1000:
                hero.last_hit_time = current_time
                hero.hp_hero -= 1
                bot_list.remove(bot)
                if hero.hp_hero < 0:
                    hero.hp_hero = 0
            if tower.colliderect(bot):
                hero.hp_tower -= 1
                bot_list.remove(bot)
                if hero.hp_tower < 0:
                    hero.hp_tower = 0

        bullet_list = list()
        for atack in atack_list:
            for bot in bot_list:
                if atack.colliderect(bot):
                    bullet_list.append(atack)
                    bot_list.remove(bot)
                    atack_list.remove(atack)
                    break   

        end_time_bot = pygame.time.get_ticks()
        if end_time_bot - start_time_bot > 2000:
            start_time_bot = end_time_bot
            y = randint(145, 200)
            if spawn_left:
                x = 0 - size_bot[0]
                direction = "right"
            else:
                x = size_window[0]
                direction = "left"
            bot_list.append(Bot(
                x,
                y,
                size_bot[0],
                size_bot[1],
                bot_image_list,
                0.3,
                direction
             ))
            spawn_left = not spawn_left
            


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
                if event.key == pygame.K_SPACE:
                    now = pygame.time.get_ticks()
                    if hero.can_shoot and now - hero.start_time > hero.shoot_limit and len(atack_list) < 1:
                        hero.start_time = now
                        hero.can_shoot = False
                        #atack_list.append(Atack(hero.centerx +5, hero.y, 10, 20, atack_image))
                        if hero.direction == "right":
                            atack_list.append(Atack(hero.centerx +5, hero.y, 10, 20, atack_image,"right"))
                        if hero.direction == "left":
                            atack_list.append(Atack(hero.centerx -15, hero.y, 10, 20, atack_image,"left"))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.walk["up"] = False
                if event.key == pygame.K_s:
                    hero.walk["down"] = False
                if event.key == pygame.K_a:
                    hero.walk["left"] = False
                if event.key == pygame.K_d:
                    hero.walk["right"] = False



        scaled = pygame.transform.scale(surface_background, size_window)
        window.blit(scaled, (0, 0))

        if hero.hp_hero <= 0 or hero.hp_tower <= 0:
            text = font.render("Game Over", True, (255, 0, 0))
            sleep(1)
            pygame.time.delay(1000)  
            wich_window = 0          
            hero.hp_hero = 5    
            hero.x = 238             
            hero.y = 184
            bot_list.clear()
            atack_list.clear()
            
    clock.tick(FPS)
    pygame.display.flip()