import  pygame, sys
import classes, random


def process(bug, fps, total_frames):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        classes.BugProjectiles.velx = 5
        bug.going_right =True
        bug.velx=5
        bug.image=pygame.image.load("./images/bug.png")
    elif keys[pygame.K_LEFT]:
        bug.going_right =False
        bug.velx=-5
        classes.BugProjectiles.velx= -5
        bug.image=pygame.image.load("./images/Bugflipped.png")
    else:
        bug.velx=0

    ## Vertical movement
    if keys[pygame.K_UP]:
        bug.jumping=True


    if keys[pygame.K_SPACE]:
        p=classes.BugProjectiles(bug.rect.x, bug.rect.y, 43, 25, "./images/projectiles/fire.png")
        if bug.going_right:
            p.velx = 8
        else:
            p.image=pygame.transform.flip(p.image, True, False)
            p.velx = -8

    spawn(fps, total_frames)
    collisions()

def spawn(FPS, total_frames):
    if total_frames % FPS == 0:
        r= random.randint(1,2)
        x=1
        if r == 2:
            x=640-40

        classes.Fly(x,130, 40, 35, "./images/fly.png")



def collisions():
    #pygame.sprite.spritecollide(obj, grp, dokill)
    for fly in classes.Fly.FlyList:
        fly_toprojectile=pygame.sprite.spritecollide(fly, classes.BugProjectiles.projecList, True)
        if len(fly_toprojectile)>0:
            for hit in fly_toprojectile:
                fly.health-=fly.half_health

