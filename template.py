import pygame
pygame.init()


WIDTH = 600
HEIGHT = 600
#set dimensions of the screen
screen= pygame.display.set_mode((WIDTH,HEIGHT))


#main loop
while run:
    #quit event to close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("white")
    #update the display
    pygame.display.update()