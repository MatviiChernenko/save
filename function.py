from data import *

class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_count = 0
        self.image_now = self.image
        self.step = step

    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count += 1
        

class Hero(Human):
    def __init__(self, x, y, width, height, image_list, step, shoot_limit):
        super().__init__(x, y, width, height, image_list, step)
        self.image_index = 0
        self.shoot_limit = shoot_limit
        self.hp_hero = 5
        self.hp_tower = 10
        self.hp_bot = 1
        self.step_bot = 0.3
        self.kill_bots = 0
        self.level = 1
        self.coin = 0
        self.start_time = pygame.time.get_ticks()
        self.walk = {"up": False, "down": False, "left": False, "right": False}
        self.direction = "right"
        self.can_shoot = True
        self.last_hit_time = 0

    def move(self, surface, camera_x, camera_y):
        self.stay = True
        if self.walk["left"] and self.x > 0:
            self.x -= self.step
            self.direction = "left"
            self.stay = False
        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step
            self.direction = "right"
            self.stay = False
        if self.walk["up"] and self.y > 145:
            self.y -= self.step
            self.stay = False
        if self.walk["down"] and self.y < 200:
            self.y += self.step
            self.stay = False

        if self.direction == "left":
            self.image_now = pygame.transform.flip(self.image, True, False)
        else:
            self.image_now = self.image

        self.move_image()
        surface.blit(self.image_now, (self.x - camera_x, self.y - camera_y))
        font_hp = pygame.font.Font(None,24)

        surface.blit(hp_hero_image,(self.x - 130 - camera_x,self.y - 115 - camera_y))
        hp_hero_text = font_hp.render(f"x{self.hp_hero}", True,RED)
        surface.blit(hp_hero_text,(self.x - 139 - camera_x + 20,self.y - 120 - camera_y))

        surface.blit(hp_tower_image,(self.x - 130 - camera_x,self.y - 100 - camera_y))
        hp_tower_text = font_hp.render(f"x{self.hp_tower}", True,RED)
        surface.blit(hp_tower_text,(self.x - 139 - camera_x + 20,self.y - 105 - camera_y))

        surface.blit(sk_image,(self.x + 115 - camera_x,self.y - 120 - camera_y))
        kill_text = font_hp.render(f"x{self.kill_bots}", True,RED)
        surface.blit(kill_text,(self.x + 110 - camera_x + 20,self.y - 120 - camera_y))

        surface.blit(coin_image,(self.x - 130 - camera_x,self.y - 83 - camera_y))
        coin_text = font_hp.render(f"x{self.coin}", True,YELLOW)
        surface.blit(coin_text,(self.x - 135 - camera_x + 20,self.y - 85 - camera_y))

        level = font_hp.render(f"{self.level}", True,BLUE)
        surface.blit(level,(self.x + 115 - camera_x,self.y - 105 - camera_y))
        level_text = font_hp.render(f"level", True,BLUE)
        surface.blit(level_text,(self.x + 110 - camera_x + 20,self.y - 105 - camera_y))

class Tower(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        self.image_count = 0

    def blit(self, surface, camera_x, camera_y):
        surface.blit(self.image, (self.x - camera_x, self.y - camera_y))


class Atack(pygame.Rect):
    def __init__(self, x, y, width, height, image,direction):
        super().__init__(x, y, width, height)
        self.image = image
        self.direction = direction
        self.image_count = 0

        if direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.image

    def blit(self, surface, camera_x, camera_y):
            surface.blit(self.image, (self.x - camera_x, self.y - camera_y))


class Bot(Human):
    def __init__(self, x, y, width, height, image_list, step, direction,hp):
        super().__init__(x, y, width, height,image_list,step)
        self.fx = float(x)
        self.start_y = y
        self.start_time = 0
        self.random_time = randint(1500, 2000)
        self.direction = direction


    def move(self, surface, camera_x, camera_y):
        if self.direction == "left":
            self.fx -= self.step
        else:
            self.fx += self.step
        self.move_image()
        if self.direction == "left":
            self.image_now = pygame.transform.flip(self.image, True, False)
        else:
            #self.image = self.image_list[0]
            self.image_now = self.image
        self.x = int(self.fx)
        surface.blit(self.image_now, (self.x - camera_x, self.y - camera_y))

