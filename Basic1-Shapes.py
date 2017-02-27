import   pygame, sys

## Main Set up
#Initialize Pygame
pygame.init()

#width and height of screen
width=600
height=600

#color of screen
black=0,0,0

#Creating the screen
screen=pygame.display.set_mode((width, height))
#set screen to black
screen.fill(black)
pygame.display.set_caption("First Game", "First Game")

clock=pygame.time.Clock()
FPS = 24

clr1=(22, 122, 211)
clr2=(100,10,133)
clr3=(54, 67,78)

### Main Loop

while 1:
    #PROCESS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #PROCESS
    #LOGIC

    #LOGIC
    #DRAW
    pygame.draw.line(screen, clr1, (0 , 0), (width, height))
    pygame.draw.rect(screen, clr3, (40,40, 300, 100))

    pygame.draw.circle(screen, clr2, (350,200),80,2)
    pygame.display.flip()
    #DRAW

    clock.tick(FPS)