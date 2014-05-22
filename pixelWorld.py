import pygame
from pygame.locals import *


redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)

worldHeight = 480
worldWidth = 640
worldMap = [[0]*worldHeight for x in range(worldWidth)]


def setMap():
    for x in range(worldWidth):
        for y in range(20):
            worldMap[x][worldHeight-y-1] = 1


if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()

    windowWidth, windowHeight = 640, 480
    windowSurfaceObj = pygame.display.set_mode((windowWidth, windowHeight))

    pygame.display.set_caption("Pixel World")

    player = pygame.image.load("resources/char.jpg")

    setMap()

    while 1:
        windowSurfaceObj.fill(whiteColor)
        windowSurfaceObj.blit(player, (100, 100))

        pixArr = pygame.PixelArray(windowSurfaceObj)

        for y in range(worldHeight):
            for x in range(worldWidth):
                if worldMap[x][y] == 1:
                    pixArr[x][y] = redColor
                else:
                    pixArr[x][y] = blueColor
        del pixArr


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pygame.display.flip()
        fpsClock.tick(30)


