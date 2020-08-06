# import the pygame module, so you can use it
import pygame
import math
# define a main function




boundx=600
boundy=600


def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
   
    screen = pygame.display.set_mode((boundx,boundy))
    bgd_image = pygame.image.load("bg.png")
    bgchardirty = pygame.image.load("bgchardirty.png")

    # define a variable to control the main loop
    running = True

    frame = 0
    character = pygame.image.load("char.png")
    charxspeed = 50
    charyspeed = 50
    
    pygame.display.flip()
    lastMousePosition = (0,0)
    charPosition = [300,10]
    charSpeed = [0,0]
    charAcceleration = [0,-1]

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            frame = frame +1
            mousePosition = pygame.mouse.get_pos()
            
            screen.blit(bgchardirty, lastMousePosition)
            # calculate the vector from character to mouse
            # x1-x2, y1-y2
            trackingVector = (mousePosition[0]-charPosition[0], mousePosition[1]-charPosition[1])
            #dist to mouse will be sqrt(distX^2 + distY^2)
            distToPlayer = math.sqrt(math.pow(trackingVector[0],2) + math.pow(trackingVector[1],2))
           

           

            # the rocket can produce  xN of force per second, until it runs out of fuel
            # the force has to be distributed between the two axis
            # jerk will not be taken into account 
            # however, the direction force is applied cannot change instantly
        
            charAcceleration = [0, (mousePosition[1]/100)-1]

            charSpeed[0] = charSpeed[0] + charAcceleration[0]
            charSpeed[1] = charSpeed[1] + charAcceleration[1]

            
            

            charPosition = [charPosition[0] + (charSpeed[0]/100),charPosition[1] + (charSpeed[1]/100)]
            charSpeed = boundLimitCheckSpeed(charPosition,charSpeed)
            charPosition = boundLimitCheckPos(charPosition)
            print("charPosition:" + str(charPosition)  +",charSpeed:"+ str(charSpeed) +",charAccel:" + str(charAcceleration))

            charPositionTuple = (charPosition[0], charPosition[1])
            screen.blit(character, charPositionTuple)
            pygame.display.flip()
            lastMousePosition = charPosition
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     

def boundLimitCheckPos(charPosition):
    if(charPosition[0] >= boundx):
        charPosition[0] = boundx
    if(charPosition[0] <= 0):
        charPosition[0] = 0
    if(charPosition[1] >= boundy):
        charPosition[1] = boundy
    if(charPosition[1] <= 0):
        charPosition[1] = 0
    return charPosition

def boundLimitCheckSpeed(charPosition, charSpeed):
    if(charPosition[0] >= boundx):
        charSpeed[0] = 0
    if(charPosition[0] <= 0):
        charSpeed[0] = 0
    if(charPosition[1] >= boundy):
        charSpeed[1] = 0
    if(charPosition[1] <= 0):
        charSpeed[1] = 0
    return charSpeed
    
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()