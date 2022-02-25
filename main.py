
import pygame, pygame_menu,sys, random
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Game with libach")

screen1 = pygame.display.set_mode((1920,1080),NOFRAME)
screen2 = pygame.Surface((640,360))

mainCharacter_png = pygame.image.load("images/mainCharacter.png")
block_png = pygame.image.load("images/block.png")
artifact1_png=pygame.image.load("images/artifact1.png")
artifact2_png=pygame.image.load("images/artifact2.png")
artifact3_png=pygame.image.load("images/artifact3.png")
artifact4_png=pygame.image.load("images/artifact4.png")
artifactSez=[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 0.0, 3.0, 3.0, 4.0, 2.0, 2.0, 2.0, 3.0, 2.0, 3.0, 4.0, 2.0, 2.0, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 2.0, 1.0, 2.0, 2.0, 3.0, 2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 1.0, 4.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 4.0, 3.0, 2.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 4.0, 2.0, 3.0, 2.0, 2.0, 3.0, 1.0, 2.0, 
3.0, 3.0, 1.0, 1.0, 2.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 3.0, 2.0, 0.0, 2.0, 2.0, 1.0, 2.0, 3.0, 2.0, 2.0, 1.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 2.0, 3.0, 3.0, 4.0, 3.0, 0.0, 2.0, 2.0, 5.0, 2.0, 3.0, 2.0, 3.0, 2.0, 2.0, 4.0, 4.0, 3.0, 2.0, 3.0, 1.0, 3.0, 3.0, 3.0, 2.0, 1.0, 3.0, 3.0, 1.0, 3.0, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0, 3.0]
artifactTimer=0
artifactFrame=0
artifactScreenSez=[]
artifactImage=""
artifactState=0
"""
def world():
    datoteka = open("map/map0.txt")
    vsebina = datoteka.read()
    datoteka.close()
    vsebina = vsebina.split('\n')
    map_sez = []
    for vrstica in vsebina:
        map_sez.append(list(vrstica))
    return (map_sez)
    """

def collideTest(Player,rectList):
    for hit in rectList:
        if(hit.colliderect(Player)):
            return(True)
    return(False)
"""
def generateWorld():
    rect_sez=[]
    block_sez=[]
    y=0
    for vrstica in map_sez:
        x=0
        for block in vrstica:
            if(block=="1"):
                block_sez.append(str(x)+" "+str(y)+" "+str(block))
                rect_sez.append(Rect(x*32,y*32,32,32))
            x+=1
        y+=1

    return(rect_sez,block_sez)
"""

"""
def bubbleSort(Sez):
    for i in range(0,len(Sez),1):
        x1=""
        xTest=0
        while(Sez[i][xTest]!=" "):
            x1+=Sez[i][xTest]
            xTest+=1
        for j in range(i,len(Sez),1):
            x2=""
            xTest2=0
            while(Sez[j][xTest2]!=" "):
                x2+=Sez[j][xTest2]
                xTest2+=1
            if(int(x1)>int(x2)):
                replaceVaule=Sez[i]
                Sez[i]=Sez[j]
                Sez[j]=replaceVaule
    return(Sez)

"""

"""
map_sez=world()
"""

class mainCharacter:
    def __init__(self,state,x,y,SpeedX,SpeedY):
        self.state=state
        self.x=x
        self.y=y
        self.SpeedX=SpeedX
        self.SpeedY=SpeedY

class artifact2: 
    def __init__(self,x,y,number,artifactImage,opacity):
        self.x=x
        self.y=y
        self.number=number
        self.artifactImage=artifactImage
        self.opacitySetting=opacity
        self.opacity=self.artifactImage.set_alpha(self.opacitySetting)

Player = mainCharacter(True,32,33,0,0)
cameraMVX=0

#ozadjeAnimation=["pravilno0.png","pravilna1.png","pravilno2.png","pravilno3.png","pravilno4.png","pravilno5.png","pravilno6.png"] Primer animacije
frame=0

"""
rectBlock_sez=generateWorld()
rectBlock_sez=[rectBlock_sez[0],bubbleSort(rectBlock_sez[1])]
print(rectBlock_sez[1])

"""

def imageLoad(frame,animation):
    img=pygame.image.load(animation[frame])
    return(img)

music1 = pygame.mixer.Sound("sound/song1MP.mp3")
pygame.mixer.music.load('sound/song1MP.mp3')
pygame.mixer.music.play(1)
w, h = pygame.display.get_surface().get_size()

def main():
    global cameraMVX, frame, artifactFrame, artifactTimer,artifactScreenSez,artifactImage,artifactState,w,h
    while(True):
        """
        for block in rectBlock_sez[1]:
            spaceCounter=0
            x=""
            y=""
            for mestoInString in block:
                if(mestoInString == " "):
                    spaceCounter+=1
                    if(spaceCounter==2):
                        break
                if(spaceCounter==0):
                    x+=mestoInString
                if(spaceCounter==1):
                    y+=mestoInString
            if(block[-1]=="1"):
                screen2.blit(block_png,(int(x)*32-cameraMVX,int(y)*32))
        """

        frame+=1
        cameraMVX= Player.x-50
        Player_rect = Rect(Player.x,Player.y,32,32)
        screen1.blit(pygame.transform.scale(screen2,(1920,1080)),(0,0))
        screen2.fill([0,255,255])
        if(artifactFrame<=((len(artifactSez)-len(artifactSez)%5))):
            artifactTimer=(artifactTimer+1)%12
            if(artifactTimer==11):
                artifactFrame+=1
                whichArtifact=0
                artifactHight=0
                if(artifactSez[artifactFrame] ==1):
                    whichArtifact=1
                    artifactHight=190
                    artifactImage=artifact1_png
                if(artifactSez[artifactFrame] ==2):
                    whichArtifact=2
                    artifactHight=140
                    artifactImage=artifact2_png
                if(artifactSez[artifactFrame] ==3):
                    whichArtifact=3
                    artifactHight=90
                    artifactImage=artifact3_png
                if(artifactSez[artifactFrame] ==4): 
                    whichArtifact=4
                    artifactHight=40
                    artifactImage=artifact4_png
                if(artifactSez[artifactFrame]!=artifactState):
                    artifactState=artifactSez[artifactFrame]
                    artifact1=artifact2(Player.x+360,artifactHight,whichArtifact,artifactImage,255)
                    artifactScreenSez.append(artifact1)
            for artifactInGame in artifactScreenSez:
                if(artifactInGame.x<Player.x+120):
                    artifactInGame.opacitySetting-=2
                    artifactInGame.artifactImage.set_alpha(artifactInGame.opacitySetting)
                else:
                    artifactInGame.artifactImage.set_alpha(artifactInGame.opacitySetting)
                screen2.blit(artifactInGame.artifactImage,(artifactInGame.x-cameraMVX+200,artifactInGame.y))
                if(artifactInGame.x<Player.x-230):
                    artifactScreenSez.pop(0)
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


        if(Player.y>328):
            Player.x=32
            Player.y=320
            Player.state=True
            artifactScreenSez=0
            artifactTimer=0
            artifactFrame=0
        screen2.blit(mainCharacter_png,(Player.x-cameraMVX,Player.y))
        pygame.display.update()
        clock.tick(60)

main()