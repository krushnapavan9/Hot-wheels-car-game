import random
import pygame

#dice

red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

def text_object (text,font):
    textsurface = font.render(text,True,white)
    return textsurface,textsurface.get_rect()
def display_text(text_msg,text_x,text_y,size):
    largetext = pygame.font.Font('freesansbold.ttf',size)
    textsurface, textrect = text_object(text_msg, largetext)
    textrect.center = (text_x,text_y)
    display.blit(textsurface, textrect)
    
pygame.init()
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("dice visualization")
clock = pygame.time.Clock()
#font = pygame.font.SysFont("none",25)
display_exits = True
while display_exits :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            display_exits = False
    pygame.draw.rect(display, red, [0,400,500,1])
    display_text('NO OF DICE',60,10,20)
    
    pygame.display.update()
    clock.tick(200)
pygame.quit()
