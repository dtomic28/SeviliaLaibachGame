
import pygame, pygame_menu,sys, random
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Game with libach")

screen1 = pygame.display.set_mode((1920,1080),NOFRAME)
screen2 = pygame.Surface((640,360))

mainCharacter_png = pygame.image.load("images/mainCharacter.png")
block_png = pygame.image.load("images/block.png")

def world():
    datoteka = open("map/map0.txt")
    vsebina = datoteka.read()
    datoteka.close()
    vsebina = vsebina.split('\n')
    map_sez = []
    for vrstica in vsebina:
        map_sez.append(list(vrstica))
    return (map_sez)

#dwadorhguerh
def collideTest(Player,rectList):
    for hit in rectList:
        if(hit.colliderect(Player)):
            return(True)
    return(False)

def generateWorld():
    rect_sez=[]
    y=0
    for vrstica in map_sez:
        x=0
        for block in vrstica:
            if(block=="1"):
                screen2.blit(block_png,(x*32-cameraMVX,y*32))
                rect_sez.append(Rect(x*32,y*32,32,32))
                if(x*32>Player.x+640):
                    break

            x+=1
        y+=1
    return(rect_sez)




map_sez=world()

class mainCharacter:
    def __init__(self,state,x,y,SpeedX,SpeedY):
        self.state=state
        self.x=x
        self.y=y
        self.SpeedX=SpeedX
        self.SpeedY=SpeedY

class obsticale: 
    def __init__(self,x,y):
        self.x=x
        self.y=y

Player = mainCharacter(True,32,33,0,0)
cameraMVX=0

def main():
    global cameraMVX
    while(True):
        cameraMVX= Player.x-50
        Player_rect = Rect(Player.x,Player.y,32,32)
        screen1.blit(pygame.transform.scale(screen2,(1920,1080)),(0,0))
        screen2.fill([0,255,255])
        rect_sez=generateWorld()

        for keyPressed in pygame.event.get():
            if(keyPressed.type == KEYUP):
                if(keyPressed.key == K_w or keyPressed.key == K_s):
                    Player.SpeedY=0
            if(keyPressed.type == KEYDOWN):
                if (keyPressed.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if(keyPressed.key == K_w):
                    Player.state=True
                if(keyPressed.key == K_s):
                    Player.state=False
        if(Player.state==False):
            Player.SpeedY=5
        else:
            Player.SpeedY=-5
        Player.y+=Player.SpeedY
        Player.x+=1


        if(collideTest(Player_rect,rect_sez)==True or Player.y>328):
            Player.x=32
            Player.y=320
            Player.state=True
        screen2.blit(mainCharacter_png,(Player.x-cameraMVX,Player.y))
        pygame.display.update()
        clock.tick(60)

main()