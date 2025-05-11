from data import *

class Human(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step):
        super().__init__(x, y, width, height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_count = 0
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
        self.hp = 5
        self.start_time = pygame.time.get_ticks()
        self.walk = {"up": False, "down": False, "left": False, "right": False}
        self.direction = "right"
        self.stay = True
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

        if not self.stay:
            self.image_index += 1
            if self.image_index >= len(self.image_list):
                self.image_index = 0
        else:
            self.image_index = 0

        image = self.image_list[self.image_index]
        if self.direction == "left":
            image = pygame.transform.flip(image, True, False)

        surface.blit(image, (self.x - camera_x, self.y - camera_y))

        bar_width = self.width - 8
        bar_x = self.x - camera_x - 25
        bar_y = self.y - 10 - camera_y 
        hp_width = int(self.hp * self.width)
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, 4))
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, hp_width, 4))

class Tower(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        self.image_count = 0
        self.hp = 10

    def blit(self, surface, camera_x, camera_y):
        surface.blit(self.image, (self.x - camera_x, self.y - camera_y))

        bar_width = self.width 
        bar_x = self.x - camera_x - 50
        bar_y = self.y - 10 - camera_y
        hp_width = int(self.hp * bar_width)

        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, 4))
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, hp_width, 4))

class Atack(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        self.image_count = 0

    def blit(self, surface, camera_x, camera_y):
        surface.blit(self.image, (self.x - camera_x, self.y - camera_y))

class Ugh(pygame.Rect):
    def __init__(self, x, y, width, height, image):
        super().__init__(x, y, width, height)
        self.image = image
        self.image_count = 0

    def blit(self, surface, camera_x, camera_y):
        surface.blit(self.image, (self.x - camera_x, self.y - camera_y))

class Bot(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, step, direction):
        super().__init__(x, y, width, height)
        self.fx = float(x)
        self.start_y = y
        self.start_time = 0
        self.random_time = randint(1500, 2000)
        self.direction = direction
        self.step = step
        self.image_list = image_list

        if direction == "left":
            self.image = pygame.transform.flip(self.image_list[0], True, False)
        else:
            self.image = self.image_list[0]

    def move(self, surface, camera_x, camera_y):
        if self.direction == "left":
            self.fx -= self.step
        else:
            self.fx += self.step
        self.x = int(self.fx)
        surface.blit(self.image, (self.x - camera_x, self.y - camera_y))


