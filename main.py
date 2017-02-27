import sys, pygame
from classes import *
from process import  process

## Setup
width=640
height=360
black=0,0,0

#clock object
clock=pygame.time.Clock()
FPS=24
total_frames=0
##  Init pygame ####
backgroundvar=pygame.image.load("./images/forest.jpg")
bug=Bug(0, height- 40,40, 40, "./images/bug.png" )
fly=Fly(40, 100, 40,35, "./images/fly.png")
# fly1=Fly(40, 200, 40,35, "./images/fly.png")
# fly2=Fly(40, 400, 40,35, "./images/fly.png")
# fly3=Fly(40, 300, 40,35, "./images/fly.png")
pygame.init()

##Screen
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Loading Image", "Loading Image")
screen.fill(black)
img_bug=pygame.image.load("./images/bug.png")

## Main Game loop ###
while 1:
    #Processing
    process(bug, FPS, total_frames)
    #Processing

    #Logic
    bug.motion(width, height)
    #fly.fly(width, height)
    Fly.update_all(width, height)
    BugProjectiles.movement()
    total_frames+=1
    #Logic
    #Draw
    #screen.fill(black)
    screen.blit(backgroundvar, (0,0))
    BugProjectiles.projecList.draw(screen)
    BaseClass.allsprites.draw(screen)
    pygame.display.flip()
    #Draw


    clock.tick(FPS)