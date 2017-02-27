import sys, pygame

## Setup
width=640
height=600
black=0,0,0

##Init pygame

pygame.init()

##Screen
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Loading Image", "Loading Image")
screen.fill(black)
img_bug=pygame.image.load("./images/bug.png")

##Main loop
while 1:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(img_bug, (200,200))
    pygame.display.flip()