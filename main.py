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

def collideTest(Player,rectList):
    for hit in rectList:
        if(hit.colliderect(Player)):
            return(True)
    return(False)

def generateWorld():
    rect_sez=[]
    block_sez=[]
    y=0
    for vrstica in map_sez:
        x=0
        for block in vrstica:
            if(block=="1"):
                screen2.blit(block_png,(x*32-cameraMVX,y*32))
                block_sez.append(str(x)+" "+str(y)+" "+str(block))
                rect_sez.append(Rect(x*32,y*32,32,32))
            x+=1
        y+=1

    return(rect_sez,block_sez)



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

#ozadjeAnimation=["pravilno0.png","pravilna1.png","pravilno2.png","pravilno3.png","pravilno4.png","pravilno5.png","pravilno6.png"] Primer animacije
frame=0
rectBlock_sez=generateWorld()


def imageLoad(frame,animation):
    img=pygame.image.load(animation[frame])
    return(img)

def main():
    global cameraMVX, frame
    while(True):

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


        frame+=1
        cameraMVX= Player.x-50
        Player_rect = Rect(Player.x,Player.y,32,32)
        screen1.blit(pygame.transform.scale(screen2,(1920,1080)),(0,0))
        screen2.fill([0,255,255])

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


        if(collideTest(Player_rect,rectBlock_sez[0])==True or Player.y>328):
            Player.x=32
            Player.y=320
            Player.state=True
        screen2.blit(mainCharacter_png,(Player.x-cameraMVX,Player.y))
        pygame.display.update()
        clock.tick(60)


def credits():
    pass


def levels():
    play_levels = pygame_menu.Menu("Levels", 1920, 1080, theme = menu_theme)

    table = play_levels.add.table(font_size = 40)
    table.default_cell_align = pygame_menu.locals.ALIGN_CENTER
    table.default_cell_padding = 20
    table.default_cell_border_color = (0,0,0,0)
    table.add_row(["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6"])
    menu.add.vertical_margin(20) 
    play_levels.add.button('Back', play_levels.disable)
    play_levels.mainloop(screen1)

menu_font = pygame_menu.font.FONT_8BIT #izberemo font za glavni meni

menu_background_image = pygame_menu.baseimage.BaseImage(image_path = "./images/menuBackground.png") #odpremo sliko za temo glavnega menija
menu_theme = pygame_menu.themes.THEME_DARK.copy() #kopiramo že obstoječo temo, ki jo bomo uredili
menu_theme.background_color = menu_background_image #temi nastavimo sliko ozadja
menu_theme.widget_font = menu_font #nastavimo izbrani font
menu_theme.widget_font_size = 64 #nastavimo izbrano velikost besedila
menu_theme.widget_selection_effect = pygame_menu.widgets.SimpleSelection()


menu = pygame_menu.Menu("",1920, 1080, theme = menu_theme)
menu.add.label("Play with Laibach", font_size=100, font_color = (255,255,255))
menu.add.vertical_margin(500)
menu.add.button('Play', levels) #ustvarimo gumb za igranje same igre
menu.add.button("How to play", credits)
menu.add.button('Credits', credits) #ustvarimo gumb za shop
menu.add.button('Quit', pygame_menu.events.EXIT) #in ustvarimo gumb za izhod

menu.mainloop(screen1) #ustvarimo mainloop za glavni meni