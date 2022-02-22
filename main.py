from re import X
from sre_parse import State
import pygame, pygame_menu,sys, random
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Game with libach")

screen1 = pygame.display.set_mode((1920,1080),NOFRAME)
screen2 = pygame.Surface((1920,1080))

mainCharacter_png = pygame.image.load("images/mainCharacter.png")

class mainCharacter:
    def __init__(self,state,x,y,SpeedX,SpeedY):
        self.state=state
        self.x=x
        self.y=y
        self.SpeedX=SpeedX
        self.SpeedY=SpeedY


Player = mainCharacter(True,500,500,0,0)

def main():
    while(True):
        for keyPressed in pygame.event.get():
            if(keyPressed.type == KEYUP):
                if(keyPressed.key == K_w or keyPressed.key==K_s):
                    Player.SpeedY=0
            if(keyPressed.type == KEYDOWN):
                if (keyPressed.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if(keyPressed.key == K_w):
                    Player.SpeedY=-5
                if(keyPressed.key == K_s):
                    Player.SpeedY=5
            
        Player.y+=Player.SpeedY
        screen1.blit(pygame.transform.scale(screen2,(1920,1080)),(0,0))
        screen1.blit(mainCharacter_png,(Player.x,Player.y))
        pygame.display.update()
        clock.tick(60)

main()