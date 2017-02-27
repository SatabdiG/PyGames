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

### Main Loop

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()