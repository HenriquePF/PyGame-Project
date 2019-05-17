import pygame
from random import randrange

#Colors for the game
white = (255, 255, 255)
grey = (99, 110, 114)
black = (45, 52, 54)
red = (214, 48, 49)
verde = (34, 112, 147)
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
font = pygame.font.SysFont(None, 25)

def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [largura/4, altura/2])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, grey, [XY[0], XY[1], tamanho, tamanho])

def apple(posX, posY):
    pygame.draw.rect(fundo, red, [posX, posY, tamanho, tamanho])

def game():
    exit = True
    fimDeJogo = False
    posX = randrange(0, largura - tamanho, 10)
    posY = randrange(0, altura - tamanho, 10)
    appleX = randrange(0, largura - tamanho, 10)
    appleY = randrange(0, altura - tamanho, 10)
    velocidadeX = 0
    velocidadeY = 0
    CobraXY = []
    CobraComp = 1
    while exit:
        while fimDeJogo:
            fundo.fill(verde)
            texto("Game Over. "
                  "To continue press C or E to exit.", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = False
                    fimDeJogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        exit = True
                        fimDeJogo = False
                        posX = randrange(0, largura - tamanho, 10)
                        posY = randrange(0, altura - tamanho, 10)
                        appleX = randrange(0, largura - tamanho, 10)
                        appleY = randrange(0, altura - tamanho, 10)
                        velocidadeX = 0
                        velocidadeY = 0
                        CobraXY = []
                        CobraComp = 1
                    if event.key == pygame.K_e:
                        exit = False
                        fimDeJogo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidadeX != tamanho:
                    velocidadeY = 0
                    velocidadeX = -tamanho
                if event.key == pygame.K_RIGHT and velocidadeX != - tamanho:
                    velocidadeY = 0
                    velocidadeX = tamanho

                if event.key == pygame.K_UP and velocidadeY != tamanho:
                    velocidadeX = 0
                    velocidadeY = -tamanho
                if event.key == pygame.K_DOWN and velocidadeY != - tamanho:
                    velocidadeX = 0
                    velocidadeY = tamanho

        if exit:
            fundo.fill(black)
            posX += velocidadeX
            posY += velocidadeY

            if posX == appleX and posY == appleY:
                appleX = randrange(0, largura - tamanho, 10)
                appleY = randrange(0, altura - tamanho, 10)
                CobraComp += 2

            # No border
            # if posX > largura:
            #     posX = 0
            # if posX < 0:
            #     posX = largura - tamanho
            #
            # if posY > altura:
            #     posY = 0
            # if posY < 0:
            #     posY = altura - tamanho

            # With border
            if posX > largura:
                fimDeJogo = True
            if posX < 0:
                fimDeJogo = True

            if posY > altura:
                fimDeJogo = True
            if posY < 0:
                fimDeJogo = True

            CobraInicio = []

            CobraInicio.append(posX)
            CobraInicio.append(posY)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            if any (Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimDeJogo = True



            cobra(CobraXY)

            apple(appleX, appleY)
            pygame.display.update()
            relogio.tick(20)

game()
pygame.quit()