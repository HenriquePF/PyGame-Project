import pygame
from random import randint

#Colors for the game
white = (255, 255, 255)
grey = (99, 110, 114)
black = (45, 52, 54)
red = (214, 48, 49)
verde = (0, 184, 148)
blue = (9, 132, 227)

#To see if the game initialize properly
try:
    pygame.init()
except:
    print('O módulo PyGame não foi inicializado com sucesso!')

#Dimensions of the window
largura = 640
altura = 480

#Position and size of the snake
tamanho = 10

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, grey, [XY[0], XY[1], tamanho, tamanho])

def apple(posX, posY):
    pygame.draw.rect(fundo, red, [posX, posY, tamanho, tamanho])

def game():
    posX = randint(0, (largura - tamanho) / 10) * 10
    posY = randint(0, (altura - tamanho) / 10) * 10
    appleX = randint(0, (largura - tamanho) / 10) * 10
    appleY = randint(0, (altura - tamanho) / 10) * 10
    velocidadeX = 0
    velocidadeY = 0
    CobraXY = []
    CobraComp = 1

    jogo = True
    while jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidadeX != 1.5:
                    velocidadeY = 0
                    velocidadeX = -1.5 #tamanho
                if event.key == pygame.K_RIGHT and velocidadeX != - 1.5:
                    velocidadeY = 0
                    velocidadeX = 1.5 #tamanho

                if event.key == pygame.K_UP and velocidadeY != 1.5:
                    velocidadeX = 0
                    velocidadeY = -1.5 #tamanho
                if event.key == pygame.K_DOWN and velocidadeY != - 1.5:
                    velocidadeX = 0
                    velocidadeY = 1.5 #tamanho


        fundo.fill(black)
        posX += velocidadeX
        posY += velocidadeY

        CobraInicio = []

        CobraInicio.append(posX)
        CobraInicio.append(posY)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]

        cobra(CobraXY)
        if posX == appleX and posY == appleY:
            appleX = randint(0, (largura - tamanho) / 10) * 10
            appleY = randint(0, (altura - tamanho) / 10) * 10
            CobraComp += 1

        apple(appleX, appleY)
        pygame.display.update()
        relogio.tick(120)
        #No border
        if posX > largura:
            posX = 0
        if posX < 0:
            posX = largura - tamanho

        if posY > altura:
            posY = 0
        if posY < 0:
            posY = altura - tamanho

        #WITH border
        # if posX > largura:
        #     posX = 0
        # if posX < 0:
        #     posX = largura - tamanho
        #
        # if posY > altura:
        #     posY = 0
        # if posY < 0:
        #     posY = altura - tamanho

game()
pygame.quit()