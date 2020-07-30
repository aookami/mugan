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
    screen = pygame.display.set_mode((600,600))
    bgd_image = pygame.image.load("bg.png")
    # define a variable to control the main loop
    running = True

    xpos = 1
    ypos = 1
    frame = 0
    partiture = pygame.image.load("partitura.png")
    screen.blit(partiture,(xpos,ypos))
    pygame.display.flip()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            frame = frame +1
            screen.blit(bgd_image, (0,0))
            screen.blit(partiture,(250+math.sin(frame/360)*150,250+math.cos(frame/360)*150))
            pygame.display.flip()
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()