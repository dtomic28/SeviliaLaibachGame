import pygame, pygame_menu,sys, random
from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Game with libach")

fps=pygame.time.Clock()
allAnimationTimer=0
allAnimationFrame=0

screen1 = pygame.display.set_mode((1920,1080),NOFRAME)
screen2 = pygame.Surface((640,360))

#player images
raketa0 = pygame.image.load("raketa/raketa0.png")
raketa1 = pygame.image.load("raketa/raketa1.png")
raketa2 = pygame.image.load("raketa/raketa2.png")
raketa3 = pygame.image.load("raketa/raketa3.png")
#player images
raketa=[raketa0,raketa1,raketa2,raketa3]
raketaAnimationFrame=0
raketaAnimationTimer=0

levelState=0
artifactLVL=[]
strehaLVL=[]
buildingLVL=[]
frameSez=[]

#lvl0 images 
Zeroartifact0_png=pygame.image.load("level0/artifact0.png")
Zeroartifact1_png=pygame.image.load("level0/artifact1.png")
Zeroartifact2_png=pygame.image.load("level0/artifact2.png")
Zeroartifact3_png=pygame.image.load("level0/artifact3.png")
Zeroartifact4_png=pygame.image.load("level0/artifact4.png")
Zerobuilding0_png=pygame.image.load("level0/stavba/stavba0.png")
Zerobuilding1_png=pygame.image.load("level0/stavba/stavba1.png")
Zerobuilding2_png=pygame.image.load("level0/stavba/stavba2.png")
Zerostreha0_png=pygame.image.load("level0/stavba/streha0.png")
Zerostreha1_png=pygame.image.load("level0/stavba/streha1.png")
ZeroBackground_png=pygame.image.load("level0/background.png")

Zeroartefact0Sez=[Zeroartifact0_png]
Zeroartefact1Sez=[Zeroartifact1_png]
Zeroartefact2Sez=[Zeroartifact2_png]
Zeroartefact3Sez=[Zeroartifact3_png]
Zeroartefact4Sez=[Zeroartifact4_png]
buildingImageSez0=[Zerobuilding0_png,Zerobuilding1_png,Zerobuilding2_png]
artifactSez0=[[Zeroartefact0Sez,0,1],[Zeroartefact1Sez,0,1],[Zeroartefact2Sez,0,1],[Zeroartefact3Sez,0,1],[Zeroartefact4Sez,0,1]]
strehaSez0=[Zerostreha0_png,Zerostreha1_png]
#lvl0 images 

#lvl1 images
Oneartifact0_png=pygame.image.load("level1/artifact0.png")
Oneartifact1_png=pygame.image.load("level1/artifact1.png")
Oneartifact2_png=pygame.image.load("level1/artifact2.png")
Oneartifact3_png=pygame.image.load("level1/artifact3.png")
Oneartifact4_png=pygame.image.load("level1/artifact4.png")
Onebuilding0_png=pygame.image.load("level1/stavba/stavba0.png")
Onebuilding1_png=pygame.image.load("level1/stavba/stavba1.png")
Onebuilding2_png=pygame.image.load("level1/stavba/stavba2.png")
Onestreha0_png=pygame.image.load("level1/stavba/streha0.png")
Onestreha1_png=pygame.image.load("level1/stavba/streha1.png")
OneBackground_png=pygame.image.load("level1/background.png")

Oneartefact0Sez=[Oneartifact0_png]
Oneartefact1Sez=[Oneartifact1_png]
Oneartefact2Sez=[Oneartifact2_png]
Oneartefact3Sez=[Oneartifact3_png]
Oneartefact4Sez=[Oneartifact4_png]
buildingImageSez1=[Onebuilding0_png,Onebuilding1_png,Onebuilding2_png]
artifactSez1=[[Oneartefact0Sez,0,1],[Oneartefact1Sez,0,1],[Oneartefact2Sez,0,1],[Oneartefact3Sez,0,1],[Oneartefact4Sez,0,1]]
strehaSez1=[Onestreha0_png,Onestreha1_png]
#lvl1 images

#lvl2 images
Two0artifact0_png=pygame.image.load("level2/ptic/ptic0.png")
Two1artifact0_png=pygame.image.load("level2/ptic/ptic1.png")
Two2artifact0_png=pygame.image.load("level2/ptic/ptic2.png")
Two3artifact0_png=pygame.image.load("level2/ptic/ptic3.png")
Two4artifact0_png=pygame.image.load("level2/ptic/ptic4.png")
Twoartifact0_png=pygame.image.load("level2/artifact0.png")
Twoartifact1_png=pygame.image.load("level2/artifact1.png")
Twoartifact2_png=pygame.image.load("level2/artifact2.png")
Twoartifact3_png=pygame.image.load("level2/artifact3.png")
Twobuilding0_png=pygame.image.load("level2/stavba/stavba0.png")
Twobuilding1_png=pygame.image.load("level2/stavba/stavba1.png")
Twobuilding2_png=pygame.image.load("level2/stavba/stavba2.png")
Twostreha0_png=pygame.image.load("level2/stavba/streha0.png")
Twostreha1_png=pygame.image.load("level2/stavba/streha1.png")
Twostreha2_png=pygame.image.load("level2/stavba/streha2.png")
Twostreha3_png=pygame.image.load("level2/stavba/streha3.png")
Twostreha4_png=pygame.image.load("level2/stavba/streha4.png")
Twostreha5_png=pygame.image.load("level2/stavba/streha5.png")
TwoBackground_png=pygame.image.load("level2/background.png")
Twoartefact0Sez=[Two0artifact0_png,Two1artifact0_png,Two2artifact0_png,Two3artifact0_png,Two4artifact0_png]
Twoartefact1Sez=[Twoartifact1_png]
Twoartefact2Sez=[Twoartifact2_png]
Twoartefact3Sez=[Twoartifact3_png]
Twoartefact4Sez=[Twoartifact0_png]
artifactSez2=[[Twoartefact1Sez,0,1],[Twoartefact0Sez,0,5],[Twoartefact2Sez,0,1],[Twoartefact3Sez,0,1],[Twoartefact4Sez,0,1]]
strehaSez2=[Twostreha0_png,Twostreha1_png,Twostreha2_png,Twostreha3_png,Twostreha4_png,Twostreha5_png]
buildingImageSez2=[Twobuilding0_png,Twobuilding1_png,Twobuilding2_png]
#lvl2 images

#lvl3 images

#lvl3 images 

sound1=[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 0.0, 3.0, 3.0, 4.0, 2.0, 2.0, 2.0, 3.0, 2.0, 3.0, 4.0, 2.0, 2.0, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 2.0, 1.0, 2.0, 2.0, 3.0, 2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 1.0, 4.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 4.0, 3.0, 2.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 4.0, 2.0, 3.0, 2.0, 2.0, 3.0, 1.0, 2.0, 
3.0, 3.0, 1.0, 1.0, 2.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 3.0, 2.0, 0.0, 2.0, 2.0, 1.0, 2.0, 3.0, 2.0, 2.0, 1.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 2.0, 3.0, 3.0, 4.0, 3.0, 0.0, 2.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 2.0, 4.0, 4.0, 3.0, 2.0, 3.0, 1.0, 3.0, 3.0, 3.0, 2.0, 1.0, 3.0, 3.0, 1.0, 3.0, 3.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 2.0, 3.0]
artifactTimer=0
artifactFrame=0
artifactScreenSez=[]
artifactImage=""
artifactState=0

buildingSpawnTimer=0
buildingSez=[]
rectSez=[]
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
    def __init__(self,x,y,number,artifactImage,opacity,numberOfFrames):
        self.x=x
        self.y=y
        self.number=number
        self.artifactImage=artifactImage
        self.opacitySetting=opacity
        self.opacity=self.artifactImage[0].set_alpha(self.opacitySetting)
        self.numberOfFrames=numberOfFrames

class building:
    def __init__(self,x,y,image):
        self.x=x
        self.y=y
        self.image=image


Player = mainCharacter(True,32,33,0,0)
cameraMVX=0

#ozadjeAnimation=["pravilno0.png","pravilna1.png","pravilno2.png","pravilno3.png","pravilno4.png","pravilno5.png","pravilno6.png"] Primer animacije
frame=0
gameStop=False

def imageLoad(frame,animation,x,y):
    screen2.blit(animation[frame],(x-cameraMVX,y))

def buildingLoading(buildingHight,buildingType):
    global buildingSez,rectSez,buildingLVL
    for buildingY in range(12):
        if(buildingY<buildingHight or buildingY>buildingHight+5):
            buildingSez.append(building(Player.x+560,buildingY*32,buildingLVL[buildingType]))
            rectSez.append(Rect(Player.x+560,buildingY*32,32,32))
        if(buildingY==buildingHight):
            buildingSez.append(building(Player.x+560,buildingY*32,strehaLVL[0]))
            rectSez.append(Rect(Player.x+560,buildingY*32,32,32))
        if(buildingY==buildingHight+5):
            buildingSez.append(building(Player.x+560,buildingY*32,strehaLVL[1]))
            rectSez.append(Rect(Player.x+560,buildingY*32,32,32))

music1 = pygame.mixer.Sound("sound/song1MP.mp3")
pygame.mixer.music.load('sound/song1MP.mp3')
startMusicTimer=False
w, h = pygame.display.get_surface().get_size()
def main():
    global cameraMVX, frame, artifactFrame, artifactTimer,artifactScreenSez,artifactImage,artifactState,w,h,fps,buildingSpawnTimer,buildingSez,buildingImageSez1,rectSez, startMusicTimer,gameStop,artifactSez1,strehaSez1, levelState,buildingLVL,artifactLVL,strehaLVL,raketa,raketaAnimationFrame,raketaAnimationTimer,sound1,buildingImageSez2,artifactSez2,strehaSez2,frameSez,allAnimationTimer,allAnimationFrame,TwoBackground_png,OneBackground_png,artifactSez0,buildingImageSez0,strehaSez0,ZeroBackground_png
    while(gameStop==False):
        allAnimationTimer=(allAnimationTimer+1)%10
        if(allAnimationTimer==9):
            allAnimationFrame+=1
        if(levelState==0):
            artifactLVL=artifactSez0
            buildingLVL=buildingImageSez0
            Background_png=ZeroBackground_png
            strehaLVL=strehaSez0
            soundSez=sound1
        if(levelState==1):
            artifactLVL=artifactSez1
            buildingLVL=buildingImageSez1
            Background_png=OneBackground_png
            strehaLVL=strehaSez1
            soundSez=sound1
        if(levelState==2):
            artifactLVL=artifactSez2
            buildingLVL=buildingImageSez2
            strehaLVL=strehaSez2
            Background_png=TwoBackground_png
            soundSez=sound1
            
        frame+=1
        cameraMVX= Player.x-50
        Player_rect = Rect(Player.x,Player.y,24,15)
        screen1.blit(pygame.transform.scale(screen2,(1920,1080)),(0,0))
        screen2.fill([0,255,255])
        screen2.blit(Background_png,(0,0))
        if(artifactFrame<=((len(soundSez)-len(soundSez)%5))):
            artifactTimer=(artifactTimer+1)%12
            if(artifactTimer==11):
                artifactFrame+=1
                whichArtifact=0
                artifactHight=0
                if(soundSez[artifactFrame] ==0):
                    whichArtifact=1
                    artifactHight=240
                    artifactImage=artifactLVL[0][0]
                if(soundSez[artifactFrame] ==1):
                    whichArtifact=1
                    artifactHight=190
                    artifactImage=artifactLVL[1][0]
                if(soundSez[artifactFrame] ==2):
                    whichArtifact=2
                    artifactHight=140
                    artifactImage=artifactLVL[2][0]
                if(soundSez[artifactFrame] ==3):
                    whichArtifact=3
                    artifactHight=90
                    artifactImage=artifactLVL[3][0]
                if(soundSez[artifactFrame] ==4): 
                    whichArtifact=4
                    artifactHight=40
                    artifactImage=artifactLVL[4][0]
                if(soundSez[artifactFrame]!=artifactState):
                    artifactState=soundSez[artifactFrame]
                    artifact1=artifact2(Player.x+360,artifactHight,whichArtifact,artifactImage,255,artifactLVL[int(soundSez[artifactFrame])][2])
                    artifactScreenSez.append(artifact1)
        for artifactInGame in artifactScreenSez:
            if(artifactInGame.x<Player.x+120):
                artifactInGame.opacitySetting-=2
                artifactInGame.artifactImage[allAnimationFrame%artifactInGame.numberOfFrames].set_alpha(artifactInGame.opacitySetting)
            else:
                artifactInGame.artifactImage[allAnimationFrame%artifactInGame.numberOfFrames].set_alpha(artifactInGame.opacitySetting)
            screen2.blit(artifactInGame.artifactImage[allAnimationFrame%artifactInGame.numberOfFrames],(artifactInGame.x-cameraMVX+200,artifactInGame.y))
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
                rectSez.pop(buildingIndex)
            buildingIndex+=1
                    
        for keyPressed in pygame.event.get():
            if(keyPressed.type == KEYUP):
                if(keyPressed.key == K_w or keyPressed.key == K_s):
                    Player.SpeedY=0
            if(keyPressed.type == KEYDOWN):
                if (keyPressed.key == K_ESCAPE):
                    pygame.mixer.music.pause()
                    gameStop=True
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


        if(Player.y>360 or collideTest(Player_rect,rectSez)==True or startMusicTimer==False or Player.y<-32):
            Player.x=32
            Player.y=320
            Player.state=True
            artifactScreenSez=[]
            artifactTimer=0
            artifactFrame=0
            buildingSpawnTimer=0
            buildingSez=[]
            startMusicTimer=True
            rectSez=[]
            pygame.mixer.music.stop()
            pygame.mixer.music.play(1)
        raketaAnimationTimer=(raketaAnimationTimer+1)%10
        if(raketaAnimationTimer==9):
            raketaAnimationFrame=(raketaAnimationFrame+1)%4
        
        imageLoad(raketaAnimationFrame,raketa,Player.x,Player.y)
        pygame.display.update()
        fps.tick(60)
        

def playLevel(level: int):
    global gameStop, levelState,artifactScreenSez,artifactTimer,artifactFrame,buildingSpawnTimer,buildingSez,rectSez
    levelState = level
    Player.x=32
    Player.y=320
    Player.state=True
    artifactScreenSez=[]
    artifactTimer=0
    artifactFrame=0
    buildingSpawnTimer=0
    buildingSez=[]
    rectSez=[]
    pygame.mixer.music.stop()
    pygame.mixer.music.play(1)
    gameStop = False
    main()


def checkIfLocked(level: int):
    uImg = ["./images/menu/0.png", "./images/menu/1.png", "./images/menu/2.png", "./images/menu/3.png", "./images/menu/4.png", "./images/menu/5.png", "./images/menu/6.png"]
    lImg = ["./images/menu/0.png", "./images/menu/1.png", "./images/menu/2l.png", "./images/menu/3l.png", "./images/menu/4l.png", "./images/menu/5l.png", "./images/menu/6l.png"]
    return lImg[level]

def credits():
    pass

def exitMenu():
    exit_menu = pygame_menu.Menu("", 1920, 1080, theme = submenu_theme)
    exit_menu.add.label("Are you sure you want to exit", font_size=65, font_color = (255,0,0))
    exit_menu.add.vertical_margin(50)
    btn1 = exit_menu.add.button('Yes', pygame_menu.events.EXIT)
    btn2 = exit_menu.add.button('Cancel', exit_menu.disable)
    exit_menu.mainloop(screen1)

def levels():
    play_levels = pygame_menu.Menu("Levels", 1920, 1080, theme = submenu_theme)

    image0 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(0))
    image1 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(1))
    image2 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(2))
    image3 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(3))
    image4 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(4))
    image5 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(5))
    image6 = pygame_menu.baseimage.BaseImage(image_path = checkIfLocked(6))

    btn0 = play_levels.add.button(" ", playLevel,0,background_color=image0).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Tutorial level', font_size=40)
    play_levels.add.vertical_margin(20)       
        
    btn1 = play_levels.add.button(" ", playLevel,1, background_color=image1).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Level 1', font_size=40)
    play_levels.add.vertical_margin(20)

    btn2 = play_levels.add.button(" ", playLevel,2, background_color=image2).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Level 2', font_size=40)
    play_levels.add.vertical_margin(20)

    btn3 = play_levels.add.button(" ", playLevel,3, background_color=image3).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Level 3', font_size=40)
    play_levels.add.vertical_margin(20)

    btn4 = play_levels.add.button(" ", playLevel,4, background_color=image4).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Level 4', font_size=40)
    play_levels.add.vertical_margin(20)

    btn5 = play_levels.add.button(" ", playLevel,5, background_color=image5).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Level 5', font_size=40)
    play_levels.add.vertical_margin(20)

    btn6 = play_levels.add.button(" ", playLevel,6, background_color=image6).resize(264*1.2, 369*1.2)
    play_levels.add.vertical_margin(20)
    play_levels.add.label('Level 6', font_size=40)
    play_levels.add.vertical_margin(20)
    
    play_levels.add.vertical_margin(100)  
    play_levels.add.button('Back', play_levels.disable)
    play_levels.add.vertical_margin(100)
    play_levels.mainloop(screen1)



menu_font = pygame_menu.font.FONT_8BIT  #set font
menu_background_image = pygame_menu.baseimage.BaseImage(image_path = "./images/menuBackground.png") #open background image
menu_theme = pygame_menu.themes.THEME_DARK.copy() #copy existing theme
menu_theme.background_color = menu_background_image #set background image
menu_theme.widget_font = menu_font #set selected font
menu_theme.widget_font_size = 64 #set font size
menu_theme.widget_selection_effect = pygame_menu.widgets.SimpleSelection() #set selection type


submenu_background_image = pygame_menu.baseimage.BaseImage(image_path = "./images/subMenuBackground.png") 
submenu_theme = pygame_menu.themes.THEME_DARK.copy() 
submenu_theme.background_color = submenu_background_image 
submenu_theme.widget_font = menu_font 
submenu_theme.widget_font_size = 64 
submenu_theme.widget_selection_effect = pygame_menu.widgets.SimpleSelection()


menu = pygame_menu.Menu("",1920, 1080, theme = menu_theme)
menu.add.label("Play with Laibach", font_size=100, font_color = (255,255,255))
menu.add.vertical_margin(500)
menu.add.button('Play', levels) 
menu.add.button('Credits', credits) 
menu.add.button('Quit', exitMenu) 

menu.mainloop(screen1) #main loop