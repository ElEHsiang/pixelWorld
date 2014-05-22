import pygame
from pygame.locals import *
from pixelWorldColor import *

blockSize = 3 

windowWidth, windowHeight = 640, 480

worldHeight = 480/blockSize
worldWidth = 640/blockSize
worldMap = [[0]*worldHeight for x in range(worldWidth)]

windowSurfaceObj = ()

def setMap():

    mudDepth = 80
    for x in range(worldWidth):
        for y in range(mudDepth):
            worldMap[x][worldHeight-y-1] = 1
    for x in range(worldWidth):
        for y in range(2):
            worldMap[x][worldHeight-y-1 - mudDepth] = 2

def dumpMap():

    f = open('dumpMap.txt','w')

    for x in range(worldWidth):
        for y in range(worldHeight):
            f.write(str(worldMap[x][y]) + " ")
        f.write('\n')

def drawBlock():

    pixArr = pygame.PixelArray(windowSurfaceObj)

    for y in range(windowHeight / blockSize):
        for x in range(windowWidth / blockSize):

            blockType = worldMap[x][y]

            drawPosX = x * blockSize
            drawPosY = y * blockSize

            if blockType == 0:
                pass
            if blockType == 1:
                pixArr[drawPosX][drawPosY] = mudColor
                pixArr[drawPosX+1][drawPosY] = mudMixColor
                pixArr[drawPosX][drawPosY+1] = mudMixColor
                pixArr[drawPosX+1][drawPosY+1] = mudColor
                pixArr[drawPosX+2][drawPosY] = mudColor
                pixArr[drawPosX][drawPosY+2] = mudColor
                pixArr[drawPosX+2][drawPosY+2] = mudColor
                pixArr[drawPosX+1][drawPosY+2] = mudColor
                pixArr[drawPosX+2][drawPosY+1] = mudColor
            if blockType == 2:
                pixArr[drawPosX][drawPosY] = grassColor
                pixArr[drawPosX+1][drawPosY] = grassMixColor
                pixArr[drawPosX][drawPosY+1] = grassMixColor
                pixArr[drawPosX+1][drawPosY+1] = grassColor
    del pixArr


if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()

    windowSurfaceObj = pygame.display.set_mode((windowWidth, windowHeight))

    pygame.display.set_caption("Pixel World")

    player = pygame.image.load("resources/char.jpg")

    setMap()

    while 1:
        windowSurfaceObj.fill(whiteColor)
        windowSurfaceObj.blit(player, (100, 100))

        drawBlock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pygame.display.flip()
        fpsClock.tick(30)


