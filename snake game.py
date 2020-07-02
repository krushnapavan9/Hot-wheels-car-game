import pygame
import random


# colors
red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# variables
window_width = 600
window_height = 800
FPS = 10
box_x = 100
box_y = 50
box_width = 500
box_height = 500
snake_width = 10

# to initialize pygame modules ...etc
pygame.init()

#  getting the window to play :)
gamedisplay = pygame.display.set_mode((window_height, window_width))

# naming at the top like caption
pygame.display.set_caption("my first game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("none", 25)

 
def sysmessage(msg, color):
    text = font.render(msg, True, color)
    gamedisplay.blit(text, [(box_x + box_width)/2, (box_y + box_height)/2])


def printsnake(snakelist):
    for block in snakelist:
        pygame.draw.rect(gamedisplay, black, [block[0], block[1], snake_width, snake_width], 0)


def gameloop():
    gameexit = False
    snakelist = [[box_x, box_y]]
    x = box_x
    y = box_y
    mix = snake_width
    miy = 0
    apple_x = random.randrange(box_x, box_x + box_width, snake_width)
    apple_y = random.randrange(box_y, box_y + box_height, snake_width)

    gameover = False

    while not gameexit:

        while gameover:
            gamedisplay.fill(black, [box_x, box_y, box_width, box_height])
            sysmessage("you lose \n p to play again\n q to exit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True
                    continue
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        gameloop()
                    elif event.key == pygame.K_q:
                        gameover = False
                        gameexit = True

        if x < box_x or x > (box_x + box_width - snake_width) or y < box_y or y > box_y + box_height - snake_width:
            gameover = True
            continue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == 32:
                    sleep = True
                    while sleep:
                        for event2 in pygame.event.get():
                            if event2.type == pygame.KEYDOWN:
                                if event2.key == 32:
                                    sleep = False
                if event.key == 273 and miy == 0:
                    miy = -snake_width
                    mix = 0
                elif event.key == 274 and miy == 0:
                    miy = snake_width
                    mix = 0
                elif event.key == 275 and mix == 0:
                    mix = snake_width
                    miy = 0
                elif event.key == 276 and mix == 0:
                    mix = -snake_width
                    miy = 0
            if event.type == pygame.QUIT:
                gameover = True
        # eating apple
        if x == apple_x and y == apple_y:
            apple_x = random.randrange(box_x, box_x + box_width - snake_width, snake_width)
            apple_y = random.randrange(box_y, box_y + box_height - snake_width, snake_width)
            snakelist.append([apple_x, apple_y])

        snakelist.append([x, y])
        snakelist.pop(0)
        # displaying whole
        gamedisplay.fill(white)
        pygame.draw.rect(gamedisplay, red, [box_x, box_y, box_width, box_height], 1)  # box
        pygame.draw.rect(gamedisplay, green, [apple_x, apple_y, snake_width, snake_width], 0)   # apple
        printsnake(snakelist)

        pygame.display.update()
        x += mix
        y += miy
        # if snake hit herself
        if [x, y] in snakelist:
            gameover = True
        clock.tick(FPS)
    pygame.quit()
    return


gameloop()
