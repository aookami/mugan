# import the pygame module, so you can use it
import pygame
import math
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1200,1200))
    bgd_image = pygame.image.load("bg.png")
    bgchardirty = pygame.image.load("bgchardirty.png")

    # define a variable to control the main loop
    running = True

    xpos = 1
    ypos = 1
    frame = 0
    character = pygame.image.load("char.png")
    screen.blit(character,(xpos,ypos))
    pygame.display.flip()
    lastMousePosition = (0,0)
    charPosition = (0,0)
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            frame = frame +1
            mousePosition = pygame.mouse.get_pos()
            print(charPosition)
            screen.blit(bgchardirty, lastMousePosition)
            if frame%2==0: 
                if charPosition[0] < mousePosition[0]:
                    charPosition = (charPosition[0] +1 , charPosition[1])
                else:
                    charPosition = (charPosition[0] -1 , charPosition[1])
                if charPosition[1] < mousePosition[1]:
                    charPosition = (charPosition[0]  , charPosition[1]+1)
                else:
                    charPosition = (charPosition[0] , charPosition[1]-1)

            screen.blit(character, charPosition)
            pygame.display.flip()
            lastMousePosition = mousePosition
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()