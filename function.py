from data import *

class Human(pygame.Rect):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height)
        self.image_list = image_list
        self.image = self.image_list[0]
        self.image_count = 0
        self.step = step

    def move_image(self):
        if self.image_count == len(self.image_list * 10) - 1:
            self.image_count = 0
        if self.image_count % 10 == 0:
            self.image = self.image_list[self.image_count // 10]
        self.image_count+=1

class Hero (Human):
    def __init__(self,x,y,width,height,image_list,step,hp):
        super().__init__(x,y,width,height,image_list,step)
        self.walk = {"left":False,"right":False,"up":False,"down":False}
        self.start_time = 0
        self.can_shoot = True
        self.shoot_limit = FPS // 2

    def shoot(self,atack):
        if atack in atack_list:
            self.can_shoot = True


    def move(self,window):
        if self.walk["left"] and self.x > 0:
            self.x -= self.step
        if self.walk["right"] and self.x < size_window[0]:
            self.x += self.step
        if self.walk["up"] and self.y > 145:
            self.y -= self.step
        if self.walk["down"] and self.y < 200:
            self.y += self.step
        window.blit(self.image,(self.x,self.y))

class Tower (pygame.Rect):
    def __init__(self,x,y,width,height,image):
        super().__init__(x,y,width,height)
        self.image = image
        self.image_count = 0

    def blit(self,window):
        window.blit(self.image,(self.x,self.y))

class Atack (pygame.Rect):
    def __init__(self,x,y,width,height,image):
        super().__init__(x,y,width,height)
        self.image = image
        self.image_count = 0

    def blit(self,window):
        window.blit(self.image,(self.x,self.y))

class Bot(Human):
    def __init__(self,x,y,width,height,image_list,step):
        super().__init__(x,y,width,height,image_list,step)
        self.start_x = x
        self.start_y = y
        self.start_time = 0
        self.random_time = randint(1500,2000)

    def move(self,window): 
        self.x -= self.step
        window.blit(self.image, (self.x, self.y)) 

    def shoot(self, time_bot):
        if time_bot - self.start_time > self.random_time:
            self.start_time = time_bot
            self.random_time = randint(1500,2500)
