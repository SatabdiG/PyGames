import  pygame, sys


def process(bug):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        bug.velx =5
        bug.image=pygame.image.load("./images/bug.png")
    elif keys[pygame.K_LEFT]:
        bug.velx=-5
        bug.image=pygame.image.load("./images/Bugflipped.png")
    else:
        bug.velx=0

    ## Vertical movement
    if keys[pygame.K_UP]:
        bug.jumping=True