import pygame
import random, math

class BaseClass(pygame.sprite.Sprite):

    allsprites=pygame.sprite.Group()

    def __init__(self, x, y, width,height, image_string):
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)
        self.image=pygame.image.load(image_string)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

        self.width=width
        self.height=height



class Bug(BaseClass):

    List=pygame.sprite.Group()
    going_right=True

    def __init__(self, x,y, width, height, image_string):
        BaseClass.__init__(self, x,y,width, height, image_string)
        Bug.List.add(self)
        self.velx, self.vely=0,5
        self.jumping, self.go_down=False, False

    def motion(self,width , height):
        predictedloaction=self.rect.x +self.velx

        if predictedloaction < 0 :
           self.velx=0
        elif predictedloaction +self.width > width:
            self.velx=0

        if self.rect.x < 0 :
            self.rect.x=0
        elif self.rect.x +self.width > width:
            self.rect.x=width-self.width

        self.rect.x+=self.velx
        self.__jump(width, height)

    def __jump(self, width, height):
        max_jump=100

        if self.jumping:
            if self.rect.y < max_jump:
                self.go_down=True
            if self.go_down:
                self.rect.y+=self.vely
                prefictedloaction=self.rect.y+self.vely
                if prefictedloaction+ self.height>height:
                    self.jumping=False
                    self.go_down = False

            else:
                self.rect.y -=self.vely


class Fly(BaseClass):
    FlyList=pygame.sprite.Group()

    def __init__(self,x, y, width, height, image_string):
        BaseClass.__init__(self, x,y,width,height,image_string)
        Fly.FlyList.add(self)
        self.velx=random.randint(1,4)
        self.amplitude, self.period= random.randint(20, 140), random.randint(4,5)/100.0

    def fly(self, width,height):

        if self.rect.x + self.width > width or self.rect.x <0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velx = -self.velx

        self.rect.x +=self.velx

        #Sine curve
        # a *sin(bx+c) +y

        self.rect.y=self.amplitude * math.sin(self.period*self.rect.x) + 140

    @staticmethod
    def movement(width, height):
        for flies in Fly.FlyList:
            flies.fly(width, height)



class BugProjectiles(pygame.sprite.Sprite):

    projecList=pygame.sprite.Group()
    normallist=[]

    def __init__(self,x,y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

        try:
            last_element=BugProjectiles.normallist[-1]
            difference=math.fabs(self.rect.x -last_element.rect.x)

            if difference<self.width:
                return

        except Exception:
            pass

        BugProjectiles.normallist.append(self)
        BugProjectiles.projecList.add(self)
        self.velx=None

    @staticmethod
    def movement():
        for projectile in BugProjectiles.projecList:
            projectile.rect.x+=projectile.velx

