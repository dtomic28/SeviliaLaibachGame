
import pygame, pygame_menu,sys, random, threading
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Game with libach")

fps=pygame.time.Clock()

screen1 = pygame.display.set_mode((1920,1080),NOFRAME)
screen2 = pygame.Surface((640,360))

mainCharacter_png = pygame.image.load("images/mainCharacter.png")
block_png = pygame.image.load("images/block.png")
artifact1_png=pygame.image.load("images/artifact1.png")
artifact2_png=pygame.image.load("images/artifact2.png")
artifact3_png=pygame.image.load("images/artifact3.png")
artifact4_png=pygame.image.load("images/artifact4.png")
building0_png=pygame.image.load("building/stavba0.png")
building1_png=pygame.image.load("building/stavba1.png")
building2_png=pygame.image.load("building/stavba2.png")
streha0_png=pygame.image.load("building/streha0.png")
streha1_png=pygame.image.load("building/streha1.png")

artifactSez=[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 0.0, 3.0, 3.0, 4.0, 2.0, 2.0, 2.0, 3.0, 2.0, 3.0, 4.0, 2.0, 2.0, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 2.0, 1.0, 2.0, 2.0, 3.0, 2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 1.0, 4.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 4.0, 3.0, 2.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 4.0, 2.0, 3.0, 2.0, 2.0, 3.0, 1.0, 2.0, 
3.0, 3.0, 1.0, 1.0, 2.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 3.0, 2.0, 0.0, 2.0, 2.0, 1.0, 2.0, 3.0, 2.0, 2.0, 1.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 2.0, 3.0, 3.0, 4.0, 3.0, 0.0, 2.0, 2.0, 5.0, 2.0, 3.0, 2.0, 3.0, 2.0, 2.0, 4.0, 4.0, 3.0, 2.0, 3.0, 1.0, 3.0, 3.0, 3.0, 2.0, 1.0, 3.0, 3.0, 1.0, 3.0, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0, 3.0]
artifactTimer=0
artifactFrame=0
artifactScreenSez=[]
artifactImage=""
artifactState=0

buildingSpawnTimer=0
buildingSez=[]
buildingImageSez=[building0_png,building1_png,building2_png,]

def collideTest(Player,rectList):
    for hit in rectList:
        if(hit.colliderect(Player)):
            return(True)
    return(False)

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

class building:
    def __init__(self,x,y,image):
        self.x=x
        self.y=y
        self.image=image


Player = mainCharacter(True,32,33,0,0)
cameraMVX=0

#ozadjeAnimation=["pravilno0.png","pravilna1.png","pravilno2.png","pravilno3.png","pravilno4.png","pravilno5.png","pravilno6.png"] Primer animacije
frame=0


def imageLoad(frame,animation):
    img=pygame.image.load(animation[frame])
    return(img)

def buildingLoading(buildingHight,buildingType):
    global buildingSez
    for buildingY in range(12):
        if(buildingY<buildingHight or buildingY>buildingHight+4):
            buildingSez.append(building(Player.x+560,buildingY*32,buildingImageSez[buildingType]))
        if(buildingY==buildingHight):
            buildingSez.append(building(Player.x+560,buildingY*32,streha0_png))
        if(buildingY==buildingHight+4):
            buildingSez.append(building(Player.x+560,buildingY*32,streha1_png))

music1 = pygame.mixer.Sound("sound/song1MP.mp3")
pygame.mixer.music.load('sound/song1MP.mp3')
pygame.mixer.music.play(1)
w, h = pygame.display.get_surface().get_size()
thread1 = buildingLoading(0,0)
def main():
    global cameraMVX, frame, artifactFrame, artifactTimer,artifactScreenSez,artifactImage,artifactState,w,h,fps,buildingSpawnTimer,buildingSez,buildingImageSez
    while(True):
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
                if(artifactInGame.x<Player.x-130):
                    artifactScreenSez.pop(0)

        buildingSpawnTimer=(buildingSpawnTimer+1)%240
        if(buildingSpawnTimer==239):
            buildingHight=random.randint(0,8)
            buildingType=random.randint(0,2)
            buildingLoading(buildingHight,buildingType)
        buildingIndex=0
        for buildingBlock in buildingSez:
            screen2.blit(buildingBlock.image,(buildingBlock.x-cameraMVX	,buildingBlock.y))
            if(buildingBlock.x<Player.x-200):
                buildingSez.pop(buildingIndex)
            buildingIndex+=1
                    
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
            Player.SpeedY=3
        else:
            Player.SpeedY=-3
        Player.y+=Player.SpeedY
        Player.x+=1


        if(Player.y>360):
            Player.x=32
            Player.y=320
            Player.state=True
            artifactScreenSez=[]
            artifactTimer=0
            artifactFrame=0
            buildingSpawnTimer=0
            buildingSez=[]

        screen2.blit(mainCharacter_png,(Player.x-cameraMVX,Player.y))
        pygame.display.update()
        fps.tick(60)
        print(fps.get_fps())
        

main()